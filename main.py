import pandas as pd
import os
from logger_config import logger

class ExcelFolderCreator:
    def __init__(self, excel_filename, columns, excel_data_dir, base_dir='data'):
        if not isinstance(excel_filename, str) or not excel_filename.endswith('.xlsx'):
            raise ValueError("Invalid Excel filename. It should be a string ending with '.xlsx'.")
        if not isinstance(columns, list) or not all(isinstance(col, str) for col in columns):
            raise ValueError("Columns must be a list of strings.")
        if not isinstance(excel_data_dir, str) or not os.path.isdir(excel_data_dir):
            raise ValueError("Invalid Excel data directory. Provide a valid directory path.")
        
        self.excel_filename = excel_filename
        self.columns = columns
        self.excel_data_dir = excel_data_dir
        self.base_dir = base_dir

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.log_handler = logging.StreamHandler()
        self.logger.addHandler(self.log_handler)

    def get_excel_path(self):
        return os.path.join(self.excel_data_dir, self.excel_filename)

    def get_base_path(self):
        return os.path.join(os.getcwd(), self.base_dir)

    def read_excel(self):
        try:
            excel_path = self.get_excel_path()
            return pd.read_excel(excel_path, usecols=self.columns)
        except Exception as e:
            self.logger.error(f"Error reading Excel file '{self.excel_filename}': {str(e)}")
            return None

    def create_folders(self, df):
        base_path = os.path.join(os.getcwd(), self.base_dir)
        try:
            os.makedirs(base_path, exist_ok=True)
            for index, row in df.iterrows():
                folder_path = os.path.join(base_path, *[str(cell) for cell in row])
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    self.logger.info(f"Created folder '{folder_path}'")
                else:
                    self.logger.info(f"Folder '{folder_path}' already exists, skipping.")
        except Exception as e:
            self.logger.error(f"Error creating folders: {str(e)}")

    def process(self):
        df = self.read_excel()
        if df is not None:
            self.create_folders(df)
        else:
            self.logger.error("No data to process.")

if __name__ == '__main__':
    excel_filename = 'your_excel_file.xlsx'
    columns_to_read = ['Column1', 'Column2', 'Column3']
    excel_data_dir = 'path_to_excel_data'

    logging.basicConfig(level=logging.INFO)

    folder_creator = ExcelFolderCreator(excel_filename, columns_to_read, excel_data_dir)
    folder_creator.process()


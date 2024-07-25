import logging
import os

# 创建一个日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建一个文件处理器，将日志写入到文件中
log_file = os.path.join(os.getcwd(), 'app.log')  # 日志文件路径
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

# 创建一个日志格式化器
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 将处理器添加到日志记录器中
logger.addHandler(file_handler)

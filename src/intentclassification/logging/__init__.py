import logging
from datetime import datetime
import os

date = datetime.now().strftime("%m_%d_%Y")
time = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
logging_str = "[%(asctime)s] %(name)s - %(levelname)s - %(message)s"
current_dir = os.getcwd()
LOG_FOLDER = f"logs-{date}"
log_folder_dir = os.path.join(os.path.dirname(current_dir),"logs", LOG_FOLDER)
log_file_path = os.path.join(log_folder_dir, f"logs_{time}.log")
os.makedirs(log_folder_dir, exist_ok = True)

logging.basicConfig(filename = log_file_path,
level = logging.INFO,
format = logging_str)

logger = logging.getLogger(__name__)
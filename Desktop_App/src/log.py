import logging
import os

documents_folder = os.path.expanduser('~/Documents')

emo_log_folder = os.path.join(documents_folder, 'Emo_log_Folder')

os.makedirs(emo_log_folder, exist_ok=True)

log_file_path = os.path.join(emo_log_folder, 'emo_app.log')
logging.basicConfig(filename=log_file_path,filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

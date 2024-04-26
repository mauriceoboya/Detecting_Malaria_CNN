import logging
import os

log_dir = '/home/fibonacci/projects/Detecting_Malaria_CNN/log_dir'
os.makedirs(log_dir, exist_ok=True)
filename = os.path.join(log_dir, 'running.logs')

format_str = '%(asctime)s: %(message)s: %(levelname)s'
logging.basicConfig(
    level=logging.INFO,
    format=format_str,
    handlers=[
        logging.FileHandler(filename=filename),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('malaria_cnn')

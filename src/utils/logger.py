import logging
from datetime import datetime as dt
from pathlib import Path

#########################################################################################

LOG_PATH = 'data/logs'
LOG_NAME = 'pipeline'

def get_logger(name: str):
    """
    Docstring for get_logger
    
    :param name: Description
    """
    
    log_dir = Path(LOG_PATH)
    log_dir.mkdir(parents= True, exist_ok= True)
    
    log_file = log_dir / f"{LOG_NAME}_{dt.now():%Y-%m-%d}.log"
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        
        #
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        
        #
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        #
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
    return logger

#########################################################################################

def log_header(logger):
    """
    Docstring for log_header
    
    :param logger: Description
    """
    
    file_handler = logger.handlers[0]
    
    file_handler.stream.write("\n" + "="*60 + "\n")
    file_handler.stream.write(f"NEW EXECUTION PIPELINE - {dt.now():%Y-%m-%d %H:%M:%S}\n")
    file_handler.stream.write("\n" + "="*60 + "\n")
    
    file_handler.stream.flush()
    
#########################################################################################
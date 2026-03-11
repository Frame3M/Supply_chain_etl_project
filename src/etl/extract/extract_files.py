import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

#########################################################################################

def extract_from_csv(path, encoding='utf-8'):
    """
    Function for extracting data from a CSV file
    
    :param path: File path that constains the data
    :param encoding: Encoding type (default: 'utf-8')
    """
    
    logger.info(f"Reading CSV file: {path}")
    
    try:
        df = pd.read_csv(filepath_or_buffer=path, encoding=encoding)
        logger.info(f"Successfully read file: {path}")
        return df
    
    except Exception as e:
        logger.error(f"Error reading the CSV file '{path}' with enconding '{encoding}': {e}", exc_info=True)
        raise
    
#########################################################################################
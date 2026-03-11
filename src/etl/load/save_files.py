import pandas as pd
import os
from src.utils.logger import get_logger

logger = get_logger(__name__)

#########################################################################################

def save_to_csv(df, save_path, index=False):
    """
    Save DataFrame to a CSV file
    
    :param df: DataFrame
    :param path_to_save: Destination path 
    :param index: (True/False)
    """
    
    logger.info(f"Saving CSV file: {save_path}")
    
    try:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        df.to_csv(save_path, index=index)
        logger.info(f"Successfully saved file: {save_path}")
    
    except Exception as e:
        logger.warning(f"Error saving CSV file {save_path}: {e}", exc_info=True)
    
#########################################################################################
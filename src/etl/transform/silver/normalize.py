import pandas as pd
import numpy as np
from utils.logger import get_logger

logger = get_logger(__name__)

#########################################################################################

def standarize_columns(df):
    """
    Function to standarize columns
    
    :param df: DataFrame
    """
    
    logger.info("Standardizing column names")
    
    try:
        df = df.copy()
    
    except Exception as e:
        logger.error(f"Failed to copy the DataFrame: {e}", exc_info=True)
        raise
    
    try:
        df.colums = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(' ','_')
            .str.replace(r'\(|\)','',regex=True)
        )
    
    except Exception as e:
        logger.error(f"Failed to standardize the columns: {e}", exc_info=True)
        raise
    
    logger.info("Standardization completed")
    
    return df

#########################################################################################
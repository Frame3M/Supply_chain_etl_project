import pandas as pd
import numpy as np
from utils.logger import get_logger

logger = get_logger(__name__)

#########################################################################################

def clean_strings(df):
    """
    Basic text cleaning
    
    :param df: DataFrame
    """
    
    logger.info("Cleaning string values")
    
    try:
        df = df.copy()
        
    except Exception as e:
        logger.error(f"Failed to copy the DataFrame: {e}", exc_info=True)
        raise
    
    types = ['object', 'string']
    string_cols = df.select_dtypes(include=types).columns
    
    if len(string_cols) == 0:
        logger.warning("No string columns found to clear")
    
    for col in string_cols:
        try:
            df[col] = (
                df[col]
                .str.strip()
                .str.title()
            )
            
        except Exception as e:
            logger.warning(f"Could not clean column '{col}', leaving it unchanged: {e}")
        
    uppercase_cols = ['customer_state', 'type', 'order_status', 'market']
    for col in uppercase_cols:
        try:
            df[col] = (
                df[col]
                .str.upper()
            )
        
        except Exception as e:
            logger.warning(f"Could not convert '{col}' to uppercase, leaving it unchanged: {e}")
        
    fix_dict = {
        'Ee. Uu.': 'EE. UU.'
    }
    
    if 'customer_country' in df.columns:
        df['customer_country'] = df['customer_country'].replace(fix_dict)
    
    else:
        logger.warning("The 'customer_country' column does not exist, skipping correction")
        
    logger.info("String cleaning completed")
        
    return df

#########################################################################################

def fix_dtypes(df):
    """
    Data type conversion
    
    :param df: DataFrame
    """
    
    logger.info("Fixing data types")
    
    try:
        df = df.copy()
    
    except Exception as e:
        logger.error(f"Failed to copy the DataFrame: {e}", exc_info=True)
        raise
    
    # Astype
    astype_dict = {
        'customer_zipcode': 'str',
        'late_delivery_risk': 'boolean',
        'order_status': 'category',
        'shipping_mode': 'category',
        'category_name': 'category',
        'department_name': 'category',
        'market': 'category',
        'type': 'category',
        'delivery_status': 'category',
        'customer_segment': 'category',
    }
    
    for col,dtype in astype_dict.items():
        if col not in df.columns:
            logger.warning(f"Column '{col}' not found, skipping conversion to {dtype}")
            continue
        
        try:
            df[col] = df[col].astype(dtype)
            
        except Exception as e:
            logger.error(f"Failer to convert '{col}' to '{dtype}': {e}", exc_info=True)
            raise
        
    # Datetime
    date_cols = ['order_date_dateorders', 'shipping_date_dateorders']
    for col in date_cols:
        if col not in df.columns:
            logger.warning(f"Column '{col}' not found, skipping conversion to {dtype}")
            continue
        
        df[col] = pd.to_datetime(
            df[col],
            format= '%m/%d/%Y %H:%M',
            errors= 'coerce'
        )
        
        invalid = df[col].isnull().sum()
        if invalid > 0.5 * len(df):
            logger.error(f"More than 50% of '{col}' resulted in NaT. Data is corrupted.")
            raise
    
    logger.info("Data type correction completed")
    
    return df

#########################################################################################

def remove_duplicates(df):
    """
    Drop duplicate rows
    
    :param df: DataFrame
    """
    
    logger.info("Dropping complete duplicates")
    
    try:
        df = df.copy()
    
    except Exception as e:
        logger.error(f"Failed to copy the DataFrame: {e}", exc_info=True)
        raise
    
    df = df.drop_duplicates()
    
    logger.info("Complete duplicates removed")
    
    return df

#########################################################################################

def drop_rows_with_nulls(df, subset=[]):
    """
    Drop NaN rows
    
    :param df: DataFrame
    """
    
    logger.info(f"Removing null values from columns: {subset}")
    
    try:
        df = df.copy()
    
    except Exception as e:
        logger.error(f"Failed to copy the DataFrame: {e}", exc_info=True)
        raise
    
    try:
        df = df.dropna(subset= subset, how='any')
    
    except Exception as e:
        logger.error(f"Failed to drop rows with nulls: {e}", exc_info=True)
        raise
    
    logger.info(f"Null values removed")
    
    return df

#########################################################################################

def fill_missing_zipcode(df):
    """
    Fill missing values in customer_zipcode with 'Unknown'
    
    :param df: Description
    """
    
    logger.info("Filling nulls in 'customer_zipcode' with 'Unknown'")
    
    try:
        df = df.copy()
    
    except Exception as e:
        logger.error(f"Failed to copy the DataFrame: {e}", exc_info=True)
        raise
    
    if 'customer_zipcode' in df.columns:
        df['customer_zipcode'] = df['customer_zipcode'].fillna("Unknown")
    
    else:
        logger.warning("Column 'customer_zipcode' not found")
    
    logger.info("Fill operation completed")
    
    return df

#########################################################################################
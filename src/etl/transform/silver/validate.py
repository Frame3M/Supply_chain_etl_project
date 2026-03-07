import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)

#########################################################################################

def validate_non_negative_columns(df, except_cols= []):
    """
    Check numeric columns for non-negative values
    
    :param df: DataFrame
    :param except_cols: Description
    """
    
    logger.info("Validating non-negative numeric columns")
    
    numeric_cols = df.select_dtypes('float64','Float64','int64','Int64').columns.difference(except_cols)
    for col in numeric_cols:
        invalid = (df[col] < 0).sum()
        if invalid > 0:
            logger.error(f"Column '{col}' contains {invalid} negative values")
            raise ValueError(f"Negative values found in '{col}'")
        
#########################################################################################

def validate_date_order(df, start_date, end_date):
    """
    Check that dates are in the correct order
    
    :param df: DataFrame
    :param start_date: Earliest date
    :param end_date: Most recent date
    """
    
    logger.info(f"Validating date order: {start_date} <= {end_date}")
    
    invalid = (df[end_date] < df[start_date]).sum()
    if invalid > 0:
        logger.error(f"{invalid} rows have '{end_date}' earlier than '{start_date}'")
        raise ValueError(f"Invalid date order between '{start_date}' and '{end_date}'")
    
#########################################################################################

def validate_not_null(df, columns):
    """
    Validate that there are no null values
    
    :param df: DataFrame
    :param columns: Columns to validate
    """
    
    logger.info(f"Validating non-null values for columns: {columns}")
    
    for col in columns:
        invalid = df[col].isnull().sum()
        if  invalid > 0:
            logger.error(f"Column '{col}' contains {invalid} null values")
            raise ValueError(f"Null values found in '{col}'")
        
#########################################################################################

def validate_not_future_date(df):
    """
    Validate that there are no future dates
    
    :param df: DataFrame
    """
    
    logger.info(f"Validating non-future date values")
    
    today = pd.Timestamp.now().normalize()
    
    columns = df.select_dtypes('datetime64').columns
    for col in columns:
        invalid = (df[col] > today).sum()
        if invalid > 0:
            logger.error(f"Column '{col}' contains {invalid} future dates")
            raise ValueError(f"Future dates found in '{col}'")

#########################################################################################
        
def validate_item_quantity_not_zero(df):
    """
    Validate that the 'item_quantity' column has no zero values
    
    :param df: DataFrame
    """
    
    logger.info("Validating that the 'order_item_quantity' column contains no zeros")
    
    if 'order_item_quantity' in df.columns:
        invalid = (df['order_item_quantity'] == 0).sum()
        if invalid > 0:
            logger.error(f"Found {invalid} zeros")
            raise ValueError(f"Zero values found")
    
    else:
        logger.warning("The 'order_item_quantity' column does not exist")
    
#########################################################################################


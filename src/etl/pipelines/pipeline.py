from etl.extract.extract_files import extract_from_csv
from etl.transform.silver.normalize import standarize_columns
from etl.transform.silver.cleaning import clean_strings, fix_dtypes, remove_duplicates, drop_rows_with_nulls, fill_missing_zipcode
from etl.transform.silver.validate import validate_non_negative_columns, validate_date_order, validate_not_null, validate_not_future_date, validate_item_quantity_not_zero
from etl.load.save_files import save_to_csv
from utils.logger import log_header, get_logger

logger = get_logger(__name__)

def run_pipeline():
    """
    Orchestrates all ETL stages.
    Each step logs its execution and allows failures to be isolated by stage
    """
    
    #
    log_header(logger)
    logger.info("Pipeline Start")
    
    try:
        # Extract data
        df_raw = extract_from_csv(path= '../../../data/raw/supply_chain_raw.csv', enconding= 'cp1252')
        
        # Transformations
        df = standarize_columns(df_raw)
        df = clean_strings(df)
        df = fix_dtypes(df)
        df = remove_duplicates(df)
        df = drop_rows_with_nulls(df, subset= ['customer_lname', 'customer_zipcode'])
        df = fill_missing_zipcode(df)
        
        # Validations
        validate_not_null(df, columns= ['category_id', 'customer_id', 'department_id', 'order_customer_id', 'order_id', 'order_item_cardprod_id', 'order_item_id', 'product_card_id', 'product_category_id'])
        validate_item_quantity_not_zero(df)
        validate_non_negative_columns(df, except_cols= ['benefit_per_order', 'latitude', 'longitude', 'order_item_profit_ratio', 'order_profit_per_order'])
        validate_date_order(df, 'order_date_dateorders', 'shipping_date_dateorders')
        validate_not_future_date(df)
        
        # Save
        save_to_csv(df, save_path= '../../../data/silver/supply_chain_silver.csv')
        
    except Exception as e:
        logger.error("Execution stopped because of an error", exc_info=True)
        raise
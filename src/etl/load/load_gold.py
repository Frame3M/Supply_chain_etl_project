import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from src.utils.logger import get_logger

logger = get_logger(__name__)

#########################################################################################

def get_supabase_engine() -> None:
    """
    "Creation of a connection to the Supabase database
    """
    
    logger.info("Starting database connection")
    
    load_dotenv()
    
    db_url = os.getenv("SUPABASE_DATABASE_URL")
    
    if not db_url:
        logger.info("Failed to connect to the database")
        raise
    
    engine = create_engine(db_url)
    
    logger.info("Connection established successfully")
    
    return engine
    
#########################################################################################

def load_gold_to_supabase(gold_dict: dict) -> None:
    """
    Loading Gold tables into the Supabase database
    
    :param gold_dict: Dictionary containing Gold tables
    """
    
    logger.info("Starting the process of loading Gold tables into the database")
    
    engine = get_supabase_engine()
    
    for table_name, table in gold_dict.items():
        try:
            table.to_sql(
                name=table_name,
                con=engine,
                schema='gold',
                if_exists='append',
                index=False,
                method='multi',
                chunksize=5000
            )
            
            logger.info(f"Table {table_name} loaded successfully")
            
        except Exception as e:
            logger.error(f"Error loading table {table_name} into the database")
            raise
        
#########################################################################################
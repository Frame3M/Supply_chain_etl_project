import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

#########################################################################################

def get_supabase_engine() -> None:
    """
    "Creation of a connection to the Supabase database
    """
    
    load_dotenv()
    
    db_url = os.getenv("SUPABASE_DATABASE_URL")
    
    if not db_url:
        raise
    
    engine = create_engine(db_url)
    return engine
    
#########################################################################################

def load_gold_to_supabase(gold_dict: dict) -> None:
    """
    Loading Gold tables into the Supabase database
    
    :param gold_dict: Dictionary containing Gold tables
    """
    
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
            
        except Exception as e:
            raise
        
#########################################################################################
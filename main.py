from src.etl.pipelines.pipeline import run_pipeline
from src.utils.logger import get_logger

logger = get_logger(__name__)

def main() -> None:
    """
    
    """
    
    logger.info("Starting ETL execution")
    
    try:
        run_pipeline()
        logger.info("ETL completed successfully")
        
    except Exception as e:
        logger.exception(f"Critical error during ETL execution: {e}")
        

if __name__ == "__main__":
    main()
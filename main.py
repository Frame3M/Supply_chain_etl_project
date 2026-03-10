from src.etl.pipelines.pipeline import run_pipeline
from src.utils.logger import get_logger

logger = get_logger(__name__)

def main() -> None:
    """
    
    """
    
    logger.info("Iniciando ejecucion del ETL")
    
    try:
        run_pipeline()
        logger.info("ETL finalizado correctamente")
        
    except Exception as e:
        logger.exception(f"Error critico durante la ejecucion del ETL: {e}")
        

if __name__ == "__main__":
    main()
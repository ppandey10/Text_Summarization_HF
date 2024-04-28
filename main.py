from txtsummarizer.pipeline.step1_data_ingestion import DataIngestionTrainingPipeline
from txtsummarizer.pipeline.step2_data_validation import DataValidationPipeline
from txtsummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

#===================================================================================#
STAGE_NAME = "Data Validation Stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


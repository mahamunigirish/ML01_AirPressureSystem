from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import  get_collection_as_dataframe
# from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity import config_entity
import os ,sys
from sensor.components import data_ingestion
from sensor.components.data_validation import DataValidation

if __name__ == "__main__":
    try:
        traning_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(traning_pipeline_config)
        print(data_ingestion_config.to_dict())

        # ✅ Start data ingestion
        data_ingestion_instance = data_ingestion.DataIngestion(data_ingestion_config)
        data_ingestion_artifact = data_ingestion_instance.initiate_data_ingestion()
        print(data_ingestion_artifact)

        # start data validation 

        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=traning_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,
                                         data_ingestion_artifact=data_ingestion_artifact)
        
        data_validation_artifact =  data_validation.initiate_data_validation()

        
        
    except Exception as e:
        print(e)

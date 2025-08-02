from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import  get_collection_as_dataframe
# from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity import config_entity
import os ,sys
from sensor.components import data_ingestion

if __name__ == "__main__":
    try:
        traning_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(traning_pipeline_config)
        print(data_ingestion_config.to_dict())
    except Exception as e:
        print(e)

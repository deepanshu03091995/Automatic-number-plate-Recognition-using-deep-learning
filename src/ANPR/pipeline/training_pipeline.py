import os,sys
from src.ANPR.config.s3_operations import S3Operation
from src.ANPR.entity.config_entity import *
from src.ANPR.entity.artifacts_entity import *
from src.ANPR.logger import logging
from src.ANPR.exception import ANPRException
from src.ANPR.constants import *
from src.ANPR.components.data_ingestion import DataIngestion


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.s3_operations = S3Operation()
    
    
    def start_data_ingestion(self)->DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the compressed data from S3 Bucket")
            data_ingestion_obj = DataIngestion(data_ingestion_config=self.data_ingestion_config,
            s3_operations=self.s3_operations)
            data_ingestion_artifact = data_ingestion_obj.initiate_data_ingestion()
            logging.info("Got the extracted data ")
            return data_ingestion_artifact
        except Exception as e:
            raise ANPRException(e, sys)    
        
        
        
    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise ANPRException(e, sys)        
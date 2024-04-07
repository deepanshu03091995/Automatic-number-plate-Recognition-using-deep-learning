import os,sys
from src.ANPR.config.s3_operations import S3Operation
from src.ANPR.entity.config_entity import *
from src.ANPR.entity.artifacts_entity import *
from src.ANPR.logger import logging
from src.ANPR.exception import ANPRException
from src.ANPR.constants import *
from src.ANPR.components.data_ingestion import DataIngestion
from src.ANPR.components.data_transformation import DataTransformation
from src.ANPR.components.prepare_base_model import PrepareBaseModel


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.prepare_base_model_config = PrepareBaseModelConfig()
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
    
    def start_data_transformation(self,data_ingestion_artifact : DataIngestionArtifacts)->DataTransformationArtifacts:
        try:
            logging.info("Entered the start_data_transformation method of TrainPipeline class")
            data_transformation_obj = DataTransformation(data_transformation_config=self.data_transformation_config,
            data_ingestion_artifact=data_ingestion_artifact)

            data_transformation_artifact = data_transformation_obj.initiate_data_transformation()
            logging.info("Exited the start_data_transformation method of TrainPipeline class")
            return data_transformation_artifact
            
        except Exception as e:
            raise ANPRException(e, sys)    
    
    def prepare_base_model(self)->PrepareBaseModelArtifacts:
        try:
            logging.info("Entered the prepare_callbacks method of TrainPipeline class")
            prepare_base_model_obj = PrepareBaseModel(prepare_base_model_config=self.prepare_base_model_config)
            prepare_base_model_artifact = prepare_base_model_obj.initiate_prepare_base_model()
            return prepare_base_model_artifact

        except Exception as e:
            raise ANPRException(e, sys)    
        
    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact)
            prepare_base_model_artifact = self.prepare_base_model()
        except Exception as e:
            raise ANPRException(e, sys)        
import sys
from src.ANPR.exception import ANPRException
from src.ANPR.logger import logging
from src.ANPR.pipeline.training_pipeline import TrainPipeline

train_obj = TrainPipeline()
train_obj.run_pipeline()
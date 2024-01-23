import os, sys
from housing.logger import logging
from housing.exception import HousingException
from housing.util.util import load_numpy_array_data
from housing.config.configuration import ModelTrainerConfig
from housing.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact


class ModelTrainer:
    def __init__(self, model_trainer_config:ModelTrainerConfig, data_transformation_artifact:DataTransformationArtifact):
        try:
            logging.info(f"{'='*20}Model Training log Started.{'='*20}\n\n")
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise HousingException(e, sys) from e
        
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            logging.info(f"Loading transformed training dataset")
            transformed_training_file_path = self.data_transformation_artifact.transformed_train_file_path
            train_array = load_numpy_array_data(file_path=transformed_training_file_path)

            logging.info(f"Loading transformed testing dataset")
            transformed_testing_file_path = self.data_transformation_artifact.transformed_test_file_path
            test_array = load_numpy_array_data(file_path=transformed_testing_file_path)

            logging.info(f"Splitting training and testing target input features")
            x_train, y_train, x_test, y_test = train_array[:,:-1], train_array[:,-1], test_array[:,:-1], test_array[:,-1]

            logging.info(f"Extracting model config file path")
            model_config_file_path = self.model_trainer_config.model_config_file_path

            logging.info(f"Initializing model factory class using the model config file : {model_config_file_path}")
            #model_factory = ModelF
        except Exception as e:
            raise HousingException(e, sys) from e
from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.config.configuration import Configuration 

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # data_validation_config = Configuration()
        # print(data_validation_config.get_data_validation_config())
    except Exception as e:
        logging.error(f"{e}")
        print("Exception : ", e)

if __name__ == "__main__":
    main()
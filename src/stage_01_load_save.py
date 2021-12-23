import os.path

from src.utils.all_utils import read_yaml,create_directory
import argparse
import pandas as pd

def get_data(config):
    config_Data=read_yaml(config)
    df=pd.read_csv(config_Data["data_source"],sep=";")
    ##print(df.head())

    ## save data set in the local directory
    ## create path to directory: artifacts/raw_localdirectory/data.csv
    artifacts_dir=config_Data["artifacts"]["artifacts_dir"]
    raw_local_dir=config_Data["artifacts"]["raw_local_dir"]
    raw_local_files=config_Data["artifacts"]["raw_local_files"]

    ## path creator
    raw_local_dir_path=os.path.join(artifacts_dir,raw_local_dir)

    ## create folders for the path
    create_directory([raw_local_dir_path])

    raw_local_files_path=os.path.join(raw_local_dir_path,raw_local_files)

    ## saving the dataframe to a local csv file in the
    df.to_csv(raw_local_files_path,sep=",",index=False)

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    parsed_args=args.parse_args()
    get_data(config=parsed_args.config)
    ##get_data("config/config.yaml")



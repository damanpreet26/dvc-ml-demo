import os.path
from src.utils.all_utils import *
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(config, params):
    config_Data=read_yaml(config)
    params_Data = read_yaml(params)

    ## create path to directory: artifacts/raw_localdirectory/data.csv
    artifacts_dir = config_Data["artifacts"]["artifacts_dir"]
    raw_local_dir = config_Data["artifacts"]["raw_local_dir"]
    raw_local_files = config_Data["artifacts"]["raw_local_files"]
    split_data_dir = config_Data["artifacts"]["split_data_dir"]
    train_filename = config_Data["artifacts"]["train"]
    test_filename = config_Data["artifacts"]["test"]

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
    raw_local_files_path = os.path.join(raw_local_dir_path, raw_local_files)


    df=pd.read_csv(raw_local_files_path, sep=",")

    random_state_val = params_Data["base"]["random_state"]
    test_size_val = params_Data["base"]["test_size"]
    ## splitting the data

    train, test = train_test_split(df, test_size=test_size_val, random_state=random_state_val )
    train_data_path = os.path.join(artifacts_dir, split_data_dir,train_filename)
    test_data_path = os.path.join(artifacts_dir, split_data_dir, test_filename)

    ## create folders
    create_directory([os.path.join(artifacts_dir,split_data_dir)])

    for data, data_path in (train, train_data_path), (test, test_data_path):
        save_local_files(data, data_path)


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args=args.parse_args()
    split_data(config=parsed_args.config,params=parsed_args.params)
    ##get_data("config/config.yaml")



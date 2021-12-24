import os.path
from src.utils.all_utils import *
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import joblib

def training(config, params):
    config_Data=read_yaml(config)
    params_Data = read_yaml(params)

    ## create path to directory: artifacts/raw_localdirectory/data.csv
    artifacts_dir = config_Data["artifacts"]["artifacts_dir"]
    split_data_dir = config_Data["artifacts"]["split_data_dir"]
    train_filename = config_Data["artifacts"]["train"]
    test_filename = config_Data["artifacts"]["test"]
    l1_ratio_val = params_Data["Model_params"]["Elasticnet"]["l1_ratio"]
    alpha_val = params_Data["Model_params"]["Elasticnet"]["alpha"]
    random_state_val = params_Data["base"]["random_state"]
    model_dir = config_Data["artifacts"]["model_dir"]
    model_file = config_Data["artifacts"]["model_file"]

#    test_size_val = params_Data["base"]["test_size"]

    ## Read training data
    df = pd.read_csv(os.path.join(artifacts_dir, split_data_dir, train_filename))

    ## splitting the data into X/Y variables
    train_y = df["quality"]
    train_x = df.drop(columns=["quality"], axis=1)

    model = ElasticNet(alpha=alpha_val, l1_ratio=l1_ratio_val, random_state=random_state_val)
    model.fit(train_x, train_y)
    print("done")

    model_dir = os.path.join(artifacts_dir, model_dir)
    create_directory([model_dir])
    model_path = os.path.join(model_dir, model_file)

    print(model_path)
    joblib.dump(model, model_path)



if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args=args.parse_args()
    training(config=parsed_args.config,params=parsed_args.params)
    ##get_data("config/config.yaml")



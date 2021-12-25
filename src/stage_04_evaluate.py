import os.path
from src.utils.all_utils import *
import argparse
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score


def evaluate_metrics(test, predict):
    rmse = np.sqrt(mean_absolute_error(test, predict))
    mae = mean_absolute_error(test, predict)
    r2 = r2_score(test, predict)
    return rmse, mae, r2


def training(config, params):
    config_Data=read_yaml(config)
    params_Data = read_yaml(params)

    ## create path to directory: artifacts/raw_localdirectory/data.csv
    artifacts_dir = config_Data["artifacts"]["artifacts_dir"]
    split_data_dir = config_Data["artifacts"]["split_data_dir"]
    test_filename = config_Data["artifacts"]["test"]
    random_state_val = params_Data["base"]["random_state"]
    model_dir = config_Data["artifacts"]["model_dir"]
    model_file = config_Data["artifacts"]["model_file"]
    report_dir = config_Data["artifacts"]["report_dir"]
    report_file = config_Data["artifacts"]["report_file"]

    test_file = pd.read_csv(os.path.join(artifacts_dir,split_data_dir,test_filename))

    test_x = test_file.drop("quality", axis=1)
    test_y = test_file["quality"]

    model_path = os.path.join(artifacts_dir,model_dir, model_file)

    model1 = joblib.load(model_path)

    pred_vals = model1.predict(test_x)
    rmse,mae,r2= evaluate_metrics(test_y, pred_vals)

    ##print("rmse:",rmse,"| mae:",mae,"| r2:",r2)
    report_val = {"RMSE" : rmse ,"MAE" : mae , "R2" : r2}

    print(report_val)


    ##saving the report in the report_dir

    report_dir_val = os.path.join(artifacts_dir,report_dir)
    create_directory([report_dir_val])
    report_file_val = os.path.join(report_dir_val,report_file)

    save_reports(report_val, report_file_val)





if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args=args.parse_args()
    training(config=parsed_args.config,params=parsed_args.params)
    ##get_data("config/config.yaml")



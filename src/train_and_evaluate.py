# Load the train and test 
# train algorithm
# save the metrics, and params

import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params
import argparse
import joblib
import json

def eval_metrics(actual, predicted):
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mae = mean_absolute_error(actual, predicted)
    r2 = r2_score(actual, predicted)

    return (rmse, mae, r2)

def train_and_evaluate(config_path):
    config = read_params(config_path)

    test_data_path = config['split_data']['test_path']
    train_data_path = config['split_data']['train_path']
    random_state = config['base']['random_state']

    model_dir = config['model_dir']

    alpha = config['estimators']['ElasticNet']['params']['alpha']
    l1_ratio = config['estimators']['ElasticNet']['params']['l1_ratio']
    target = [config['base']['target_col']]

    train = pd.read_csv(train_data_path, sep=',')
    test = pd.read_csv(test_data_path, sep=',')

    train_y = train[target]
    test_y = test[target]

    train_X = train.drop(target, axis=1)
    test_X = test.drop(target, axis=1)

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)

    lr.fit(train_X, train_y)

    predicted_qualities = lr.predict(test_X)   

    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    print(
        f"""RMSE {rmse}\n
         MAE {mae}\n
         R2 SCORE {r2}"""
    )




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
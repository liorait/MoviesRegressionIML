import numpy as np


def load_data(pathname):
    """
    Loads the data
    :return:
    """
    pass


def preprocess(X):
    """
    PreProcessing the data
    :param X:
    :return: X
    """
    pass


def train_val_test(X):
    """
    Divides the data into train and test parts - train (70%), validation(10%), test(20%)
    returns X and a response vector y todo add response vector y2
    :param X: PreProcessed data
    :return: X, y
    """
    pass


def train(X, y):
    """
    Trains the model
    :param X: PreProcessed data
    :param y: response vector
    :return: coefficients vector w
    """
    pass


def predict(X):
    """
    Receives row data, pre-processing the data and predicts the model
    :param X: PreProcessed data
    :return: y
    """
    pass


def error_rate(y, y_hat):
    """
    Calculates the error rate using RMSE
    :param y: the response vector
    :param y_hat: the predicted vector
    :return: the error rate
    """
    pass


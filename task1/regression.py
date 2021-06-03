import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(pathname):
    """
    Loads the data
    :return:
    """
    movies_df = pd.read_csv(pathname)
    return movies_df


def preprocess(X):
    """
    PreProcessing the data
    :param X:
    :return: X
    """
    return X


def train_val_test_split(X):
    """
    Divides the data into train and test parts - train (70%), validation(10%), test(20%)
    returns X and a response vector y todo add response vector y2
    :param X: PreProcessed data
    :return: X, y
    """
    train, test = train_test_split(X, test_size=0.2)
    train, validation = train_test_split(X, test_size=0.125)
    return train, validation, test


def train(X, y):
    """
    Trains the model
    :param X: PreProcessed data
    :param y: response vector
    :return: coefficients vector w
    """
    pass


def predict(X, w):
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
    return np.sqrt(np.mean((y-y_hat)**2))


if __name__ == '__main__':
 #   movies_df = load_data("movies_dataset.csv")
 #   train, validation, test = train_val_test_split(movies_df)

    train_data = np.load("train.npy", allow_pickle=True)
    validation = np.load("validation.npy", allow_pickle=True)
    test = np.load("test.npy", allow_pickle=True)
    train = preprocess(train)




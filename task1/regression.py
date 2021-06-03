import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures


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
    Trains the model.
    Excepting and return numpy arrays.
    :param X: PreProcessed data
    :param y: response vector
    :return: coefficients vector w
    """
    k = choose_degree(X, y)
    return make_pipeline(PolynomialFeatures(k), LinearRegression()).fit(X, y)


def predict(X, w):
    """
    Receives row data, pre-processing the data and predicts the model.
    Excepting and return numpy arrays.
    :param X: PreProcessed data
    :return: y
    """
    return w.predict(X)


def error_rate(y, y_hat):
    """
    Calculates the error rate using RMSE
    :param y: the response vector
    :param y_hat: the predicted vector
    :return: the error rate
    """
    return np.sqrt(np.mean((y - y_hat) ** 2))


def choose_degree(X, y):
    """
    Finds the best degree for the polynomial that causes the lowest error rate.
    :param X: PreProcessed data
    :param y: response vector
    :return: the best degree for the polynomial.
    """
    ks = [2, 3, 4, 5, 100]
    best_degree = 0
    max_accurate = 0
    for i, k in enumerate(ks):
        y_hat = make_pipeline(PolynomialFeatures(k), LinearRegression()).fit(X, y).predict(X)
        accurate = 1 - error_rate(y, y_hat)
        if accurate > max_accurate:
            max_accurate = accurate
            best_degree = k

    return best_degree


if __name__ == '__main__':
    movies_df = load_data("movies_dataset.csv")
    train, validation, test = train_val_test_split(movies_df)
    train = preprocess(train)

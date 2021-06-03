import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
import preprocessing
import matplotlib.pyplot as plt


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
    :param X: the original data
    :return: X the preprocess data
    """
    return preprocessing.process_begin(X)


def train_val_test_split(X, y):
    """
    Divides the data into train and test parts - train (70%), validation(10%), test(20%)
    returns X and a response vector y
    :param X: PreProcessed data
    :return: X, y
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=0.125, random_state=42)
    return X_train, X_validation, X_test, y_train, y_validation, y_test


def split_X_y(X):
    """
    split to X- the PreProcessed data and y- response array with 2 columns
    (revenue and vote_average)
    :param X: PreProcessed data
    :return: X, y
    """
    y = pd.DataFrame(X, columns=["revenue", "vote_average"])
    X = X.drop("revenue", axis=1)
    X = X.drop("vote_average", axis=1)
    return X, y


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
        error = error_rate(y, y_hat)
        error /= len(y)
        accurate = 1 - error
        if accurate > max_accurate:
            max_accurate = accurate
            best_degree = k

    return best_degree


if __name__ == '__main__':
    movies_df = load_data("movies_dataset.csv")
    movies_df = preprocess(movies_df)
    X, y = split_X_y(movies_df)
    X_train, X_validation, X_test, y_train, y_validation, y_test = train_val_test_split(X, y)

    # check which regression is better
    y_train = y_train.to_numpy()
    X_train = X_train.to_numpy()
    lin_reg = LinearRegression().fit(X_train, y_train)
    w = lin_reg.coef_
    y_hat = lin_reg.predict(X_test)
    linear_error_rate = error_rate(y_test, lin_reg.predict(X_test))
    plt.plot(list(range(len(y))))
    """
    poly_w = train(X_train, y_train)
    y_hat_poly = predict(X_test, poly_w)
    poly_error_rate = error_rate(y_test, y_hat_poly)
    print(poly_error_rate)
    """

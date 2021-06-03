import numpy as np
import pandas as pd


def remove(data, feature):
    data = data.drop([feature], axis=1)
    return data


def add_dummy(data, feature):
    dummy = pd.get_dummies(data.feature, prefix=feature)
    data = pd.concat([data, dummy], axis=1)
    return data


def belongs_to_collection(data):
    print(data["belongs_to_collection"])


def do_changes(data):
    remove_features = ["id", "homepage", "original_title"]
    for feature in remove_features:
        data = remove(feature)
    belongs_to_collection()


if __name__ == '__main__':
    movies_df = pd.read_csv("movies_dataset.csv")
    belongs_to_collection(movies_df)

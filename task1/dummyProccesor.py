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
    data['belongs_to_collection'] = data['belongs_to_collection'].fillna(0)
    data.loc[data.belongs_to_collection != 0, 'belongs_to_collection'] = 1


def do_changes(data):
    remove_features = ["id", "homepage", "original_title"]
    for feature in remove_features:
        data = remove(data, feature)
    belongs_to_collection(data)


def genre(data):
    pass


def original_language(data):
    most_common = ['en', 'fr', 'hi', 'ru', 'es', 'ja']
    data.loc[-data.original_language.isin(most_common), 'original_language'] = 'other'
    dummy = pd.get_dummies(data.original_language, prefix='original_language')
    data = pd.concat([data, dummy], axis=1)
    data = remove(data, 'original_language')
    return data


if __name__ == '__main__':
    # behatzlacha kapara
    movies_df = pd.read_csv("movies_dataset.csv")
    genre(movies_df)
    original_language(movies_df)

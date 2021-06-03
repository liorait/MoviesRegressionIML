import ast
import numpy as np
import pandas as pd


def remove(data, feature):
    """
    remove feature from data
    :param data: data frame
    :param feature:
    :return: the data without the feature
    """
    data = data.drop([feature], axis=1)
    return data


def add_dummy(data, feature):
    dummy = pd.get_dummies(data.feature, prefix=feature)
    data = pd.concat([data, dummy], axis=1)


def belongs_to_collection(data):
    """
    preprocess the feature belongs_to_collection into dummies vectors
    0 if no collection, 1 if in a collection
    :param data: movies data frame
    :return: edited data frame
    """
    data['belongs_to_collection'] = data['belongs_to_collection'].fillna(0)
    data.loc[data.belongs_to_collection != 0, 'belongs_to_collection'] = 1
    return data


def do_changes(data):
    data = belongs_to_collection(data)
    data = original_language(data)
    data = genre(data)
    return data


def genre(data):
    """
    preprocess the feature genres into dummies vectors
    :param data: movies data frame
    :return: edited data frame
    """
    genre_load = data["genres"].apply(ast.literal_eval)
    for i in range(len(genre_load)):
        genre_list = genre_load[i]
        arr = []
        for genre_dict in genre_list:
            if 'name' in genre_dict:
                arr.append(genre_dict['name'])
        genre_load[i] = arr
    data['genres'] = genre_load
    dummy = pd.get_dummies(data.genres.apply(pd.Series).stack()).sum(level=0)
    data = pd.concat([data, dummy], axis=1)
    data = remove(data, 'genres')
    return data


def cast(data):
    genre_load = data["cast"].apply(ast.literal_eval)
    for i in range(len(genre_load)):
        genre_list = genre_load[i]
        arr = []
        for genre_dict in genre_list:
            if 'name' in genre_dict:
                arr.append(genre_dict['name'])
        genre_load[i] = arr
    data['cast'] = genre_load
    # dummy = pd.get_dummies(data.genres.apply(pd.Series).stack()).sum(level=0)
    # data = pd.concat([data, dummy], axis=1)
    # data = remove(data, 'cast')
    return data


def original_language(data):
    """
    preprocess the feature original_language into dummies vectors
    :param data: movies data frame
    :return: edited data frame
    """
    most_common = ['en', 'fr', 'hi', 'ru', 'es', 'ja']
    data.loc[-data.original_language.isin(most_common), 'original_language'] = 'other'
    dummy = pd.get_dummies(data.original_language, prefix='original_language')
    data = pd.concat([data, dummy], axis=1)
    data = remove(data, 'original_language')
    return data


def production_companies(data):
    pc_load = data["production_companies"].apply(ast.literal_eval)
    for i in range(len(pc_load)):
        pc_list = pc_load[i]
        arr = []
        for pc_dict in pc_list:
            if 'name' in pc_dict:
                arr.append(pc_dict['name'])
        pc_load[i] = arr
    data['production_companies'] = pc_load

    all = []
    for i in range(len(pc_load)):
        all += pc_load[i]
    all = np.array(all)
    print(len(np.unique(all)))
    print(np.unique(all))

    # dummy = pd.get_dummies(data.genres.apply(pd.Series).stack()).sum(level=0)
    # data = pd.concat([data, dummy], axis=1)
    # data = remove(data, 'production_companies')
    return data


def production_countries(data):
    pc_load = data["production_countries"].apply(ast.literal_eval)
    for i in range(len(pc_load)):
        pc_list = pc_load[i]
        arr = []
        for pc_dict in pc_list:
            if 'name' in pc_dict:
                arr.append(pc_dict['name'])
        pc_load[i] = arr
    data['production_countries'] = pc_load

    all = []
    for i in range(len(pc_load)):
        all += pc_load[i]
    all = np.array(all)
    print(len(np.unique(all)))
    print(np.unique(all))

    # dummy = pd.get_dummies(data.genres.apply(pd.Series).stack()).sum(level=0)
    # data = pd.concat([data, dummy], axis=1)
    # data = remove(data, 'production_companies')
    return data


if __name__ == '__main__':
    # behatzlacha kapara
    movies_df = pd.read_csv("movies_dataset.csv")
    cast(movies_df)

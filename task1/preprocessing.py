import pandas as pd
import ast
import json

TAGLINE_FEATURE = "tagline"
TITLE_FEATURE = "title"
KEYWORDS_FEATURE = "keywords"
RUNTIME_FEATURE = "runtime"
RELEASED = "Released"

cast_dict = {}
keyword_dict = {}
producer_dict = {}
director_dict = {}
writer_dict = {}
RUNTIME_FEATURE = "runtime"
RELEASED = "Released"

cast_dict = {}
keyword_dict = {}
producer_dict = {}
director_dict = {}
writer_dict = {}

DEPARTMENT = "known_for_department"

PRODUCER = "Production"
DIRECTOR = "Directing"
WRITER = "Writing"


def remove(data, feature):
    """
    remove feature from data
    :param data: data frame
    :param feature:
    :return: the data without the feature
    """
    data = data.drop([feature], axis=1)
    return data


def add_value_to_cast(cast_data, revenue, vote_average):
    """
    Creates actor dict
    :param cast_data: cell in cast column
    :param revenue: the revenue of the current row
    :param vote_average:
    :return:
    """
    for actor in cast_data:
        actor = json.load(actor)
        actor_id_num = actor[id]
        if actor_id_num in cast_dict:
            cast_dict[actor_id_num].append((revenue, vote_average))
        else:
            cast_dict[actor_id_num] = [(revenue, vote_average)]


# Creates producer_dict,
def add_value_to_crew(crew_data, revenue, vote_average):
    """
    Creates producer_dict, writer_dict, director_dict
    :param crew_data: cell in crew column
    :param revenue: the revenue of the current row
    :return:
    """
    # for each worker in the row, crates a dict with the worker's data
    for worker in crew_data:
        worker = json.load(worker)
        if worker[DEPARTMENT] == PRODUCER:
            worker_id_num = worker[id]
            if worker_id_num in producer_dict:
                producer_dict[worker_id_num].append((revenue, vote_average))
            else:  # creates a new actor
                producer_dict[worker_id_num] = [(revenue, vote_average)]
        elif worker[DEPARTMENT] == DIRECTOR:
            worker_id_num = worker[id]
            if worker_id_num in director_dict:
                director_dict[worker_id_num].append((revenue, vote_average))
            else:
                director_dict[worker_id_num] = [(revenue, vote_average)]
        elif worker[DEPARTMENT] == WRITER:
            worker_id_num = worker[id]
            if worker_id_num in writer_dict:
                writer_dict[worker_id_num].append((revenue, vote_average))
            else:
                writer_dict[worker_id_num] = [(revenue, vote_average)]


def calculate_crew_value(crew_dict):
    """
    Calculate the average of revenue and vote_average for each crew member in the dict
    :param crew_dict: dict of crew members
    :return: the dict after replacing the list in the average value
    """
    for key in crew_dict:
        revenue_list = crew_dict[key][0]
        vote_average_list = crew_dict[key][1]

        average_of_revenue = sum(revenue_list) / len(revenue_list)
        average_of_vote = sum(vote_average_list) / len(vote_average_list)

        crew_dict[key][0] = average_of_revenue
        crew_dict[key][1] = average_of_vote

        # for each crew member save a grade constructed of 70% revenue average and 30% vote average
        crew_dict[key] = average_of_revenue * 0.7 + average_of_vote * 0.3
    return crew_dict


def calculate_crew_average(crew_data):
    """
    calculates average between crew roles: writer,producer, director in the following way:
    gets a value in the crew_data column
    for each worker that is in producer, writer, director
    goes to the dict in the relevant worker id
    gets its rank , calculates the average and saves in the cell
    :param crew_data: a value in the crew_data column
    :return: total crew rank
    """
    rank_of_producer = []
    rank_of_writer = []
    rank_of_director = []

    for worker in crew_data:
        worker = json.load(worker)
        if worker[DEPARTMENT] == PRODUCER:
            worker_id_num = worker[id]
            if worker_id_num in producer_dict:
                rank_of_producer.append(producer_dict[worker_id_num])  # adds to the list of producer's rank the rank
        elif worker[DEPARTMENT] == WRITER:
            worker_id_num = worker[id]
            if worker_id_num in writer_dict:
                rank_of_writer.append(writer_dict[worker_id_num])  # adds to the list of writer's rank the rank
        elif worker[DEPARTMENT] == DIRECTOR:
            worker_id_num = worker[id]
            if worker_id_num in director_dict:
                rank_of_director.append(director_dict[worker_id_num])  # adds to the list of directors's rank the rank

    sum_of_producers_rank = sum(rank_of_producer)
    sum_of_director_rank = sum(rank_of_director)
    sum_of_writer_rank = sum(rank_of_writer)

    total_crew_average_rank = (sum_of_producers_rank + sum_of_director_rank + sum_of_writer_rank) / 3
    crew_data = total_crew_average_rank
    return crew_data


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


def crew_cast_process(data):
    """
    preprocess data in crew column and in cast column
    :return:
    """
    # todo for each row get the cell in the crew column
    for row in data:
        revenue = 0  # todo the revenue
        vote_average = 0  # todo the vote of the line

        # crew part
        crew_data = [{}]  # todo the cell in crew column

        # create producer_dict, writer_dict, director_dict
        add_value_to_crew(crew_data, revenue, vote_average)

        # cast part
        cast_data = [{}]  # todo the cell in crew column

        # create dict of cast - for each cast member save revenue & vote average
        add_value_to_cast(cast_data, revenue, vote_average)

    # for each dict calculate the crew value
    calculate_crew_value(producer_dict)
    calculate_crew_value(writer_dict)
    calculate_crew_value(director_dict)
    calculate_crew_value(cast_dict)

    for row in data:
        crew_data = [{}]  # todo get the cell
        cast_data = [{}]  # todo the cell in crew column
        crew_data = calculate_crew_value(crew_data)
        # todo replace the cell in crew column with the new crew_data

    # cast_data = calculate_cast_value(cast_data)
    # todo replace the cell in cast column with the new crew_data

    return data


def process_nan(data):
    features = list(data.columns)
    for f in features:
        avrage = data[f].mean()
        data[f] = data[f].fillna(avrage)

    return data


def process_begin(data):
    """
    Processes the data
    :param data: A dataframe
    :return:
    """
    # processed_data = copy.deepcopy (data)

    # remove columns
    remove_features = ["id", "homepage", "original_title",
                       "production_companies", "production_countries", "title", "keywords", "tagline"]
    for feature in remove_features:
        data = remove(data, feature)

    # remove rows with invalid values
    data = data[data.runtime != 0]  # keep rows that their runtime is not 0
    data = data[data.runtime != ""]  # keep rows that their runtime is not None
    data = data[data.status == RELEASED]  # keep rows that their status is released
    data = data[data.crew != ""]  # keep rows that their crew is not None
    data = data[len(data.crew) == 0]  # keep rows that their crew is empty

    for line in data:
        pass

    data = belongs_to_collection(data)
    data = original_language(data)
    data = genre(data)
    data = crew_cast_process(data)

    # remove rows with invalid values
    data = data.drop(data[data.runtime == 0].index)  # keep rows that their runtime is not 0
    data = data.drop(data[data.runtime == ""].index)  # keep rows that their runtime is not None
    data = data.drop(data[data.status != RELEASED].index)  # keep rows that their status is released
    data.dropna(subset=["revenue"], inplace=True)  # keep rows that their status is released
    data.dropna(subset=["vote_count"], inplace=True)  # keep rows that their status is released
    data = remove(data, "status")
    data = process_nan(data)

    # Add intercept vector
    data.insert(loc=0, column="new_one", value=[1] * len(data.index))

    return data

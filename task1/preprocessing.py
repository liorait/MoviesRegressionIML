import copy
import dummyProccesor as pro
import json

TAGLINE_FEATURE ="tagline"
TITLE_FEATURE = "title"
KEYWORDS_FEATURE ="keywords"
RUNTIME_FEATURE ="runtime"
RELEASED = "Released"


cast_dict={}
keyword_dict={}
producer_dict={}
director_dict={}
writer_dict={}

DEPARTMENT="known_for_department"

PRODUCER = "Production"
DIRECTOR = "Directing"
WRITER = "Writing"

# some change

def add_value_to_cast(cast_data, revenue):
    for actor in cast_data:

        actor_id_num=actor[id]
        if actor_id_num in cast_dict:
            cast_dict[actor_id_num].append(revenue)
        else:
            cast_dict[actor_id_num]=[revenue]


# Creates producer_dict,
def add_value_to_crew(crew_data, revenue, vote_average):
    """
    Creates producer_dict, writer_dict, director_dict
    :param crew_data: row in crew column
    :param revenue: the revenue
    :return:
    """
    # for each worker in the row, crates a dict with the worker's data
    for worker in crew_data:
        worker = json.load(worker)
        if worker[DEPARTMENT] == PRODUCER:
            worker_id_num=worker[id]
            if worker_id_num in producer_dict:

                producer_dict[worker_id_num].append((revenue, vote_average))
            else:  # creates a new actor
                producer_dict[worker_id_num]=[(revenue, vote_average)]
        elif worker[DEPARTMENT] == DIRECTOR:
            worker_id_num=worker[id]
            if worker_id_num in director_dict:
                director_dict[worker_id_num].append((revenue, vote_average))
            else:
                director_dict[worker_id_num]=[(revenue, vote_average)]
        elif worker[DEPARTMENT] == WRITER:
            worker_id_num=worker[id]
            if worker_id_num in writer_dict:
                writer_dict[worker_id_num].append((revenue, vote_average))
            else:
                writer_dict[worker_id_num]=[(revenue, vote_average)]


def calculate_crew_value(crew_dict):
    """
    Calculate the average of revenue and vote_average for each crew member in the dict
    :param crew_dict: dict of crew members
    :return: the dict after replacing the list in the average value
    """
    for key in crew_dict:
        revenue_list = crew_dict[key][0]
        vote_average_list = crew_dict[key][1]

        average_of_revenue = sum(revenue_list)/len(revenue_list)
        average_of_vote = sum(vote_average_list)/len(vote_average_list)

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
                rank_of_producer.append(producer_dict[worker_id_num])  #  adds to the list of producer's rank the rank
        elif worker[DEPARTMENT] == WRITER:
            worker_id_num = worker[id]
            if worker_id_num in writer_dict:
                rank_of_writer.append(writer_dict[worker_id_num])  #  adds to the list of writer's rank the rank
        elif worker[DEPARTMENT] == DIRECTOR:
            worker_id_num = worker[id]
            if worker_id_num in director_dict:
                rank_of_director.append(director_dict[worker_id_num])  #  adds to the list of directors's rank the rank

    sum_of_producers_rank = sum(rank_of_producer)
    sum_of_director_rank = sum(rank_of_director)
    sum_of_writer_rank = sum(rank_of_writer)

    total_crew_average_rank = (sum_of_producers_rank + sum_of_director_rank + sum_of_writer_rank) / 3
    crew_data = total_crew_average_rank
    return crew_data


def process_begin(data):
    """
    Processes the data
    :param data: A dataframe
    :return:
    """
    # processed_data = copy.deepcopy (data)

    # remove columns
    pro.remove(data, TAGLINE_FEATURE)
    pro.remove(data, TITLE_FEATURE)
    pro.remove(data, KEYWORDS_FEATURE)

    # remove rows with invalid values
    data[data.runtime != 0]    # keep rows that their runtime is not 0
    data[data.runtime != ""] # keep rows that their runtime is not None
    data[data.status == RELEASED] # keep rows that their status is released
    data[data.crew != ""]  # keep rows that their crew is not None
    data[len(data.crew) == 0] # keep rows that their crew is empty

    # todo convert Json columns to dict and remove empty dict

    for line in data:
        pass



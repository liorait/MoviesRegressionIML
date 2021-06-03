import copy
import json

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

def add_value_to_crew(crew_data, revenue):
    # for each worker in the row, crates a dict with the worker's data
    for worker in crew_data:
        worker = json.load(worker)
        if worker[DEPARTMENT] == PRODUCER:
            actor_id_num=worker[id]
            if actor_id_num in producer_dict:
                producer_dict[actor_id_num].append(revenue)
            else: # creates a new actor
                producer_dict[actor_id_num]=[revenue]
        elif worker[DEPARTMENT] == DIRECTOR:
            actor_id_num=worker[id]
            if actor_id_num in director_dict:
                director_dict[actor_id_num].append(revenue)
            else:
                director_dict[actor_id_num]=[revenue]
        elif worker[DEPARTMENT] == WRITER:
            actor_id_num=worker[id]
            if actor_id_num in writer_dict:
                writer_dict[actor_id_num].append(revenue)
            else:
                writer_dict[actor_id_num]=[revenue]



def calculate_crew_value():
    for key in producer_dict:
        list= producer_dict[key]
        new_val = sum[list]/len(list)
        producer_dict[key]=new_val

def calculate_crew_value():
    for key in producer_dict:
        list= producer_dict[key]
        new_val = sum[list]/len(list)
        producer_dict[key]=new_val

def process_begin(data):
    # processed_data = copy.deepcopy (data)
    # for line in processed_data:
    pass


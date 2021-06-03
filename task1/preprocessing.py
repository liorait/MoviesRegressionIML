cast_dict={}
keyword_dict={}
crew_dict={}
DEPARTMENT="known_for_department"

PRODUCER = "Production"
DIRECTOR = "Directing"
WRITER = ""

# some change

def add_value_to_cast(cast_data, revenue):
    for actor in cast_data:
        actor_id_num=actor[id]
        if actor_id_num in cast_dict:
            cast_dict[actor_id_num].append(revenue)
        else:
            cast_dict[actor_id_num]=[revenue];

def add_value_to_crew(crew_data, revenue):
    for actor in crew_data:
        actor_id_num=actor[id]
        if actor_id_num in crew_dict:
            crew_dict[actor_id_num].append(revenue)
        else:
            crew_dict[actor_id_num]=[revenue]

def calculate_crew_value():
    for key in crew_dict:
        list= crew_dict[key]
        new_val = sum[list]/len(list)
        crew_dict[key]=new_val


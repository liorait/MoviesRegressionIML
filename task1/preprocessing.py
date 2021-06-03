cast_dict={}
keyword_dict={}
crew_dict={}

# some change

def add_value_to_cast(cast_data, box_office):
    for actor in cast_data:
        actor_id_num=actor[id]
        if actor_id_num in cast_dict:
            cast_dict[actor_id_num].append(box_office)
        else:
            cast_dict[actor_id_num]=[box_office];

def add_value_to_crew(crew_data, box_office):
    for actor in crew_data:
        actor_id_num=actor[id]
        if actor_id_num in crew_dict:
            crew_dict[actor_id_num].append(box_office)
        else:
            crew_dict[actor_id_num]=[box_office]

def calculate_crew_value():
    for key in crew_dict:
        list= crew_dict[key]
        new_val = sum[list]/len(list)
        crew_dict[key]=new_val



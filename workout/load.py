import yaml
from .workouts import workout
from .sections import section
from .routines import routine_map

def load_workout(fname):
    with open(fr'{fname}') as file:
        workout_dict = yaml.load(file, Loader=yaml.FullLoader)
        workout = strip_workout(workout_dict)
    workout.run()
    return workout

def strip_workout(workout_dict):
    name = workout_dict['name']
    section_dicts = workout_dict['sections']
    sections = []
    for section_dict in section_dicts.values():
        section = strip_section(section_dict)
        sections.append(section)
    return workout(name=name, sections=sections)

def strip_section(section_dict):
    name = section_dict['name']
    routine_name = section_dict['routine']
    routine = routine_map[routine_name]
    exercises = section_dict['exercises']
    return section(name=name, exercises=exercises, routine=routine)

# # import routines (how to execute each list of exercises)
# from workout.routines import one_min_each, abab_25

# # define the different `sections` of your workout with a list of exercises and a routine for running them
# warmup   = section(name='warmup',   exercises=warmup_exercises,   routine=one_min_each)
# hit      = section(name='HIT',      exercises=hit_exercises,      routine=abab_25)
# cooldown = section(name='cooldown', exercises=cooldown_exercises, routine=one_min_each)

# # create a workout defined by a list of sections
# hard_workout = workout(name='hard', sections=[warmup, hit, cooldown])

# # run the workout
# hard_workout.run()


    # print(name)
    # print(sections)


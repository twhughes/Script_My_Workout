import yaml
from .workouts import workout
from .sections import section
from .routines import routine_map

def load_workout(fname):
    with open(fr'{fname}') as file:
        workout_dict = yaml.load(file, Loader=yaml.FullLoader)
        workout = strip_workout(workout_dict)
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

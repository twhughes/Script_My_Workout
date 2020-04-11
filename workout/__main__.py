import sys

from .load import load_workout

""" Usage:   `python -m workout my_workout_file.yaml`  """

def get_workout():
    """ First argument is the YAML file defining the workout """
    fname = sys.argv[1]
    return load_workout(fname)

# load the workout from file
workout = get_workout()

# and run it
workout.run()


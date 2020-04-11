import sys
from .load import load_workout

def get_workout():
    fname = sys.argv[1]
    load_workout(fname)

get_workout()

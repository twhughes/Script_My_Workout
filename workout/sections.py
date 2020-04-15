from numpy.random import shuffle

from .progress import say, display

""" Workouts are made up of several 'sections', defined here.
    For example, a workout might consist of the following sections
    workout_A = {
        warmup (5 min)
        HIIT (15 min)
        abs (10 min)
        cooldown (5 min)
    }
"""

class section():

    def __init__(self, name, exercises, routine, shuffle=False):
        self.name = name
        self.exercises = exercises
        self.routine = routine
        if shuffle:
            self.shuffle()

    def shuffle(self):
        shuffle(self.exercises)

    def run(self):
        say(f'beginning {self.name} section')
        display(f'\nrunning section: {self.name}')
        self.routine(self.exercises)

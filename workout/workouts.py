from .progress import say, display, timed_rest, untimed_rest

""" A 'workout' defines a full exercise regime.
    It consists of several 'programs', each containing a set of excercises executed in a `routine`.
"""

class workout():

    def __init__(self, name, sections):
        self.name = name
        self.sections = sections

    def print_info(self):
        display(f'\nrunning workout: "{self.name}" with sections:')
        for i, section in enumerate(self.sections):
            display(f'  section {i}: {section.name}')

    def run(self):
        # say('this workout will kick your ass')
        self.print_info()
        for section in self.sections:
            untimed_rest()
            section.run()

# hard_workout = workout(name='hard', sections=[warmup, hit, cooldown], rest_time=20)
# hard_workout.run()

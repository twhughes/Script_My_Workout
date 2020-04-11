from .progress import say, display, timed_rest, untimed_rest
from .trainers import Juan, Veronica, Rishi

""" A 'workout' defines a full exercise regime.
    It consists of several 'programs', each containing a set of excercises executed in a `routine`.
"""

class workout():

    def __init__(self, name, sections, trainer=Rishi):
        self.name = name
        self.sections = sections
        self.trainer = trainer

    def print_info(self):
        display(f'\nrunning workout: "{self.name}" with sections:')
        for i, section in enumerate(self.sections):
            display(f'  section {i}: {section.name}')

    def run(self):
        # self.trainer.introduce()
        self.print_info()
        for section in self.sections:
            untimed_rest()
            # self.trainer.say_phrase()
            section.run()


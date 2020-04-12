import numpy as np
from .progress import say, say_and_display

class trainer():

    def __init__(self, voice, introduction, phrases):
        self.voice = voice
        self.phrases = phrases
        self.introduction = introduction

    def say(self, string):
        say(string, voice=self.voice)

    def say_and_display(self, string):
        say_and_display(string, voice=self.voice)

    def introduce(self):
        self.say(self.introduction)

    def say_phrase(self):
        self.say(np.random.choice(self.phrases))


Rishi = trainer(voice='Rishi',
               introduction="Im rishi and this is going to be a great workout!",
               phrases=[
                 "youre doing such a great job",
                 "keep up the incredible work"
               ])

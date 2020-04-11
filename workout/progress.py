import os
import time

""" Terminal display and audio progress markers """

BEST_VOICES = [
    'Juan',   # mexican dude with deep voice
    'Rishi',  # friendly indian man
    'Kyoko',  # japanese robot girl
    'Carmit', # israeli woman
    'Milena'  # mean russian lady
]

DEFAULT_VOICE = 'Rishi'

def say(string, voice=DEFAULT_VOICE):
    """ Have computer speak string out loud, return time """
    time_before = time.time()
    os.system(f'say -v "{voice}" {string}')
    say_time = time.time() - time_before
    return say_time

def display(string):
    """ Print string to display """
    print(string)

def say_and_display(string, voice=DEFAULT_VOICE):
    """ Both say string and display string """
    say_time = say(string, voice=voice)
    display(string)
    return say_time

def say_and_sleep(string, sec):
    """ Say `string` and sleep for total of `sec` seconds """
    t = say(string)
    if sec > t:
        sleep(sec - t)

def countdown(sec, sec_say=None):
    """ Time a `sec` second countdown, say countdown out loud with `sec_say` left """
    sec, sec_say = int(sec), int(sec_say)
    say(f'{sec} seconds')
    for sec_left in range(sec, 0, -1):
        if sec_say is not None and sec_left <= sec_say:
            t = max(say(sec_left), 0)
            time.sleep(1 - t)
        else:
            time.sleep(1)

def untimed_rest():
    """ Pause until user presses return key """
    say(f'starting rest, press enter to continue')
    input(f'\n  resting ... press Return key to start again:')

def timed_rest(rest_time):
    """ Pause for `rest_time` seconds """
    say(f'resting for')
    countdown(rest_time, sec_say=5)

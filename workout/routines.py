from .progress import say, display, say_and_display, countdown, timed_rest

""" Routines define how a section runs through a set of exercises """

def one_by_one(exercises, sec_on, sec_off):
    """ Do each exercise in list for `sec_on` seconds with `sec_off` seconds rest """
    for i, e in enumerate(exercises):
        display(f'  ({i+1}/{len(exercises)}) {e} for {sec_on} sec:')
        say(f'{e}')
        countdown(sec_on, sec_say=5)
        timed_rest(sec_off)

def abab(exercises, sec_on=20, sec_off=10):
    """ ABAB format with `sec_on` seconds on and `sec_off` seconds off between each excercise """

    for i, (a, b) in enumerate(_pairs(exercises)):
        display(f'  ({i+1}/{len(exercises)//2}): {a} and {b}')
        say(f'{a} and {b}')

        display(f'    -> (1a) {a} for {sec_on} sec: ')
        say(a)
        countdown(sec_on, sec_say=5)
        timed_rest(sec_off)

        display(f'    -> (1b) {b} for {sec_on} sec: ')
        say(b)
        countdown(sec_on, sec_say=5)
        timed_rest(sec_off)

        display(f'    -> (2a) {a} for {sec_on} sec: ')
        countdown(sec_on, sec_say=5)
        timed_rest(sec_off)

        display(f'    -> (2b) {b} for {sec_on} sec: ')
        say(b)
        countdown(sec_on, sec_say=5)
        timed_rest(sec_off)

def _pairs(exercises):
    """ Returns a list of pairs of exercises in `excercises` """
    pair_list = []
    for i in range(len(exercises)//2):
        pair_list.append((exercises[2 * i], exercises[2 * i + 1]))
    return pair_list

""" Specific examples """

def one_min_each(exercises):
    """ Do one minute of each exercise with 10 second break """
    one_by_one(exercises, sec_on=60, sec_off=10)

def abab_25(exercises):
    """ ABAB format with 25 seconds on and 5 seconds off between each excercise """
    return abab(exercises, sec_on=25, sec_off=10)

routine_map = {
    'one_min_each': one_min_each,
    'abab_25': abab_25
}

from .progress import say, display, say_and_display, countdown, timed_rest

""" Routines templates that define how a section runs through a set of exercises """

def one_by_one(exercises, sec_on, sec_off):
    """ Do each exercise in list for `sec_on` seconds with `sec_off` seconds rest """

    for i, e in enumerate(exercises):
        display(f'  ({i+1}/{len(exercises)}) for {sec_on} sec:')
        display(f'  -> {e}')
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
        say(a)
        countdown(sec_on, sec_say=5)
        timed_rest(sec_off)

        display(f'    -> (2b) {b} for {sec_on} sec: ')
        say(b)
        countdown(sec_on, sec_say=5)
        timed_rest(sec_off)

def pyramid(exercises, sec_max=60, sec_off=10):
    """ Ramps up by 10 seconds to `sec_max` with `sec_off` rest in between """

    for i, e in enumerate(exercises):
        display(f'  ({i+1}/{len(exercises)}) exercise: {e}')
        say(f'  starting pyramid round {e}')

        for t in range(10, sec_max + 10, 10):
            display(f'  -> {t} seconds')
            countdown(t, sec_say=5)

        for t in range(sec_max - 10, 0, -10):
            display(f'  -> {t} seconds')
            countdown(t, sec_say=5)

def _pairs(exercises):
    """ Returns a list of pairs of exercises in `excercises` """
    pair_list = []
    for i in range(len(exercises)//2):
        pair_list.append((exercises[2 * i], exercises[2 * i + 1]))
    return pair_list


""" Specific routines that you can use in the files and scripts """
def each_1_min(exercises):
    """ Do one minute of each exercise with 10 second break """
    one_by_one(exercises, sec_on=60, sec_off=10)

def each_50_sec(exercises):
    """ Do 50 seconds of each exercise with 10 second break """
    one_by_one(exercises, sec_on=50, sec_off=10)

def each_30_sec(exercises):
    """ Do one minute of each exercise with no break """
    one_by_one(exercises, sec_on=30, sec_off=0)

def each_20_sec(exercises):
    """ Do ten seconds of each exercise with 0 second break """
    one_by_one(exercises, sec_on=20, sec_off=5)

def abab_25(exercises):
    """ ABAB format with 25 seconds on and 10 seconds off between each excercise """
    return abab(exercises, sec_on=25, sec_off=10)

def abab_20(exercises):
    """ ABAB format with 20 seconds on and 10 seconds off between each excercise """
    return abab(exercises, sec_on=20, sec_off=10)

def pyramid_60(exercises):
    """ Ramps up and down by 10 seconds to 60 seconds with 10 sec rest in between """
    return pyramid(exercises, sec_max=60, sec_off=10)
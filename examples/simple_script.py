# import core classes for defining workout
from workout import workout, section

# import lists of exercises
from workout.exercises import warmup_exercises, hiit_exercises, cooldown_exercises

# import routines (how to execute each list of exercises)
from workout.routines import each_20_sec, abab_25

# define the different `sections` of your workout with a list of exercises and a routine for running them
warmup   = section(name='warmup',   exercises=warmup_exercises,   routine=each_20_sec)
hiit      = section(name='HIIT',     exercises=hiit_exercises,     routine=abab_25)
cooldown = section(name='cooldown', exercises=cooldown_exercises, routine=each_20_sec)

# create a workout defined by a list of sections
hard_workout = workout(name='hard', sections=[warmup, hiit, cooldown])

# run the workout
hard_workout.run()

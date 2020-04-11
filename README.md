# Script My Workout

Create your own terminal-based workouts in python!

![](img/jumping-jack-160.gif)

## How to install

No installation necessary, just clone the repo.

    git clone https://github.com/twhughes/Script_My_Workout.git
    cd Script_My_Workout

optionally, you can pip install it locally after these steps.

    pip install -e .

## How to use

There are two ways to define workouts:

### Python Script

The script `hard_workout.py` gives an example of a customized workout, copied below.

```python
# import core classes for defining workout
from workout import workout, section

# import lists of exercises
from workout.exercises import warmup_exercises, hit_exercises, cooldown_exercises

# import routines (how to execute each list of exercises)
from workout.routines import one_min_each, abab_25

# define the different `sections` of your workout with a list of exercises and a routine for running them
warmup   = section(name='warmup',   exercises=warmup_exercises,   routine=one_min_each)
hit      = section(name='HIT',      exercises=hit_exercises,      routine=abab_25)
cooldown = section(name='cooldown', exercises=cooldown_exercises, routine=one_min_each)

# create a workout defined by a list of sections
hard_workout = workout(name='hard', sections=[warmup, hit, cooldown])

# run the workout
hard_workout.run()
```

To start, simply run

    python hard_workout.py

### YAML file

You can also define a workout in a YAML file and run it.

As an example. we've defined `hard_workout.yaml`, with contents copied below.

```yaml
name: "hard workout"

sections:

  section1:
    name: "warmup"
    routine: "one_min_each"
    exercises:
      - toe touch
      - gorilla lunge

  section2:
    name: "HIT"
    routine: "abab_25"
    exercises:
      - jumping jacks
      - burpees
      - push ups

  section3:
    name: "cooldown"
    routine: "one_min_each"
    exercises:
      - hamstring stretch
      - cobra stretch
```

And one can run it with

    python -m workout hard_workout.yaml

Note that the routines here must be defined in the `routines_map` dictionary in `workout/routines.py`.

## Customizing your own workouts.

Workouts are fully customizable by editing the files in the `workout/` directory.

1.  Define lists of exercises in `workout/exercises.py`, which define the categories of exercise you want to perform.

2.  Make routines in `workout/routines.py`, which define how to run through your excercises.

3.  Group your exercises and routines into 'sections' using `workout/sections.py`.

4.  Combine sections together to form daily workouts in `workout/workouts.py`.

## Features Coming soon

- [ ] Customizable command line interface (define workout via command line arguments)
- [x] Workout definition through YAML file.
- [ ] More sophisticated definition of exercises (difficulty, categories, etc.)
- [ ] Randomization of workouts (choose amount of time and difficulty -> generate exercise list)
- [x] Progress bar display.
- [ ] ASCII art for each exercise.
- [ ] Trainers with different personalities.

I fully welcome contributions or ideas for new features or improvements!  Please leave an issue or pull request if you want to make any contributions.

## Credit

Copyright (2020) Tyler Hughes
Logo by Nadine Gilmer @nagilmer



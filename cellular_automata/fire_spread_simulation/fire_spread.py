import numpy as np
import random
import time
import os


DIM_X = 150
DIM_Y = 50

DELTA_X = 1
DELTA_T = 0.01

DIF_CONSTANT = 1

NUM_STEPS = 10000
DISPLAY_EVERY = 1
NUM_POINTS = 250

IGNITION_THRESHOLD = 0.5
IGNITION_INCREASE = 0.03

WIND_INTENSITY = random.random() + random.random() if random.randint(0, 1) == 0 else random.random()
WIND_INTENSITY = 0.5
DIRECTIONS = ['N', 'E', 'S', 'W']
WIND_DIRECTION = random.choice(DIRECTIONS)

IS_RAINING = False
RAINING_INTENSITY = random.random()
RAIN_DURATION = 0

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_object():
    object = np.zeros((DIM_Y, DIM_X))

    for _ in range(NUM_POINTS):
        x = random.randint(0, DIM_X - 1)
        y = random.randint(0, DIM_Y - 1)
        while x == 0 or x == DIM_X - 1 or y == 0 or y == DIM_Y - 1:
            x = random.randint(0, DIM_X - 1)
            y = random.randint(0, DIM_Y - 1)

        object[y][x] = 1

    return object


def visualize(object, step=0):
    display_natural_events(step)
    for y in range(DIM_Y - 1):
        for x in range(DIM_X - 1):
            if object[y][x] > 0.99:
                print("@", end="")
            elif object[y][x] > 0.90:
                print("#", end="")
            elif object[y][x] > 0.75:
                print("o", end="")
            elif object[y][x] > 0.5:
                print("*", end="")
            elif object[y][x] > 0.25:
                print(".", end="")
            elif object[y][x] > 0.1:
                print(",", end="")
            else:
                print(" ", end="")
        print()


def all_neighbors_burning(tablet, x, y):
    return tablet[y][x-1] > IGNITION_THRESHOLD and \
           tablet[y][x+1] > IGNITION_THRESHOLD and \
           tablet[y-1][x] > IGNITION_THRESHOLD and \
           tablet[y+1][x] > IGNITION_THRESHOLD

def all_neigbors_fairly_burning(tablet, x, y):
    return tablet[y][x-1] > IGNITION_THRESHOLD * 0.5 and \
           tablet[y][x+1] > IGNITION_THRESHOLD * 0.5 and \
           tablet[y-1][x] > IGNITION_THRESHOLD * 0.5 and \
           tablet[y+1][x] > IGNITION_THRESHOLD * 0.5

def display_natural_events(step):
    compass = {
        'S': '^',
        'W': '>',
        'N': 'v',
        'E': '<',
    }

    rain = {
        True: 'v',
        False: '',
    }

    print(f"Wind direction {compass[WIND_DIRECTION] * int(WIND_INTENSITY * 10)} | Rain: {rain[IS_RAINING] * int(RAINING_INTENSITY * 10)}, Duration: {RAIN_DURATION - step + 1 if IS_RAINING else 0}")

def no_fire(tablet):
    return np.sum(tablet) == 0

def ignite_random(tablet):
    x = random.randint(0, DIM_X - 1)
    y = random.randint(0, DIM_Y - 1)
    while x == 0 or x == DIM_X - 1 or y == 0 or y == DIM_Y - 1:
        x = random.randint(0, DIM_X - 1)
        y = random.randint(0, DIM_Y - 1)

    tablet[y][x] = 1
    return tablet

def evolve(tablet):
    global WIND_DIRECTION, WIND_INTENSITY, IS_RAINING, RAINING_INTENSITY, RAIN_DURATION
    new_tablet = np.copy(tablet)

    for step in range(NUM_STEPS):
        for y in range(1, DIM_Y - 1):
            for x in range(1, DIM_X - 1):
                if x == 0 or x == DIM_X - 1 or y == 0 or y == DIM_Y - 1:
                    new_tablet[y][x] = 0
                else:
                    new_tablet[y][x] = tablet[y][x] + DIF_CONSTANT * DELTA_T / DELTA_X**2 * \
                                    (tablet[y][x-1] + tablet[y][x+1] + tablet[y-1][x] + tablet[y+1][x] - 4 * tablet[y][x])
        # Ignition mechanism
        for y in range(1, DIM_Y - 1):
            for x in range(1, DIM_X - 1):
                if IS_RAINING:
                    change =  RAINING_INTENSITY + random.random() * 0.1
                    tablet[y][x] = max(tablet[y][x] - change, 0)

                if tablet[y][x] > IGNITION_THRESHOLD and all_neigbors_fairly_burning(tablet, x, y):
                    tablet[y][x] = max(tablet[y][x] - 0.5, 0)

                if random.randint(0, 10) < 3 and tablet[y][x] > 0:
                    tablet[y][x] = 0

                if tablet[y][x] > IGNITION_THRESHOLD and not all_neighbors_burning(tablet, x, y):
                    north_ignite = IGNITION_INCREASE
                    east_ignite = IGNITION_INCREASE
                    south_ignite = IGNITION_INCREASE
                    west_ignite = IGNITION_INCREASE

                    if WIND_DIRECTION == 'N':
                        south_ignite += IGNITION_INCREASE * WIND_INTENSITY
                        north_ignite -= IGNITION_INCREASE * WIND_INTENSITY

                    elif WIND_DIRECTION == 'E':
                        west_ignite += IGNITION_INCREASE * WIND_INTENSITY
                        east_ignite -= IGNITION_INCREASE * WIND_INTENSITY

                    elif WIND_DIRECTION == 'S':
                        north_ignite += IGNITION_INCREASE * WIND_INTENSITY
                        south_ignite -= IGNITION_INCREASE * WIND_INTENSITY

                    elif WIND_DIRECTION == 'W':
                        east_ignite += IGNITION_INCREASE * WIND_INTENSITY
                        west_ignite -= IGNITION_INCREASE * WIND_INTENSITY

                    if random.random() < random.random() and y > 0:
                        new_tablet[y-1][x] = min(new_tablet[y-1][x] + north_ignite, 1)

                    if random.random() < random.random() and y < DIM_Y - 1:
                        new_tablet[y+1][x] = min(new_tablet[y+1][x] + south_ignite, 1)

                    if random.random() < random.random() and x > 0:
                        new_tablet[y][x-1] = min(new_tablet[y][x-1] + west_ignite, 1)

                    if random.random() < random.random() and x < DIM_X - 1:
                        new_tablet[y][x+1] = min(new_tablet[y][x+1] + east_ignite, 1)
                elif all_neighbors_burning(tablet, x, y):
                    new_tablet[y][x] = 0


        tablet, new_tablet = new_tablet, tablet

        if step % DISPLAY_EVERY == 0:
            clear_console()
            visualize(tablet, step)

            if step % 100 == 0:
                WIND_DIRECTION = random.choice(DIRECTIONS)
                WIND_INTENSITY = random.random() + random.random() if random.randint(0, 1) == 0 else random.random()

            if random.randint(0, 1) == 0 and not IS_RAINING and step % 100 == 0:
                IS_RAINING = True
                RAINING_INTENSITY = random.random()
                if RAINING_INTENSITY <= 0:
                    RAINING_INTENSITY = 0.1
                elif step < 1000:
                    RAINING_INTENSITY = 0.1
                RAIN_DURATION = random.randint(step, step + 300)

            if IS_RAINING and step > RAIN_DURATION:
                IS_RAINING = False
                RAINING_INTENSITY = 0
                RAIN_DURATION = 0

            if no_fire(tablet):
                tablet = ignite_random(tablet)

    return tablet

def main():
    clear_console()
    tablet = initialize_object()
    tablet = evolve(tablet)

if __name__ == "__main__":
    main()


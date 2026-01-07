# Log File:
# /Users/[your name]/Library/Preferences/Ableton/Live 11.2.6
import random
import numpy as np
import matplotlib.pyplot as plt
from math import pi

p = {'name': ['kick', 'snare', 'hi-hat'],
     'points': [16, 5, 8],
     'start': [0, 3, 5],
     'size': 32,
     'length': 4}

def polygon(names, points, starts, size):
    d = {}
    for name, num_points, start, in zip(names, points, starts):
        if num_points == size:
            d[name] = list(range(size))
        else:
            d[name] = sorted([start] + random.sample(range(start+1, size), num_points-1))
    return d


def visualise(name, points, start, size):
    # Create the Circle, through the use of a subplot
    ax = plt.subplot(111, polar=True)
    # Create linear spaced points (floats) for the X axis
    ax.set_xticks(np.linspace(0, 2 * pi, size, endpoint=False))
    # Replace the calculated points with integers
    ax.set_xticklabels(range(size))
    # List comprehension: Get the string values from the newly created labels
    labels = [item.get_text() for item in ax.get_xticklabels()]
    # Map these values to our instrument names, and set them
    labels[start[0]], labels[start[1]], labels[start[2]] = 'kick', 'snare', 'hi-hat'
    ax.set_xticklabels(labels)
    # Some padding
    ax.tick_params(axis='x', which='major', pad=15)
    # Reverse the direction of the X labels
    ax.set_theta_direction(-1)
    # Rotate the Plot -90 degrees
    ax.set_theta_offset(pi / 2)
    # Remove the Y labels
    plt.yticks([])
    plt.show()






d = polygon(p['name'], p['points'], p['start'], p['size'])
visualise(p['name'], d, p['start'], p['size'])

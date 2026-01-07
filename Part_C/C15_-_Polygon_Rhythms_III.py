# Log File:
# /Users/[your name]/Library/Preferences/Ableton/Live 11.2.6
import random
import numpy as np
import matplotlib.pyplot as plt
from math import pi

p = {'name': ['kick', 'snare', 'hi-hat'],
     'points': [5, 5, 8],
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
    ax = plt.subplot(111, polar=True)
    total_points = np.linspace(0, 2 * pi, size, endpoint=False)
    ax.set_xticks(total_points)
    ax.set_xticklabels(range(size))
    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[start[0]], labels[start[1]], labels[start[2]] = 'kick', 'snare', 'hi-hat'
    ax.set_xticklabels(labels)
    ax.tick_params(axis='x', which='major', pad=15)
    ax.set_theta_direction(-1)
    ax.set_theta_offset(pi / 2)
    plt.yticks([])
    # Create a list with the positions for X, based on the points per instruments
    x = []
    for i in range(len(points)):
        x.append(total_points[points[name[i]]])
    print(x)
    # Create a list of 0's based on the length of the X array'
    y = [1, ] * len(x[0])
    # Append the starting points
    for i in range(len(name)):
        try:
            x[0] = np.append(x[0], x[0][0])
            y[0] = np.full(len(x[0]), 1)
            x[1] = np.append(x[1], x[1][0])
            y[1] = np.full(len(x[1]), 1)
            x[2] = np.append(x[2], x[2][0])
            y[2] = np.full(len(x[2]), 1)
        except IndexError:
            print("There's an Index Error")
            break
    # Draw the lines between the points
    for i in range(len(name)):
        ax.plot(x[i], y[i], linewidth=1, linestyle='solid', label=name[i])
    plt.ylim(0, 1)
    plt.legend(loc=(0.99, 0.95))
    plt.show()

d = polygon(p['name'], p['points'], p['start'], p['size'])
visualise(p['name'], d, p['start'], p['size'])

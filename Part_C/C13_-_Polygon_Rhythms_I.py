# Log File:
# /Users/[your name]/Library/Preferences/Ableton/Live 11.2.6
import random


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

d = polygon(p['name'], p['points'], p['start'], p['size'])

print(d)

print(sorted([2, 7, 4, 9, 1, 5, 3]))
print(random.sample([1, 2, 3, 4, 5, 6, 7], 3))

print(list(range(32)))
animals = ['Bear', 'Python', 'Mouse']
count = [14, 3, 6]

result = zip(animals, count)
print(result)
print(list(result))
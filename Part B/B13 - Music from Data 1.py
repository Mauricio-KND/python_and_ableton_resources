# Dataset Documentation
# https://www.kaggle.com/datasets/markmarkoh/near-earth-asteroids

# Velocity Infinity          -> Pitch               -> Higher Speed         -> High Pitch
# Minimum Distance           -> Note Length         -> Further Distance     -> Longer Note
# ref                        -> Velocity            -> Higher Ref           -> Higher Velocity

import pandas as pd
import matplotlib.pyplot as plt

def read_and_plot(file, r1, r2, r3):
    d = pd.read_csv(file)
    print(f"Number of Rows: {len(d)}")
    print(d.head())
    pitch = d[r1].values
    length = d[r2].values
    velocity = d[r3].values
    plt.scatter(pitch, length, s=pitch, c=velocity)
    plt.xlabel(r1)
    plt.ylabel(r2)
    plt.show()

read_and_plot('./00data/near_earth.csv', 'Vinfinity(km/s)', 'CA DistanceMinimum(LD/AU)', 'ref')




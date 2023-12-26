"""
There are a few common methods to automatically choose prototype points (cluster centers) in k-means clustering:
1) Random initialization: Select k random points from the dataset as the initial prototypes. Simple but can lead to poor clusters if the random points are poor.
2) K-means++ initialization: Selects initial prototype points with specific probabilities that spreads them across the dataset. More likely to find global optimum.
3) Canopy clustering: Quickly partitions data into overlapping subsets from which initial prototypes are picked.
4) Farthest-first traversal algorithm: Iteratively select prototype that has the farthest distance from the existing prototypes. Aims to spread out points.

Additionally, once initial prototypes are chosen, k-means refinement iterates between these steps:
1) Assign each data point to the nearest prototype
2) Set each prototype to the mean of all points assigned to it.

This adjustable nature allows prototypes to naturally shift toward optimal cluster centers.

In general, k-means++ with refinement through centroid updating tends to work very well for automatically finding good prototypes.
"""

import random
from math import sqrt

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate 33 coordinates from 3 different ranges (99 total)
ranges = [
    # [(min_x, max_x), (min_y, max_y)]
    [(0, 10), (2, 4)],
    [(8, 10), (8, 10)],
    [(5, 7), (5, 7)]
]

coords = []
for group_idx, r in enumerate(ranges):
    x_range, y_range = r

    coords_in_range = set()
    while len(coords_in_range) < 33:
        x = random.uniform(*x_range)
        y = random.uniform(*y_range)
        coords_in_range.add((x, y, group_idx))

    coords.extend(coords_in_range)

# Convert coordinates to DataFrame
df = pd.DataFrame(coords, columns=['x', 'y', 'real_group'])

# Plot scatterplot (pl. wykres punktowy) with real groupes
ax = sns.scatterplot(data=df, x='x', y='y', hue='real_group', palette='deep')

plt.show()

# Predict groups using k-means clustering
def average_coordinate(l: list) -> tuple:
    x_sum = 0
    x_count = 0
    y_sum = 0
    y_count = 0

    for x, y in l:
        x_sum += x
        y_sum += y

        x_count += 1
        y_count += 1

    return (x_sum / x_count, y_sum / y_count)


prototype1 = coords[0][0:2]
prototype2 = coords[33][0:2]
prototype3 = coords[66][0:2]

predicted_groups = []
predicted_group1 = []
predicted_group2 = []
predicted_group3 = []
initial_prototypes = [prototype1, prototype2, prototype3]
for x, y, _ in coords:
    differences = [
        sqrt((x-prototype1[0])**2 + (y-prototype1[1])**2),
        sqrt((x-prototype2[0])**2 + (y-prototype2[1])**2),
        sqrt((x-prototype3[0])**2 + (y-prototype3[1])**2)
    ]

    if min(differences) == differences[0]:
        predicted_group1.append((x, y))
        predicted_groups.append(0)
        prototype1 = average_coordinate(predicted_group1)
    elif min(differences) == differences[1]:
        predicted_group2.append((x, y))
        predicted_groups.append(1)
        prototype2 = average_coordinate(predicted_group2)
    else:
        predicted_group3.append((x, y))
        predicted_groups.append(2)
        prototype3 = average_coordinate(predicted_group3)

# Add a new column to the DataFrame
df['predicted_group'] = predicted_groups

# Plot scatterplot with predicted groups
ax = sns.scatterplot(data=df, x='x', y='y', hue='predicted_group', palette='deep')

# Highlight initial prototypes
for idx, coord in enumerate(initial_prototypes):
    x, y = coord
    ax.text(x+0.01, y, f'prototype{idx}', horizontalalignment='left', size='medium', color='black')

plt.show()

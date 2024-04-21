from scipy.stats import skewnorm
import numpy as np
import pandas as pd
from random import random, uniform
from math import sqrt, pow

def generate_skewed_distribution():
    skewness_param = 5
    skewed_data = skewnorm.rvs(skewness_param, size=333333)
    return skewed_data

def generate_random_point(center_x, center_y, cluster):
    points = []
    distances = generate_skewed_distribution()

    for distance in distances:
        while True:
            angle = random() * np.pi * 2
            x = center_x + np.cos(angle) * distance
            y = center_y + np.sin(angle) * distance
            if [x, y, cluster] not in points:
                break
        points.append([x, y, cluster])
    return points

if __name__ == '__main__':
    cluster_centers = [[10, 25], [2, -9], [-15, -35]]  # Pre-defined three centers for clusters
    dataset = []
    
    for center in cluster_centers:
        dataset += generate_random_point(center[0], center[1], cluster_centers.index(center))

    df = pd.DataFrame(dataset)
    df.drop(df.columns[[2]], axis=1, inplace=True)
    df.to_csv("dataset.txt", header=False, index=False, sep="," )
    
    # Save cluster centers to a text file
    with open("centroids.txt", "w") as file:
        for center in cluster_centers:
            file.write(f"{center[0]}, {center[1]}\n")



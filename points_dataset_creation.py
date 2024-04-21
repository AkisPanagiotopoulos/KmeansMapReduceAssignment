from scipy.stats import skewnorm
import numpy as np
import pandas as pd
from random import random, uniform
from math import cos, sin, pi

def generate_skewed_distribution(size):
    skewness_param = 5
    skewed_data = skewnorm.rvs(skewness_param, size=size)
    return skewed_data

def generate_random_point(center_x, center_y, cluster, distances):
    points = []
    
    for distance in distances:
        angle = random() * pi * 2
        x = center_x + cos(angle) * distance
        y = center_y + sin(angle) * distance
        points.append([x, y, cluster])
    
    return points

if __name__ == '__main__':
    cluster_centers = [[10, 25], [2, -9], [-15, -35]]  # Pre-defined three centers for clusters
    
    # Generate skewed distances once
    distances = generate_skewed_distribution(333333)
    
    dataset = []
    for center in cluster_centers:
        dataset += generate_random_point(center[0], center[1], cluster_centers.index(center), distances)
    
    df = pd.DataFrame(dataset)
    df.drop(df.columns[[2]], axis=1, inplace=True)
    df.to_csv("dataset.txt", header=False, index=False, sep="," )
    
    # Save cluster centers to a text file
    with open("centroids.txt", "w") as file:
        for center in cluster_centers:
            file.write(f"{center[0]}, {center[1]}\n")

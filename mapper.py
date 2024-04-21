#!/usr/bin/env python
"""mapper.py for KMeans algorithm"""

import sys
import math

def read_centroids(filepath):
    centroids = []
    try:
        with open(filepath) as fp:
            for line in fp:
                line = line.strip()
                if line:
                    try:
                        x, y = map(float, line.split(','))
                        centroids.append((x, y))
                    except ValueError:
                        # Skip lines that cannot be parsed
                        continue
    except FileNotFoundError:
        print(f"Error: Centroids file '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)
    return centroids

def assign_to_nearest_cluster(data_point, centroids):
    x, y = map(float, data_point.split(','))
    min_dist = float('inf')
    nearest_centroid = None
    for centroid in centroids:
        dist = math.sqrt((x - centroid[0])**2 + (y - centroid[1])**2)
        if dist < min_dist:
            min_dist = dist
            nearest_centroid = centroid
    return f"{centroids.index(nearest_centroid)}\t{x}\t{y}"

if __name__ == "__main__":
    centroids = read_centroids('centroids.txt')
    for line in sys.stdin:
        line = line.strip()
        if line:
            print(assign_to_nearest_cluster(line, centroids))


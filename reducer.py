#!/usr/bin/env python
"""reducer.py for KMeans algorithm"""

import sys

def update_centroids():
    current_cluster = None
    sum_x = 0
    sum_y = 0
    count = 0

    for line in sys.stdin:
        cluster_index, x, y = line.split('\t')

        try:
            x = float(x)
            y = float(y)
        except ValueError:
            # Skip lines that cannot be parsed
            continue

        if current_cluster == cluster_index:
            count += 1
            sum_x += x
            sum_y += y
        else:
            if count != 0:
                # Calculate and print the new centroids for each cluster
                print(f"{sum_x / count}, {sum_y / count}")

            current_cluster = cluster_index
            sum_x = x
            sum_y = y
            count = 1

    # Print the centroids for the last cluster
    if current_cluster == cluster_index and count != 0:
        print(f"{sum_x / count}, {sum_y / count}")

if __name__ == "__main__":
    update_centroids()


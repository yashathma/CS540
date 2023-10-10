import csv
import math
import numpy as np

import scipy.spatial
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt

def load_data(filepath):
    #Creating set
    dataset = []
    with open(filepath, "r") as inputfile:
        reader = csv.DictReader(inputfile)
        #Setting Vals
        for eachRow in reader:
            val = dict(eachRow)
            dataset.append(val)
    return dataset

def calc_features(row):
    #Setting Column Names
    columns = [float(row["Population"]), 
                         float(row["Net migration"]), 
                         float(row["GDP ($ per capita)"]), 
                         float(row["Literacy (%)"]), 
                         float(row["Phones (per 1000)"]), 
                         float(row["Infant mortality (per 1000 births)"])]
    
    #Setting Values
    features = np.array(columns, 
                        dtype = np.float64)
    return features

def hac(features):
    # Set print options to suppress scientific notation
    np.set_printoptions(suppress=True)
    
    # Compute the distance matrix for the input features
    dist_matrix = scipy.spatial.distance_matrix(features, features, p=2)
    
    # Initialize a list to store cluster information
    cluster_list = [[i, 0] for i in range(0,len(features))]
    
    # Initialize a matrix to store the clustering results
    result_matrix = np.zeros((len(features) - 1, 4))

    # Iterate through the clustering process
    for row_idx in range(len(result_matrix)):
        min_distance = float("inf")
        min_indices = [float("inf"), float("inf")]
        cluster_indices = [0, 0]

        # Find the minimum distance between clusters
        for i in range(len(cluster_list)):
            for j in range(i + 1, len(cluster_list)):
                computed_distance = 0

                # Calculate the distance between elements in two clusters
                for num1 in cluster_list[i][0:-1]:
                    for num2 in cluster_list[j][0:-1]:
                        if dist_matrix[num1][num2] > computed_distance:
                            computed_distance = dist_matrix[num1][num2]

                # Update the minimum distance and cluster indices
                if computed_distance < min_distance:
                    min_distance = computed_distance
                    min_indices = [cluster_list[i][0], cluster_list[j][0]]
                    cluster_indices = [i, j]
                elif computed_distance == min_distance:
                    if cluster_list[i][0] < min_indices[0]:
                        min_distance = computed_distance
                        min_indices = [cluster_list[i][0], cluster_list[j][0]]
                        cluster_indices = [i, j]

        # Store clustering results in the result_matrix
        result_matrix[row_idx, 2] = min_distance
        result_matrix[row_idx, 3] = len(cluster_list[cluster_indices[0]]) + len(cluster_list[cluster_indices[1]]) - 2

        # Update cluster indices for merging clusters
        if len(cluster_list[cluster_indices[0]]) > 2:
            min_indices[0] = len(features) + cluster_list[cluster_indices[0]][-1]

        if len(cluster_list[cluster_indices[1]]) > 2:
            min_indices[1] = len(features) + cluster_list[cluster_indices[1]][-1]

        if min_indices[1] < min_indices[0]:
            min_indices[1], min_indices[0] = min_indices[0], min_indices[1]

        result_matrix[row_idx, 0] = min_indices[0]
        result_matrix[row_idx, 1] = min_indices[1]

        # Merge clusters and update cluster list
        for num in cluster_list[cluster_indices[1]][0:-1]:
            cluster_list[cluster_indices[0]].insert(-1, num)

        cluster_list[cluster_indices[0]][-1] = row_idx
        del cluster_list[cluster_indices[1]]

    # Return the final clustering result
    return result_matrix

def fig_hac(Z,names):
    #Creating A matplotlib figure
    matPlotGraph = plt.figure()

    #Applying Values
    dendrogram(Z, labels=names, leaf_rotation=90)
    matPlotGraph.tight_layout()
    return matPlotGraph

def normalize_features(features):
    copy = []
    for i in features:
        copy.append(i.copy())
    for i in range(0,6):
        m = 0
        sd = 0

        #Calculating Mean
        for f in features:
            m+=f[i]
        m = m/len(features)

        #Calculating Standard Deviation
        for f in features:
            sd+=pow((f[i]-m),2)
        sd = sd/ len(features)
        sd = math.sqrt(sd)

        #Normalizing with mean and Standard Deviation
        for f in copy:
            f[i] = (f[i] -m)/sd
    return copy


# if __name__=="__main__":
#     data = load_data("/Users/yash/Desktop/School/VSCode/hw4/countries.csv")
                     
#     country_names = [row["Country"] for row in data]
#     features = [calc_features(row) for row in data]
#     features_normalized = normalize_features(features)
#     n = 10
#     Z_raw = hac(features[:n])
#     Z_normalized = hac(features_normalized[:n])
#     fig = fig_hac(Z_raw, country_names[:n])
#     plt.show()
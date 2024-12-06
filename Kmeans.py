import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch as T
import torch.nn as nn

class Kmeans(nn.Module):
    def initialisation(self, df):
        for i in range(len(df)):
            df[i] = df[i]/(np.max(df[i])-np.min(df[i]))
        df = T.tensor(df)
        return df
            
    def forward(self, df):
        model = nn.Sequential(
            nn.Linear(df.shape[1], 1024),
            nn.ReLU(),
            nn.Linear(1024,512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Linear(128,64),
            nn.ReLU()
        )
    
        newp = []
        for i in np.arange(df.shape[0]):
            newp.append(np.array(model(df[i]).tolist()))
    
        return newp

    def kmeans(self, df, cent):
        centroids = np.array(cent)
        k = len(centroids)  
        clusters = [[] for _ in range(k)]
        
        for point in df:
            distances = [np.linalg.norm(point - centroid) for centroid in cent]
            closest_centroid = np.argmin(distances)
            clusters[closest_centroid].append(point)
        
        new_centroids = []
        for cluster_points in clusters:
            if cluster_points:
                new_centroids.append(np.mean(cluster_points, axis=0))
            else:
                new_centroids.append(centroids[len(new_centroids)])
        
        return new_centroids, clusters

    def initial_cent(self, tick):
        return np.random.randint(0,len(tick), 2)
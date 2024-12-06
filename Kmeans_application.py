import numpy as np
import matplotlib.pyplot as plt
from Kmeans import Kmeans
import DataImport as di
import torch as T

ticker_selection = Kmeans()
price_data = di.adj_close_price
normalised_data = ticker_selection.initialisation(price_data)
input = ticker_selection.forward(normalised_data)
initial_centroids = ticker_selection.initial_cent(input, di.tickers)
initial_centroids, input

centroids = initial_centroids
while True:
    new_centroids, clusters = ticker_selection.kmeans(input, centroids)
    #print(new_centroids)
    if np.allclose(new_centroids, centroids):
        break
    centroids = new_centroids

pair_1 = [] 
pair_2 = []
for i in range(len(input)):
    if np.max(abs(input[i] - clusters[0][0])) < 1e-15:
        pair_1.append(di.tickers[i])
    if np.max(abs(input[i] - clusters[0][1])) < 1e-15:
        pair_1.append(di.tickers[i])

for i in range(len(input)):
    if np.max(abs(input[i] - clusters[1][0])) < 1e-15:
        pair_2.append(di.tickers[i])
    if np.max(abs(input[i] - clusters[1][1])) < 1e-15:
        pair_2.append(di.tickers[i])

pair_1, pair_2
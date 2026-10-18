# -*- coding: utf-8 -*-
from sklearn.cluster import k_means
import numpy as np
import scipy.ndimage as ndi
import skimage.io as io
import skimage.metrics as met
import matplotlib.pyplot as plt
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")

"import immagine"
file = str(path_immagini/"rice.y")
x = np.fromfile(file, np.uint8)
x = x.reshape(256,256)
x = np.float64(x)

plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')


"applico il k-means ed eseguo threshold globale"
(M,N) = x.shape
K = 2

x_flat = np.reshape(x, (M*N, 1))
centroid, idx, sum_var = k_means(x_flat, K)
y = np.reshape(idx, (M,N))

t = np.sum(centroid)/2
mask = x > t
plt.figure('maschera globale'); plt.imshow(mask, clim=[0,1], cmap='gray')


"eseguo thresholding adattivo"
"funzione che calcola la semisomma dei due centroidi data una matrice"
def find_ott(x):
    (M,N) = x.shape
    K = 2
    
    x_flat = x.reshape((M*N, 1))
    centroid, index, sum_var = k_means(x_flat, K)
    
    return (centroid[0] + centroid[1])/2
    
    
lista_ottimi = []
lista_sottomatrici = []
lista_cluster = []

"ad ogni iterazioni creo i gruppi di righe e trovo le rispettive soglie"
for i in range(8):
    
    List = x[(2**i)-1:(2**(i+1))-1,:]
    
    lista_sottomatrici.append(List)
    
    lista_ottimi.append(find_ott(List))
    
    
"per ogni gruppo di righe eseguo il treshold"
for i,j in zip(lista_sottomatrici, lista_ottimi):
    lista_cluster.append(i > j)

"faccio lo stack dei cluster locali"
cluster_loc = np.vstack(lista_cluster)

plt.figure('maschera locale'); plt.imshow(cluster_loc, clim=[0,1], cmap='gray')

























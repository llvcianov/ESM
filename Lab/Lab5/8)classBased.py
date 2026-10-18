# -*- coding: utf-8 -*-


from sklearn.cluster import k_means
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")


# """Immagini in scala di grigio"""
# x = np.float64(io.imread(path_immagini/"granelli_riso.tif"))
# plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')
# (M,N) = x.shape

# #non lavoriamo su matrice, elabora ogni pixel separatamente.
# #quindi vuole come input un vettore
# K = 2
# d = np.reshape(x, (M*N, 1)) #oppure al posto di -1 scriviamo M*N
# centroid, idx, sum_var = k_means(d, K)
# #ora riportiamo la dimensione in matrice
# y = np.reshape(idx, x.shape)

# plt.figure(2); plt.imshow(y, clim=None, cmap='jet')

"""Immagini a colori"""

x = np.float64(io.imread(path_immagini/"elefante.jpg"))/255
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

(M,N,L) = x.shape
K = 5

"devo trasformare l'immagine in un vettore, ogni elemento ha 3 valori"
"e cioè i valori r,g,b. per tale motivo faccio L colonne"
d = np.reshape(x, (M*N, L))

centroid, idx, sum_var = k_means(d, K)

"l'output non è più in RGB, devo semplicemnete trasformare in"
"immagine in scala di grigi"
y = np.reshape(idx, (M,N))
plt.figure(2); plt.imshow(y, clim=None, cmap='jet')















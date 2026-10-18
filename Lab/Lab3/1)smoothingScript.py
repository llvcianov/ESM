# -*- coding: utf-8 -*-
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.exposure import equalize_hist
from skimage.transform import warp
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

x = np.float64(io.imread(path_immagini/"lena.jpg"))
plt.subplot(1,3,1); plt.imshow(x, clim = None, cmap = 'gray')

"""Smoothing con correlate devo creare la maschera manualmente"""
# k = 9
# h = np.ones((k,k))/(k**2)  #creo maschero con tutti 1/9
# y = ndi.correlate(x, h, mode='reflect')
# my.vediIstogrammaStretchato(y, 256)

"""Smoothing con uniform e gaussian la maschera è preimpostata"""
# z = ndi.uniform_filter(x, (9,9), mode = 'reflect')
# plt.subplot(1,3,2); plt.imshow(z, clim = None, cmap = 'gray')

g1 = ndi.gaussian_filter(x, sigma = 1.5)
plt.subplot(1,3,2); plt.imshow(g1, clim = None, cmap = 'gray')

"""Smoothing gaussian usando correlate"""
h = np.array([[1,2,1],[2,4,2],[1,2,1]])/16
# h = np.array([
#     [1,   1,   2,   2,   2,   2,   2,   1,   1],
#     [1,   2,   2,   4,   4,   4,   2,   2,   1],
#     [2,   2,   4,   8,   8,   8,   4,   2,   2],
#     [2,   4,   8,  16,  16,  16,   8,   4,   2],
#     [2,   4,   8,  16,  32,  16,   8,   4,   2],
#     [2,   4,   8,  16,  16,  16,   8,   4,   2],
#     [2,   2,   4,   8,   8,   8,   4,   2,   2],
#     [1,   2,   2,   4,   4,   4,   2,   2,   1],
#     [1,   1,   2,   2,   2,   2,   2,   1,   1]
# ], dtype=np.float64)

# # Normalizzazione: Somma di tutti i coefficienti
# h /= np.sum(h)

g2 = ndi.correlate(x, h)
plt.subplot(1,3,3); plt.imshow(g2, clim = None, cmap = 'gray')








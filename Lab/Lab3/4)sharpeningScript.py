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

x = np.float64(io.imread(path_immagini/"luna.jpg"))
plt.subplot(1,4,1); plt.imshow(x, clim = None, cmap = 'gray')

"""filtri laplaciani
   N.B. filtri uguali ma i bordi vengono evidenziati con colori opposti"""
   
h1 = np.array([[0, 1,0],
               [1,-4,1],
               [0, 1,0]])

h2 = np.array([[ 0,-1, 0],
               [-1, 4,-1],
               [ 0,-1, 0]])

y1 = ndi.correlate(x, h1, mode = 'reflect')
plt.subplot(1,4,2); plt.imshow(y1, clim = None, cmap = 'gray')

y2 = ndi.correlate(x, h2, mode = 'reflect')
plt.subplot(1,4,3); plt.imshow(y2, clim = None, cmap = 'gray')

"""filtro che somma il laplaciano all'immagine originale"""

h3 = np.array([[ 0,-1, 0],
               [-1, 5,-1],
               [ 0,-1, 0]])

y3 = ndi.correlate(x, h3, mode = 'reflect')
plt.subplot(1,4,4); plt.imshow(y3, clim = None, cmap = 'gray')










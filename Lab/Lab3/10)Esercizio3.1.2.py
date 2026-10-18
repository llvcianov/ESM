# -*- coding: utf-8 -*-
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.util import random_noise
from skimage.exposure import equalize_hist
from skimage.transform import warp
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab")

x = np.float64(io.imread(path_immagini/"luna.jpg"))
plt.subplot(1,3,1); plt.imshow(x, clim = None, cmap = 'gray')

""" filtro laplaciano usando la differenza centrale """
h = np.array([[0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [1, 0,-4, 0, 1],
              [0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0]])

""" filtro laplaciano usando la differenza normale """ 
h1 = np.array([[0, 1, 0],
               [1,-4, 1],
               [0, 1, 0]])

y = ndi.convolve(x, h, mode = 'reflect')
plt.subplot(1,3,2); plt.imshow(y, clim = None, cmap = 'gray')

y1 = ndi.correlate(x, h1, mode = 'reflect')
plt.subplot(1,3,3); plt.imshow(y1, clim = None, cmap = 'gray')

# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.exposure import equalize_hist
from skimage.transform import warp
from pathlib import Path
from seg_utils import zero_crossing
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab")


"""Filtraggio mediante derivata seconda (tecniche Laplaciano)"""

x = np.float64(io.imread(path_immagini/"angiogramma.jpg"))
plt.subplot(1,2,1); plt.imshow(x, clim = None, cmap = 'gray')

sigma = 5
y = ndi.gaussian_laplace(x, (sigma,sigma))

""" dopo aver filtrato con laplaciano di una gaussiana applico la
    funzione zero crossing"""
    
z = zero_crossing(y)
plt.subplot(1,2,2); plt.imshow(z, clim = None, cmap = 'gray')















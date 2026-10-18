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

"""Filtraggio mediante filtri non lineari: filtro mediano"""

x = np.float64(io.imread(path_immagini/"circuito_rumoroso.jpg"))
plt.subplot(1,2,1); plt.imshow(x, clim = None, cmap = 'gray')

y = ndi.median_filter(x, (5,5), mode = 'reflect')
plt.subplot(1,2,2); plt.imshow(y, clim = None, cmap = 'gray')
# -*- coding: utf-8 -*-

from sklearn.cluster import k_means
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

x = np.float64(io.imread(path_immagini/"yeast.tif"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

""" calcolo deiazione standard locale"""
y = ndi.generic_filter(x, np.std, (3,3))

""" calcolo media globale"""
mg = np.mean(x)

""" parametri"""
a = 30
b = 1.5

"""calcolo mappa binaria"""
g = (x > a * y) & (x > b * mg)
plt.figure('mappa'); plt.imshow(g, clim=None, cmap='gray')
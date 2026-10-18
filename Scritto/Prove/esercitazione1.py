# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import skimage.exposure as exp
import scipy.ndimage as ndi
from skimage.color import rgb2hsv, hsv2rgb
from seg_utils import zero_crossing
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\esercitazione_250411\esercitazione_250411")
plt.close('all')
    
x = np.float64(io.imread(path_immagini/"ponte.gif"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

#equalizzo per visualizzare bene
y = exp.equalize_hist(x, nbins=256)
# y = y * 255
plt.figure('equalizzato'); plt.imshow(y, clim=None, cmap='gray')
#plt.figure(2); plt.hist(y.flatten(), bins=256); plt.xlim((0,255))

# #calcolo varianze per scoprire i difetti
# varianze = (ndi.generic_filter(y, np.var, (2,2), mode='reflect')/255)
# plt.figure('varianze locali'); plt.imshow(varianze, clim=None, cmap='gray')

# #la maschera è dove la varianza è alta
# maschera = (varianze > 26)
# maschera = ~maschera
# plt.figure('maschera binaria'); plt.imshow(maschera, clim=None, cmap='gray')

# #unisco maschera e immagine e filtro con mediano
# y_mask = y * maschera
# z = ndi.generic_filter(y_mask, np.median, (7,7), mode='reflect')
# plt.figure('mediano su equalizzata'); plt.imshow(z, clim=None, cmap='gray')

# #uso immagine filtrata con mediano solo sulla maschera
# w = (1-maschera)*z + maschera*y 
# plt.figure('mediano + originale'); plt.imshow(w, clim=None, cmap='gray')

# #tolgo i punti bianchi rimasti
# m = ndi.generic_filter(w, np.median, (2,2), mode='reflect')
# plt.figure('mediano'); plt.imshow(m, clim=None, cmap='gray')

# #potenzio bordi
# h = np.array([[ 0,-1, 0],
#               [-1, 5,-1],
#               [ 0,-1, 0]])

# g = ndi.correlate(m, h, mode='reflect')
# plt.figure('bordi enfatizzati'); plt.imshow(g, clim=None, cmap='gray')

# #equalizzo per vedere bene
# r = exp.equalize_hist(g, nbins=256)
# plt.figure("equalizzazione finale"); plt.imshow(r, clim=None, cmap='gray')

# #smooth leggero per vedere meglio
# f = ndi.gaussian_filter(r,0.5)
# plt.figure('smooth leggero'); plt.imshow(f, clim=None, cmap='gray')












































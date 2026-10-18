# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

"""
Negativo

"""
# z = io.imread(path_immagini/"mammografia.jpg")
# z = np.float64(z)
# plt.subplot(2,2,1); plt.imshow(z, clim=[0,255], cmap='gray'); plt.colorbar()
# plt.subplot(2,2,2); plt.hist(z.flatten(), bins=256); plt.xlim((0,255))

# zNeg = -z + 256 - 1
# plt.subplot(2,2,3); plt.imshow(zNeg, clim=[0,255], cmap='gray'); plt.colorbar()
# plt.subplot(2,2,4); plt.hist(zNeg.flatten(), bins=256); plt.xlim((0,255))

"""
Full Scale Histogram Stretch

"""
# x = io.imread(path_immagini/"granelli.jpg")
# x = np.float64(x)
# my.vediIstogramma(x)
# xS = my.fshs(x, 256)
# plt.figure()
# plt.subplot(1,2,1); plt.imshow(xS, clim = [0,255], cmap = 'gray')
# plt.subplot(1,2,2); plt.hist(xS.flatten(), bins = 256); plt.xlim((0,255))

# plt.figure('ottimizzato');
# plt.imshow(x, clim=None, cmap='gray')


"""
Logaritmo

"""
# x = io.imread(path_immagini/"spettro.jpg")
# x = np.float64(x)
# my.vediIstogramma(x)

# y = my.fshs(np.log(x+1), 256)  #devo sempre ricordarmi di stretchare l'istogramma
# my.vediIstogramma(y)

"""
Potenza

"""

# x = io.imread(path_immagini/"pout.tif")
# x = np.float64(x)
# my.vediIstogramma(x)

# z = x**0.02
# my.vediIstogrammaStretchato(z, 256)


"""
Equalizzazione

"""
import skimage.exposure as exp

x = io.imread(path_immagini/"marte.jpg")
x = np.float64(x)
my.vediIstogramma(x)

y = my.fshs(exp.equalize_hist(x), 256)
my.vediIstogramma(y)



















# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.exposure import equalize_hist
from skimage.transform import warp
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab")


"""Filtraggio mediante derivata prima (tecniche Gradiente)"""

"""esercizio house.y"""
# #import immagine
# file = str(path_immagini/"house.y")
# x = np.float64(np.fromfile(file, np.uint8))
# x = np.reshape(x, (512,512))
# plt.subplot(1,3,1); plt.imshow(x, clim = None, cmap = 'gray')

# #definisco derivate con maschere di Sobel

# #classiche
# # S1 = np.array([[-1,-2,-1],
# #                [ 0, 0, 0],
# #                 [1, 2, 1]])

# # S2 = np.array([[-1,0,1],
# #                [-2,0,2],
# #                [-1,0,1]])

# #enfasi su bordi obliqui
# S1 = np.array([[ 0, 1, 2],
#                [-1, 0, 1],
#                [-2,-1, 0]])

# S2 = np.array([[-2,-1, 0],
#                [-1, 0, 1],
#                [ 0, 1, 2]])

# y1 = ndi.convolve(x, S1, mode = 'reflect')
# y2 = ndi.convolve(x, S2, mode = 'reflect')

# """calcolo gradiente come elevamento al quadrato delle immagini filtrate dalle derivate"""
# G = np.sqrt(y1**2 + y2**2)
# plt.subplot(1,3,2); plt.imshow(G, clim = None, cmap = 'gray')

# """threshold + mappa"""
# T = 1.5 * np.mean(G)
# mask = G > T
# plt.subplot(1,3,3); plt.imshow(mask, clim = None, cmap = 'gray')






"""esercizio angiogramma"""
#import immagine
x_pre = np.float64(io.imread(path_immagini/"angiogramma.jpg"))
plt.subplot(1,4,1); plt.imshow(x_pre, clim = None, cmap = 'gray')

#pre elaborazione di smooth con filtro gaussiano N.B. dimensione maschera = 6 * sigma
sigma = 3
x = ndi.gaussian_filter(x_pre, (sigma,sigma))
plt.subplot(1,4,2); plt.imshow(x, clim = None, cmap = 'gray')

#alternativa usando media aritmetica
# x = ndi.uniform_filter(x_pre, (9,9))
# plt.subplot(1,4,2); plt.imshow(x, clim = None, cmap = 'gray')

#definisco derivate con maschere di Sobel
#enfasi su bordi obliqui
S1 = np.array([[ 0, 1, 2],
               [-1, 0, 1],
               [-2,-1, 0]])

S2 = np.array([[-2,-1, 0],
               [-1, 0, 1],
               [ 0, 1, 2]])

y1 = ndi.convolve(x, S1, mode = 'reflect')
y2 = ndi.convolve(x, S2, mode = 'reflect')

#calcolo gradiente
G = np.sqrt(y1**2 + y2**2)
plt.subplot(1,4,3); plt.imshow(G, clim = None, cmap = 'gray')

#threshold + mappa
T = 1.9 * np.mean(G)
mask = G > T
plt.subplot(1,4,4); plt.imshow(mask, clim = None, cmap = 'gray')

import skimage.morphology as morph

b = morph.disk(2)
z = morph.binary_erosion(mask, b)
plt.figure('output'); plt.imshow(z, clim=None, cmap='gray')









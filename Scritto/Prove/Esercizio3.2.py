# -*- coding: utf-8 -*-
import numpy as np
import scipy.ndimage as ndi
import skimage.io as io
from skimage.color import rgb2gray
import skimage.morphology as morph
import matplotlib.pyplot as plt
from seg_utils import zero_crossing
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")

x_ori = np.float64(io.imread(path_immagini/"ala_ape.jpg"))/255
x = rgb2gray(x_ori)
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

"edge detection con laplaciano di una gaussiana"
y = ndi.gaussian_laplace(x, 5)
y = zero_crossing(y)
plt.figure('laplaciano'); plt.imshow(y, clim=None, cmap='gray')


"edge detection con gradiente"
xm = ndi.generic_filter(x, np.median, (5,5))
plt.figure('mediano'); plt.imshow(xm, clim=None, cmap='gray')

# S1 = np.array([[-1,-2,-1],
#                [ 0, 0, 0],
#                [ 1, 2, 1]])

# S2 = np.array([[-1,0,1],
#                [-2,0,2],
#                [-1,0,1]])

S1 = np.array([[-2,-1, 0],
               [-1, 0, 1],
               [ 0, 1, 2]])

S2 = np.array([[ 0,-1,-2],
               [ 1, 0,-1],
               [ 2, 1, 0]])

y1 = ndi.convolve(xm, S1, mode = 'reflect')
y2 = ndi.convolve(xm, S2, mode = 'reflect')

G = np.sqrt((y1**2 + y2**2))
T = 4 * np.mean(G)
g = G > T

plt.figure('mediano + gradiente'); plt.imshow(g, clim = None, cmap = 'gray');

b = morph.disk(1)
f = morph.binary_opening(g, b)
f = morph.thin(g)

plt.figure('morphing'); plt.imshow(f, clim = None, cmap = 'gray');




"edge detection con k-means"
from sklearn.cluster import k_means

(M,N) = x.shape

xr = np.reshape(x, (M*N, 1))
cent, index, var = k_means(xr, 2)
km = np.reshape(index, (M,N))

plt.figure('k-means'); plt.imshow(km);

T = np.mean(cent)
mask = x > T
plt.figure('maschera globale k-means'); plt.imshow(mask, clim=[0,1], cmap='gray')





# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from seg_utils import zero_crossing
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")
plt.close('all')

file = str(path_immagini/"target_rumorosa.raw")
x = np.fromfile(file, np.float32)
x = x.reshape(256,256)

plt.figure(1); plt.imshow(x, clim=None, cmap='gray');plt.title('originale')


"edge detection con laplaciano di una gaussiana"
y = ndi.gaussian_laplace(x, 4.5)
y = zero_crossing(y)
# plt.figure(2); plt.imshow(y, clim=None, cmap='gray');plt.title('laplaciano')


"edge detection con gradiente"
S1 = np.array([[-1,-2,-1],
               [ 0, 0, 0],
               [ 1, 2, 1]])

S2 = np.array([[-1,0,1],
               [-2,0,2],
               [-1,0,1]])

y1 = ndi.convolve(x, S1, mode = 'reflect')
y2 = ndi.convolve(x, S2, mode = 'reflect')

G = np.sqrt(y1**2 + y2**2)

T = 2.5 * np.mean(G)
mask = G > T
plt.figure('gradiente'); plt.imshow(mask, clim = None, cmap = 'gray');


"strategia esercizio"

def filtra(block):
    
   # block = block.reshape(np.sqrt(len(block)), np.sqrt(len(block)))
    
    media_arit = np.mean(block**2)
    media_geom = (np.prod(block**2))**(1/len(block))
    
    return media_arit/media_geom
    
    
k = 5
w = ndi.generic_filter(x, filtra, (k,k), mode='reflect')
T = 1.15
output = w > T
plt.figure('strategia'); plt.imshow(output, clim = None, cmap = 'gray')


"applico operazione morfologica"

import skimage.morphology as morph

b = morph.disk(1)
#♥v = morph.binary_erosion(mask, b)
v = morph.binary_opening(output, b)
plt.figure('morph opening su strategia'); plt.imshow(v, clim = None, cmap = 'gray')
p = morph.thin(v)
plt.figure('morph thin su strategia'); plt.imshow(p, clim = None, cmap = 'gray')



















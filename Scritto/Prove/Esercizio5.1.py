# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io
import skimage.exposure as exp
from skimage.color import rgb2gray
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")

"import immagine"
x_rgb = np.float64(io.imread(path_immagini/"barbara.jpg"))/255
#plt.figure('originale'); plt.imshow(x_rgb, clim=None, cmap='gray')

x = x_rgb[:,:,0]
plt.figure('originale grigia'); plt.imshow(x, clim=None, cmap='gray')

(M,N) = x.shape


"definisco i filtri"
mask2 = ([[-1, 0, 0],
          [ 0, 0, 0],
          [ 0, 0, 1]])

mask2 = ([[ 0, 0,-1],
          [ 0, 0, 0],
          [ 1, 0, 0]])

L = ([[-1, 0,-1],
      [ 0, 4, 0],
      [-1, 0,-1]]) 

h = ndi.correlate(x, L, mode='reflect')
plt.figure('laplaciano'); plt.imshow(h, clim=None, cmap='gray')

"visualizzo in frequenza"
H = np.fft.fftshift(np.fft.fft2(h, (M,N)))









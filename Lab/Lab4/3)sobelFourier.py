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

"filtro di sobel in frequenza"

x = np.float64(io.imread(path_immagini/"lena.jpg"))
plt.subplot(1,2,1); plt.imshow(x, clim=None, cmap='gray');

h = np.array([[1,0,-1],
              [2,0,-2],
              [1,0,-1]], dtype=np.float64)

M,N = x.shape

""" qui devo passare anche la dimensione di uscita per poi
    eseguire la moltiplicazione """
    
X = np.fft.fft2(x)
H = np.fft.fft2(h, (M,N))

Y = H * X
y = np.real(np.fft.ifft2(Y))
plt.subplot(1,2,2); plt.imshow(y, clim=None, cmap='gray');

















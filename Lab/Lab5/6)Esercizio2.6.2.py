# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi 
import skimage.io as io
from skimage.color import rgb2hsv, hsv2rgb
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

""" Filtraggio in frequenza nella banda I"""

x = np.float64(io.imread(path_immagini/"foto_originale.tif"))/255
plt.figure('originale'); plt.imshow(x)

w = rgb2hsv(x)

i = w[:,:,2]
(M,N) = i.shape

I = np.fft.fftshift(np.fft.fft2(i))

n = np.fft.fftshift(np.fft.fftfreq(N))
m = np.fft.fftshift(np.fft.fftfreq(M))
l,k = np.meshgrid(n,m)

H = (np.abs(l) <= 0.10) & (np.abs(k) <= 0.25)
plt.figure('filtro'); plt.imshow(H, clim=None, cmap='gray', 
                                 extent=(-0.5, +0.5, +0.5, -0.5))

Y = H * I

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))

g = np.stack((w[:,:,0], w[:,:,1], y), -1)

output = hsv2rgb(g)
plt.figure('output'); plt.imshow(output)

































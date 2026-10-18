# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io
import skimage.metrics as met
import skimage.exposure as exp
import skimage.transform as tras
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

x = np.float64(io.imread(path_immagini/"mare.png"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

X = np.fft.fft2(x)
#Xquadro = (np.abs(X))**2
R = np.real(np.fft.ifft2(X))
plt.figure('antitrasformata'); plt.imshow(R, clim=None, cmap='gray')
                                          
"""APPESONE"""
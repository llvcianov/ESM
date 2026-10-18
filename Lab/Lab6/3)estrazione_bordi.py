# -*- coding: utf-8 -*-

import skimage.morphology as morph
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\immagini_lab_morfologia\DIP3E_Original_Images_CH09")

#attenzione se l'immagine non è binaria dividiamo per 255
x = np.float64(io.imread(path_immagini/"profilo.tif", plugin='pil'))/255
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

s = morph.square(3)
z = morph.binary_erosion(x,s)
plt.figure('erosa'); plt.imshow(x, clim=None, cmap='gray')

y = x - z

plt.figure('bordi'); plt.imshow(y, clim=None, cmap='gray')


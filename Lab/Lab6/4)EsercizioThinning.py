# -*- coding: utf-8 -*-
import skimage.morphology as morph
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\immagini_lab_morfologia\DIP3E_Original_Images_CH09")

"""thinning sull'impronta elaborata"""

x = np.float64(io.imread(path_immagini/"impronta.tif", plugin='pil'))/255
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

s = morph.disk(1)

z = morph.binary_opening(x,s)
z = morph.binary_closing(z,s)

z = morph.thin(z)

#letteralmente scheletrizza le figure, in questo caso l'effetto è lo stesso
#z = morph.skeletonize(z) 

plt.figure('bordi'); plt.imshow(z, clim=None, cmap='gray')

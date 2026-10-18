# -*- coding: utf-8 -*-
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.util import random_noise
from skimage.exposure import equalize_hist
from skimage.transform import warp
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

#import immagine
x = np.float64(io.imread(path_immagini/"lena.jpg"))
plt.subplot(1,3,1); plt.imshow(x, clim = None, cmap = 'gray')

#aggiunta rumore
noisy = random_noise(x, mode = 's&p')
plt.subplot(1,3,2); plt.imshow(noisy, clim = None, cmap = 'gray')


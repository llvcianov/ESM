# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi 
import skimage.io as io
from skimage.color import rgb2gray
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")

"import immagini"

x1 = np.float64(io.imread(path_immagini/"disk1.jpg"))/255
x1 = rgb2gray(x1)
plt.figure('originale1'); plt.imshow(x1, clim=None, cmap='gray')  

x2 = np.float64(io.imread(path_immagini/"disk2.jpg"))/255
x2 = rgb2gray(x2)
plt.figure('originale2'); plt.imshow(x2, clim=None, cmap='gray') 

"calcolo il quadrato dei laplaciani delle immagini"

L1 = ndi.laplace(x1, mode='reflect')
plt.figure('laplaciano1'); plt.imshow(L1, clim=None, cmap='gray') 

L2 = ndi.laplace(x2, mode='reflect')
plt.figure('laplaciano2'); plt.imshow(L2, clim=None, cmap='gray') 

L1_q = L1**2
L2_q = L2**2

"valuto livello attività calcolando formula con media e varianza"

media1 = ndi.uniform_filter(L1_q, (5,5), mode='reflect')
var1 = ndi.generic_filter(L1_q, np.var, (5,5), mode='reflect')

media2 = ndi.uniform_filter(L2_q, (5,5), mode='reflect')
var2 = ndi.generic_filter(L2_q, np.var, (5,5), mode='reflect')

att1 = media1 * var1
att2 = media2 * var2

"normalizzo e fondo"

norm1 = att1/(att1 + att2+1e-15)
# norm2 = att2/(att1 + att2)
norm2 = 1 - norm1

fusion = (norm1 * x1) + (norm2 * x2)

plt.figure('output'); plt.imshow(fusion, clim=None, cmap='gray') 


























          
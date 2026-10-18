# -*- coding: utf-8 -*-

import skimage.morphology as morph
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\immagini_lab_morfologia\DIP3E_Original_Images_CH09")

"""prova dilatazione - Esercizio 1"""
# x = np.float64(io.imread(path_immagini/"testo_fax.tif"))
# plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

# #elemento strutturante
# b = np.array([[0,1,0],[1,1,1],[0,1,0]], np.bool)
# y = morph.binary_dilation(x,b)
# plt.figure('dilatata'); plt.imshow(y, clim=None, cmap='gray')

""" Esercizio 2 
    Conservo i quadrati più grandi,
    l'elemento strutturante deve essere leggermente
    più piccolo del quadrato da consrvare """

# x = np.float64(io.imread(path_immagini/"quadrati.tif"))
# plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

# #elemento strutturante
# b = morph.square(16)
# y = morph.binary_erosion(x,b)
# plt.figure('erosa'); plt.imshow(y, clim=None, cmap='gray')
# z = morph.binary_dilation(y, b)
# plt.figure('output'); plt.imshow(z, clim=None, cmap='gray')


""" Esercizio 3
    Conservare solo il quadrato centrale """

x = np.float64(io.imread(path_immagini/"forme.tif"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

#tolgo imperfezioni interne
#elemento strutturante
b = morph.square(50)
y = morph.binary_dilation(x,b)
plt.figure('dilatata'); plt.imshow(y, clim=None, cmap='gray')
z = morph.binary_erosion(y, b)
plt.figure('erosa'); plt.imshow(z, clim=None, cmap='gray')

#tolgo imperfezioni esterne
#elemento strutturante
b1 = morph.square(100)
w = morph.binary_erosion(z,b1)
plt.figure('erosa2'); plt.imshow(w, clim=None, cmap='gray')
g = morph.binary_dilation(w, b1)
plt.figure('output2'); plt.imshow(g, clim=None, cmap='gray')

#N.B. POTEVO FARE MOLTO PRIMA COSI
h = morph.binary_closing(x, b)
k = morph.binary_opening(h, b1)
plt.figure('output_ottimizzato'); plt.imshow(k, clim=None, cmap='gray')




























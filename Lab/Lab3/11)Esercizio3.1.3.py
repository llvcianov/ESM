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

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab")

def enhanc(x,mask,k):
    X1 = mask * x
    a = 0.073
    b = 0.177
    h = ([[a,b,a],
          [b,0,b],
          [a,b,a]])
    
    for i in range(k):
        X2 = ndi.convolve(X1, h, mode = 'reflect') #immagine filtrata
        
        """ l'immagine finale è data dalla combinazione delle diverse immagini
            nei punti dati dalle maschere """
            
        X1 = (1-mask)*X2 + mask*X1 #nuova immagine
        
    return X1
        
       
""" carico immagine """
x = np.float64(io.imread(path_immagini/"bebe.jpg"))
plt.subplot(1,3,1); plt.imshow(x, clim = None, cmap = 'gray')

""" carico la maschera e la trasformo in maschera booleana"""
mask = np.float64(io.imread(path_immagini/"mask.bmp"))
mask1 = mask >= 255
plt.subplot(1,3,2); plt.imshow(mask, clim = [0,1], cmap = 'gray')

k = 100
y = enhanc(x, mask1, k)
plt.subplot(1,3,3); plt.imshow(y, clim = None, cmap = 'gray')









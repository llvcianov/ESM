# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.exposure import equalize_hist
from skimage.transform import warp
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab")


"""Point detection"""
x = np.float64(io.imread(path_immagini/"turbina.jpg"))
plt.subplot(1,3,1); plt.imshow(x, clim = None, cmap = 'gray')

h = np.array([[-1,-1,-1],
              [-1, 8,-1],
              [-1,-1,-1]])

y = ndi.convolve(x, h, mode = 'reflect')
plt.subplot(1,3,2); plt.imshow(y, clim = None, cmap = 'gray')

#N.B.   prendo il valore assoluto dell'immagine filtrata perchè
#       mi interessano le ampiezze per fare il thresholding
z = np.abs(y)
T = 0.9 * np.max(y)
mask = z < T
plt.subplot(1,3,3); plt.imshow(mask, clim = None, cmap = 'gray')

"""Line detection"""
#filtraggio
x = np.float64(io.imread(path_immagini/"quadrato.jpg"))
plt.subplot(2,3,1); plt.imshow(x, clim = None, cmap = 'gray'); plt.title('originale')

h1 = np.array([[-1,-1,-1],
                [ 2, 2, 2],
                [-1,-1,-1]])
y1 = np.abs(ndi.convolve(x, h1, mode = 'reflect'))
plt.subplot(2,3,2); plt.imshow(y1, clim = None, cmap = 'gray'); plt.title('orizzontale')

h2 = np.array([[-1,-1, 2],
                [-1, 2,-1],
                [ 2,-1,-1]])
y2 = np.abs(ndi.convolve(x, h2, mode = 'reflect'))
plt.subplot(2,3,3); plt.imshow(y2, clim = None, cmap = 'gray'); plt.title('diagonaledx')

h3 = np.array([[-1,2,-1],
                [-1,2,-1],
                [-1,2,-1]])
y3 = np.abs(ndi.convolve(x, h3, mode = 'reflect'))
plt.subplot(2,3,4); plt.imshow(y3, clim = None, cmap = 'gray'); plt.title('verticale')

h4 = np.array([[ 2,-1,-1],
                [-1, 2,-1],
                [-1,-1, 2]])
y4 = np.abs(ndi.convolve(x, h4, mode = 'reflect'))
plt.subplot(2,3,5); plt.imshow(y4, clim = None, cmap = 'gray'); plt.title('diagonalesx')

""" faccio lo stack dei filtri nelle varie dimensioni per avere un filtraggio
    completo """
z = np.stack((y1,y2,y3,y4), -1)
z = np.max(z, -1)
plt.subplot(2,3,6); plt.imshow(z, clim = None, cmap = 'gray'); plt.title('filtraggio_totale')


""" stessa cosa per le mappe, thresholding e stack delle varie direzioni"""
#thresholding
k = 0.4
th1 = k * np.max(y1)
th2 = k * np.max(y2)
th3 = k * np.max(y3)
th4 = k * np.max(y4)

#mappa
mask1 = y1>th1
mask2 = y2>th2
mask3 = y3>th3
mask4 = y4>th4

w = np.stack((mask1,mask2,mask3,mask4), -1)
w = np.max(w, -1)

plt.figure(3)
plt.subplot(2,3,1); plt.imshow(mask1, clim=[0,1], cmap='gray'); plt.title('mappa_orizzontale')
plt.subplot(2,3,2); plt.imshow(mask2, clim=[0,1], cmap='gray'); plt.title('mappa_diagonaledx')
plt.subplot(2,3,3); plt.imshow(mask3, clim=[0,1], cmap='gray'); plt.title('mappa_verticale')
plt.subplot(2,3,4); plt.imshow(mask4, clim=[0,1], cmap='gray'); plt.title('mappa_diagonalesx')
plt.subplot(2,3,6); plt.imshow(w, clim = [0,1], cmap = 'gray'); plt.title('mappa_totale')

# eventuale thinning, qui inutile perchè i bordi sono già molto snelli









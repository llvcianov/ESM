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


"""Smoothing seguito da thresholding"""

#immagine originale
x = np.float64(io.imread(path_immagini/"space.jpg"))
plt.subplot(1,3,1); plt.imshow(x, clim = None, cmap = 'gray')

#effettuo smoothing
x_filt = ndi.uniform_filter(x, (15,15), mode = 'reflect')
plt.subplot(1,3,2); plt.imshow(x_filt, clim = None, cmap = 'gray')

"""effettuo thresholding
N.B. PRIMA DEFINISCO LA SOGLIA E DOPO SCARTO I PIXEL.
LO SCARTO VA FATTO SULL'IMMAGINE FILTRATA POICHè SENO POTREI AVERE RISULTATI INSTABILI 
CAUSA RUMORE. COSI HO UN RISULTTAO PIù RAPPRESENTATIVO DELLA SCENA"""
T = 0.25 * np.max(x_filt) 
mask = x_filt < T  
x[mask] = 0   
plt.subplot(1,3,3); plt.imshow(x, clim = None, cmap = 'gray')


"""Aggiunta del rumore + filtraggio + valutazione qualità"""
# #immagine originale
# x = np.float64(io.imread(path_immagini/"lena.jpg"))
# (M,N) = x.shape
# plt.subplot(1,3,1); plt.imshow(x, clim = None, cmap = 'gray')

# #aggiungo rumore
# d = 25 #deviazione standard rumore
# n = d * np.random.randn(M, N)
# noisy = x + n
# plt.subplot(1,3,2); plt.imshow(noisy, clim = None, cmap = 'gray')

# #effettuo smoothing e valuto MSE
# y = ndi.uniform_filter(noisy, (5,5), mode = 'reflect')
# plt.subplot(1,3,3); plt.imshow(y, clim = None, cmap = 'gray')

# mse = np.mean((y - x)**2)
# print(mse)


"""Filtraggio spaziale adattivo"""

def filtra(x, sigma):
    
    (M,N) = x.shape
    
    """aggiungo rumore"""
    n = sigma * np.random.randn(M, N)
    noisy = x + n
    
    """valuto media e varianza locale dell'immagine rumorosa"""
    media_locale = ndi.uniform_filter(noisy, (7,7), mode = 'reflect')
    var_locale = ndi.generic_filter(noisy, np.var, (7,7), mode = 'reflect')
    
    """effettuo elaborazione"""
    y = noisy - ((sigma**2)*(noisy - media_locale)/(var_locale))
    
    """valuto MSE adattivo"""
    mse_adapt = np.mean((y - x)**2)
    
    """filtro con media aritmetica"""
    z = ndi.generic_filter(noisy, np.mean, (7,7), mode='reflect')
    
    """valuto MSE media"""
    mse_media = np.mean((z - x)**2)
    
    return mse_adapt, mse_media
    
    
"""immagine originale"""
x = np.float64(io.imread(path_immagini/"barbara.gif"))
plt.figure('originale'); plt.imshow(x, clim = None, cmap = 'gray')

"""assi per il grafico"""
asseX = np.array([5,10,15,20,25,30,35])
asseYadapt = []
asseYmedia = []

for i in range(7):
    
    mse_adapt, mse_media = filtra(x, asseX[i])
    
    asseYadapt.append(mse_adapt)
    asseYmedia.append(mse_media)

plt.figure('grafico')
plt.plot(asseX, asseYadapt, '-ro', label='filtro adattivo', color='red')
plt.plot(asseX, asseYmedia, '-ro', label='filtro media aritmetica', color='blue')
plt.grid(True)
plt.legend()
plt.xlabel('deviazione standard rumore')
plt.ylabel('MSE')  

    
    
    
    
    
"""
filtro adattivo funziona meglio al crescere della deviazione standard del rumore
tanto più la finestra è grande.
vedi grafico in script differenza grafico filtro adattivo e media
"""

    
# """codice funzione"""
# """aggiungo rumore"""
# d = 35 #deviazione standard rumore
# n = d * np.random.randn(M, N)
# noisy = x + n
# plt.subplot(1,3,2); plt.imshow(noisy, clim = None, cmap = 'gray')

# """valuto media e varianza loacale dell'immagine rumorosa"""
# k = 9
# media_locale = ndi.uniform_filter(noisy, (k,k), mode = 'reflect')
# var_locale = ndi.generic_filter(noisy, np.var, (k,k), mode = 'reflect')

# """effettuo elaborazione"""
# y = noisy - ((d**2)*(noisy - media_locale)/(var_locale))
# plt.subplot(1,3,3); plt.imshow(y, clim = None, cmap = 'gray')

# """valuto MSE"""
# mse = np.mean((y - x)**2)
# print(mse)






















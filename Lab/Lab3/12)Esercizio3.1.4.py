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

def Varianza(kernel):
    
    """reshape perchè ndi.generic.filter passa i dati come array 1D """
    kernel = kernel.reshape(9,9)  
    
    """ N.B. ATTENZIONE qui trasformo in maschera booleana per prendere solo gli 1
        necessario per non pesare gli 0 nella varianza """
        
    mask1 = (np.array([[0,0,0,0,0,0,0,1,1],
                      [0,0,0,0,0,0,1,1,1],
                      [0,0,0,0,0,1,1,1,0],
                      [0,0,0,0,1,1,1,0,0],
                      [0,0,0,1,1,1,0,0,0],
                      [0,0,1,1,1,0,0,0,0],
                      [0,1,1,1,0,0,0,0,0],
                      [1,1,1,0,0,0,0,0,0],
                      [1,1,0,0,0,0,0,0,0]]) > 0) 
    
    mask2 = (np.array([[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [1,1,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,1,1,1],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0]]) > 0)
    
    mask3 = (np.array([[1,1,0,0,0,0,0,0,0],
                      [1,1,1,0,0,0,0,0,0],
                      [0,1,1,1,0,0,0,0,0],
                      [0,0,1,1,1,0,0,0,0],
                      [0,0,0,1,1,1,0,0,0],
                      [0,0,0,0,1,1,1,0,0],
                      [0,0,0,0,0,1,1,1,0],
                      [0,0,0,0,0,0,1,1,1],
                      [0,0,0,0,0,0,0,1,1]]) > 0)
    
    mask4 = (np.array([[0,0,0,1,1,1,0,0,0],
                      [0,0,0,1,1,1,0,0,0],
                      [0,0,0,1,1,1,0,0,0],
                      [0,0,0,1,1,1,0,0,0],
                      [0,0,0,1,1,1,0,0,0],
                      [0,0,0,1,1,1,0,0,0],
                      [0,0,0,1,1,1,0,0,0],
                      [0,0,0,1,1,1,0,0,0],
                      [0,0,0,1,1,1,0,0,0]]) > 0)
    
    """ incicizzo per calcolare quella a varianza minima a tempo esecuzione """
    masks = [mask1, mask2, mask3, mask4] 
    
    """ la varianza va calcolata sul blocco nelle posizioni date dalla maschera """
    
    var1 = np.var(kernel[mask1])
    var2 = np.var(kernel[mask2])
    var3 = np.var(kernel[mask3])
    var4 = np.var(kernel[mask4])
    varianze = np.array([var1, var2, var3, var4])
    
    """ uso di np.argmin per calcolare a tempo di esecuzione 
        l'indice della varianza minore"""
        
    indice_maschera = np.argmin(varianze)
    
    """ uso l'indice per prendere la maschera giusto da applicare """
    return np.mean(kernel[masks[indice_maschera]])

    
"""leggo immagine"""

file = str(path_immagini/"zebre.y")
x = np.fromfile(file, np.uint8)
x = x.reshape(321,481)
(M,N) = x.shape
plt.figure('immagine originale'); plt.imshow(x, clim = None, cmap = 'gray')

"""applico rumore"""

d = 25 #deviazione standard rumore
n = d * np.random.randn(M, N)
noisy = x + n
plt.figure('immagine rumorosa'); plt.imshow(noisy, clim = None, cmap = 'gray')

"""filtro non lineare + calcolo PSNR"""

x_filt = ndi.generic_filter(noisy, Varianza, (9,9), mode = 'reflect')
plt.figure('immagine filtrata non lineare'); plt.imshow(x_filt, clim = None, cmap = 'gray')
MSE = np.mean((x - x_filt)**2)
PSNR = 10 * np.log10((255**2)/MSE)
print (PSNR, "PSNR non lineare")

"""filtro lineare + calcolo PSNR"""

x_filt1 = ndi.uniform_filter(noisy, (5,5), mode = 'reflect')
plt.figure('immagine filtrata lineare'); plt.imshow(x_filt1, clim=None, cmap='gray')
MSE = np.mean((x - x_filt1)**2)
PSNR = 10 * np.log10((255**2)/MSE)
print(PSNR, "PSNR lineare" )













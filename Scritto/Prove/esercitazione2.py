# -*- coding: utf-8 -*-

import numpy as np
import scipy.ndimage as ndi
import skimage.io as io
import skimage.transform as tras
import skimage.exposure as exp
import matplotlib.pyplot as plt
import myLibreria as my
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\esercitazione_250411\esercitazione_250411")
plt.close('all')

def adapt_filter(x,k):
    #calcolo varianza locale e percentile
    var = ndi.generic_filter(x, np.var, (k,k), mode='reflect')
    T = np.percentile(var, 70)
    
    #definisco la maschera
    mask1 = ((var < T).reshape(M,N))

    #filtro le medie
    med1 = ndi.generic_filter(noisy, np.mean, (k,k), mode='reflect')
    #plt.figure('media1'); plt.imshow(med1, clim=None, cmap='gray')

    med2 = ndi.generic_filter(noisy, np.mean, (k-2,k-2), mode='reflect')
    #plt.figure('media2'); plt.imshow(med2, clim=None, cmap='gray')

    #adatto
    return med1*mask1 + med2*(1-mask1)
    
    
x = np.float64(io.imread(path_immagini/"cigno.jpg"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')
(M,N)=x.shape

#aggiungo rumore
d = 25 #deviazione standard rumore
n = d * np.random.randn(M, N)
noisy = x + n
plt.figure('rumorosa'); plt.imshow(noisy, clim = None, cmap = 'gray')

#y = adapt_filter(noisy, 5)
# y = ndi.uniform_filter(noisy, (5,5), mode='reflect')
# plt.figure()
# plt.subplot(1,2,1); plt.imshow(y, clim=None, cmap='gray');plt.title('filtrata')
# plt.subplot(1,2,2); plt.hist(y.flatten(), bins=256)

# z = exp.rescale_intensity(y, in_range='image', out_range=(0,255))
# z = np.round(z)
# plt.figure()
# plt.subplot(1,2,1); plt.imshow(z, clim=None, cmap='gray');plt.title('riscalata per MSE')
# plt.subplot(1,2,2); plt.hist(z.flatten(), bins=256)

valuesX = np.array([3,5,7,9])
valuesAdapt = np.zeros(4)
valuesMean = np.zeros(4)

for i in range(0,4):
    k = valuesX[i] 
    
    #filtro adattivo
    y = adapt_filter(noisy, k)
    y = np.round(exp.rescale_intensity(y, in_range='image', out_range=(0,255)))
    MSE1 = np.mean((x-y)**2)
    PSNR1 = 10 * np.log10((255**2)/MSE1)
    valuesAdapt[i] = PSNR1
    
    #filtro media
    z = ndi.uniform_filter(noisy, (k,k), mode='reflect')
    z = np.round(exp.rescale_intensity(z, in_range='image', out_range=(0,255)))
    MSE2 = np.mean((x-z)**2)
    PSNR2 = 10 * np.log10((255**2)/MSE2)
    valuesMean[i] = PSNR2
    
    if(i == 1):
        plt.figure()
        plt.subplot(1,2,1); plt.imshow(y, clim=None, cmap='gray'); plt.title('adattivo, k=5')
        plt.subplot(1,2,2); plt.imshow(z, clim=None, cmap='gray'); plt.title('media, k=5')
    
    
plt.figure()
plt.plot(valuesX, valuesAdapt, label='filtro adattivo', color='blue')
plt.plot(valuesX, valuesMean, label='filtro media', color='red')
plt.xlabel('dimensioni blocco')
plt.ylabel('PSNR')
plt.legend()
plt.grid(True)
plt.show()
    




# #calcolo varianza locale
# k = 5
# var = ndi.generic_filter(noisy, np.var, (k,k), mode='reflect')
# T = np.percentile(var, 70)

# #definisco la maschera
# mask1 = ((var < T).reshape(M,N))

# #filtro le medie
# med1 = ndi.generic_filter(noisy, np.mean, (k,k), mode='reflect')
# plt.figure('media1'); plt.imshow(med1, clim=None, cmap='gray')

# med2 = ndi.generic_filter(noisy, np.mean, (k-2,k-2), mode='reflect')
# plt.figure('media2'); plt.imshow(med2, clim=None, cmap='gray')

# y = med1*mask1 + med2*(1-mask1)
# plt.figure('filtrata con adattivo'); plt.imshow(y, clim=None, cmap='gray')



    
    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
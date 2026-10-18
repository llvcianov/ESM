# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io
import skimage.metrics as met
from skimage.color import rgb2gray
import skimage.exposure as exp
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")


"import immagine"
x_rgb = np.float64(io.imread(path_immagini/"barbara.jpg"))
x = rgb2gray(x_rgb)
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

"aggiungo rumore"
(M,N) = x.shape
sigma = 20
n = sigma * np.random.randn(M,N)
noisy = x + n
plt.figure('rumorosa'); plt.imshow(noisy, clim=None, cmap='gray')


"filtro"
def filt(block):
    
    block = block.reshape(7,7)    
    mask1 = block < (block[3,3] + 2 * 20)
    mask2 = block > (block[3,3] - 2 * 20)
    mask = mask1 & mask2
    numero = np.sum(mask)
    
    if (numero < 4):     
        return np.mean(block)
    else:
        return np.mean(block[mask])
        
    
K = 7
noisy_filt = ndi.generic_filter(noisy, filt, (K,K), mode='reflect')
plt.figure('filtrata'); plt.imshow(noisy_filt, clim=None, cmap='gray')


"calcolo PSNR"
PSNR = met.peak_signal_noise_ratio(x, noisy_filt, data_range=255)
print(f"Il PSNR tra immagine originale e filtrata è {PSNR}")





































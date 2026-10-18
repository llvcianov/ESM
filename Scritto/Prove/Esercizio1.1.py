# -*- coding: utf-8 -*-
import numpy as np
import scipy.ndimage as ndi
import skimage.io as io
import skimage.metrics as met
import matplotlib.pyplot as plt
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")

"import immagine"
x = np.float64(io.imread(path_immagini/"lena.jpg"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

"aggiunta rumore"

""" da usare all'esame

    from skimage.util import random_noise
    noisy_image = random_noise(x, mode='s&p', amount=0.05)"""
    

(M,N) = x.shape
val = np.random.rand(M,N)
mask1 = val < 0.2
mask2 = (val*2) < 0.2
noisy = np.copy(x)
noisy[mask1] = 0
noisy[mask2] = 255

    
# noisy = np.float64(io.imread(path_immagini/"lena_s&p.png"))
plt.figure('rumorosa'); plt.imshow(noisy, clim=None, cmap='gray')

"funzione filtro"

def smf(x,k,T):
    
    "mediano"
    noisy_m = ndi.generic_filter(x, np.median, (k,k), mode='reflect')
    
    "maschera per filtrare"
    z_mask = np.abs(noisy_m - x) > T
    
    "filtro"
    switch_m_filter = (noisy_m * z_mask) + (x * (1 - z_mask))
    
    return switch_m_filter, noisy_m
    

"definisco liste per gli assi e soglia"
asseX = [3,5,7,9,11]
asseY_switch = []
asseY_median = []

T = 30

"ciclo la funzione popolando le liste"
for i in range(5):
    (s,m) = smf(noisy, asseX[i], T)
    
    PSNR_s = met.peak_signal_noise_ratio(x, s, data_range=255)
    PSNR_m = met.peak_signal_noise_ratio(x, m, data_range=255)
    
    asseY_switch.append(PSNR_s)
    asseY_median.append(PSNR_m)
    
    if (i == 1):
        plt.figure('switch median filter'); plt.imshow(s, clim=None, cmap='gray')
        plt.figure('filtro mediano'); plt.imshow(m, clim=None, cmap='gray')

"plotto il grafico"
plt.figure('grafico')
plt.plot(asseX, asseY_switch, '-ro', label='switch median filter', color='blue')
plt.plot(asseX, asseY_median, '-ro', label='filtro mediano', color='red')
plt.legend()
plt.grid(True)
plt.xlabel('dimensioni finestra')
plt.ylabel('PSNR')





"codice funzione"
# z_mask = np.abs(noisy_m - noisy) > T

# switch_m_filter = (noisy_m * z_mask) + (noisy * (1 - z_mask))

# plt.figure('switching_median_filter'); plt.imshow(switch_m_filter,
#                                                   clim=None, cmap='gray')





























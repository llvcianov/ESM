# -*- coding: utf-8 -*-

import numpy as np
import scipy.ndimage as ndi
import skimage.io as io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")

"import immagine"
x1_rgb = np.float64(io.imread(path_immagini/"I1.png"))/255

x2_rgb = np.float64(io.imread(path_immagini/"I2.png"))/255

"converto in scala di grigi"
x1 = rgb2gray(x1_rgb)
x2 = rgb2gray(x2_rgb)
plt.figure('originale1'); plt.imshow(x1, clim=None, cmap='gray')
plt.figure('originale2'); plt.imshow(x2, clim=None, cmap='gray')


"applico maschera punto 1 esercizio"
mask = ([[-1, 2,-1],
         [ 2,-4, 2],
         [-1, 2,-1]])     

x1_filt = ndi.correlate(x1, mask, mode='reflect')
x2_filt = ndi.correlate(x2, mask, mode='reflect')

"filtro al secondo punto"

def filtra(block):
    block = block.reshape(3,3)
    
    "parametro 0"
    u0 = block[0,0] - block[1,1]
    if(u0 < 0): u0 = 0
    else: u0 = 1
    u0s = u0 * (2**0)    
     
    "parametro 1"
    u1 = block[0,1] - block[1,1]
    if(u1 < 0): u1 = 0
    else: u1 = 1
    u1s = u1 * (2**1) 
    
    "parametro 2"
    u2 = block[0,2] - block[1,1]
    if(u2 < 0): u2 = 0
    else: u2 = 1
    u2s = u2 * (2**2) 
    
    "parametro 3"
    u3 = block[1,2] - block[1,1]
    if(u3 < 0): u3 = 0
    else: u3 = 1
    u3s = u3 * (2**3) 
    
    "parametro 4"
    u4 = block[2,2] - block[1,1]
    if(u4 < 0): u4 = 0
    else: u4 = 1
    u4s = u4 * (2**4) 
    
    "parametro 5"
    u5 = block[2,1] - block[1,1]
    if(u5 < 0): u5 = 0
    else: u5 = 1
    u5s = u5 * (2**5) 
    
    "parametro 6"
    u6 = block[2,0] - block[1,1]
    if(u6 < 0): u6 = 0
    else: u6 = 1
    u6s = u6 * (2**6) 
    
    "parametro 7"
    u7 = block[1,0] - block[1,1]
    if(u7 < 0): u7 = 0
    else: u7 = 1
    u7s = u7 * (2**7) 

    return (u0s + u1s + u2s + u3s + u4s + u5s + u6s + u7s)

y1 = ndi.generic_filter(x1_filt, filtra, (3,3), mode='reflect')
y2 = ndi.generic_filter(x2_filt, filtra, (3,3), mode='reflect')

"visualizzo istogramma e valuto"

plt.figure('istogramma1'); plt.hist(y1.flatten(), bins=256); plt.xlim=(0,255)
plt.figure('istogramma2'); plt.hist(y2.flatten(), bins=256); plt.xlim=(0,255)

y1flat = y1.flatten()
y2flat = y2.flatten()

a1, b1 = np.histogram(y1flat, bins=256)
a2, b2 = np.histogram(y2flat, bins=256)

std1 = np.std(a1)
std2 = np.std(a2)

if (std1 > 495): print("la foto 1 è vera")   
else: print("La foto 1 è falsa")

if (std2 > 495): print("la foto 2 è vera")   
else: print("La foto 2 è falsa")












































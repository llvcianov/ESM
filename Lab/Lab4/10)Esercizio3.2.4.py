# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import skimage.transform as tform
import skimage.exposure as exp
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")
plt.close('all')

"""Immagini sintetiche"""

def densitàLF(x, tau):
    H = np.log(np.abs(np.fft.fftshift(np.fft.fft2(x)))) 
    
    (M,N) = x.shape
    n = np.fft.fftshift(np.fft.fftfreq(N))
    m = np.fft.fftshift(np.fft.fftfreq(M))
    l,k = np.meshgrid(n, m)
    
    D = np.sqrt(l**2 + k**2)
    mask = (D <= tau)
    Y = mask * H
    
    sommaLF = np.sum(Y[Y > 0])
    sommaTotale = np.sum(H)
    return sommaLF/sommaTotale
    
def leggi(file, tau):
    xRGB = np.float64(io.imread(path_immagini/file))/255
    plt.figure('originale'); plt.imshow(xRGB); 

    "per trasformare in scala di grigi faccio semplicemente la media dei 3 canali"
    "np.mean(xRGB,2) fa la media lungo il 3 asse dell'immagine, ovvero lungo i 3 canali RGB"
    x = np.mean(xRGB,2)
    
    d = densitàLF(x,tau)
    if (d < 0.7):
        print(f"l'immagine {file} è sintetica con densità = {d}")
    else:
        print(f"l'immagine {file} è naturale con densità = {d}")
       
tau = 0.35   
file1 = "volto1.png"
leggi(file1, tau)

file2 = "volto2.png"
leggi(file2, tau)

file3 = "volto3.png"
leggi(file3, tau)

file4 = "volto4.png"
leggi(file4, tau)







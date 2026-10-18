# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import skimage.exposure as exp
import skimage.transform as tras
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

"""Immagini ridimensionate"""

def detect(x):
    (M,N) = x.shape
    
    """orizzontali"""
    mask_d2_hori = np.array([[0, 0, 0],
                             [-1,2,-1],
                             [0, 0, 0]])
    
    d2_hori = ndi.correlate(x, mask_d2_hori, mode='reflect')
    Pvar_hori = np.sum(np.abs(d2_hori), 0)
    
    mask_d_hori = np.array([-1,1])
    d_hori = ndi.correlate(Pvar_hori, mask_d_hori)
    
    D_hori = np.abs(np.fft.fftshift(np.fft.fft(d_hori, N-2)))
    f = np.fft.fftshift(np.fft.fftfreq(N-2))
    ni_hori = f[(D_hori == np.max(D_hori)) & (f > 0)]
    R_hori = 1/ni_hori
    
    
    """verticali"""
    mask_d2_vert = mask_d2_hori.T
    
    d2_vert = ndi.correlate(x, mask_d2_vert, mode='reflect')
    Pvar_vert = np.sum(np.abs(d2_vert), 1)
    
    mask_d_vert = np.array([-1,1])
    d_vert = ndi.correlate(Pvar_vert, mask_d_vert)
    
    D_vert = np.abs(np.fft.fftshift(np.fft.fft(d_vert, M-2)))
    f = np.fft.fftshift(np.fft.fftfreq(M-2))
    ni_vert = f[(D_vert == np.max(D_vert)) & (f > 0)]
    R_vert = 1/ni_vert
    
    return D_hori, D_vert, R_hori, R_vert
    
    
    
    
file = str(path_immagini/"zoom.y")
x = np.fromfile(file, np.float32)
x = np.reshape(x,(128,128))


D_hori, D_vert, R_hori, R_vert = detect(x)
f_hori = np.fft.fftshift(np.fft.fftfreq(len(D_hori)))
f_vert = np.fft.fftshift(np.fft.fftfreq(len(D_vert)))

plt.figure() 
plt.subplot(2,1,1)
plt.plot(f_hori, D_hori, '-or')
plt.title(f'DFT derivata pseudo-varianza orizontale, fattori di scala: {R_hori}')
plt.subplot(2,1,2)
plt.plot(f_vert, D_vert,'-or')
plt.title(f'DFT derivata pseudo-varianza verticale, fattori di scala: {R_vert}')




"""
#codice funzione
(M,N) = x.shape

plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

mask_d2 = np.array([[0, 0, 0],
                    [-1,2,-1],
                    [0, 0, 0]])

d2 = ndi.correlate(x, mask_d2, mode='reflect')
plt.figure('derivata'); plt.imshow(d2, clim=None, cmap='gray')

#per ogni colonna dell'immagine, sommo tutte le righe
#cioè funzione np.sum sulla prima dimensione per inidicare che somma
#solo le righe e non le colonne. Quindi alla fine avrò un vettore
Pvar = np.sum(np.abs(d2), 0)

#calcolo la derivata prima di un vettore
mask_d = np.array([-1,1])
dPvar = ndi.correlate(Pvar, mask_d)

#alternativamente posso fare anche così
#dPvar = Pvar[1:] - Pvar[:-1]

#calcolo la DFT su N-2 punti come da guida esercizio e la shifto in -1/2, 1/2
D = np.abs(np.fft.fftshift(np.fft.fft(dPvar, N-2)))

#devo calcolare il picco nell'intervallo 0,1/2
#per avere questa coordinata devo innanzitutto creare un intervallo in cui muovermi
#se stessi lavorando in due dimensioni avrei dovuto usare meshgrid
f = np.fft.fftshift(np.fft.fftfreq(N-2))

#la posizione è la frequenza in cui D assume valore massimo nelle f positive
mask = (D==np.max(D)) & (f>0)
n0 = f[mask]
"""























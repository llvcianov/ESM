# -*- coding: utf-8 -*-
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")
plt.close('all')


def elabora(x, r1, r2):
    X = np.fft.fftshift(np.fft.fft2(x))
    (M,N) = x.shape
    n = np.fft.fftshift(np.fft.fftfreq(N))
    m = np.fft.fftshift(np.fft.fftfreq(M))
    l,k = np.meshgrid(n,m)
    H = ((np.abs(l) >= r1) & (np.abs(l) <= r2)) & ((np.abs(k) >= r1) & (np.abs(k) <= r2))
    Y = H * X
    #definisco maschera con valori maggiori di zero
    mask = np.abs(Y) > 0
    #calcolo il quadrato del modulo
    YQ = (np.abs(Y))**2
    #conto elementi maggiori di zero
    Omega = np.sum(mask)
    #calcolo energia
    EM = np.sum(YQ[mask])/Omega
    E = np.sum(np.abs(x)**2)
    return EM/E
    
    
x1 = np.float64(io.imread(path_immagini/"impronta1.tif"))
plt.figure('originale1'); plt.imshow(x1, clim=None, cmap='gray')

x2 = np.float64(io.imread(path_immagini/"impronta2.tif"))
plt.figure('originale2'); plt.imshow(x2, clim=None, cmap='gray')

r1 = 0.10
r2 = 0.25

impronta1 = elabora(x1, r1, r2)
impronta2 = elabora(x2, r1, r2)

if(impronta1 > impronta2):
    print("l'impronta 1 è autentica")
else:
    print("l'impronta 2 è autentica")
    




# #codice funzione
# X = np.fft.fftshift(np.fft.fft2(x))
# plt.figure('trasformata'); plt.imshow(np.log(1+np.abs(X)), clim=None, cmap='gray',
#                                       extent=(-0.5,+0.5,+0.5,-0.5))

# (M,N) = x.shape
# n = np.fft.fftshift(np.fft.fftfreq(N))
# m = np.fft.fftshift(np.fft.fftfreq(M))
# l,k = np.meshgrid(n,m)

# r1 = 0.10
# r2 = 0.25

# H = ((np.abs(l) >= r1) & (np.abs(l) <= r2)) & ((np.abs(k) >= r1) & (np.abs(k) <= r2))
# plt.figure('filtro'); plt.imshow(H, clim=[0,1], cmap='gray',
#                                       extent=(-0.5,+0.5,+0.5,-0.5))

# Y = H * X
# plt.figure('filtrata'); plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray',
#                                       extent=(-0.5,+0.5,+0.5,-0.5))

# #definisco maschera con valori maggiori di zero
# mask = Y > 0
# #calcolo il quadrato del modulo
# YQ = (np.abs(Y))**2
# #conto elementi maggiori di zero
# Omega = np.sum(Y>0)
# #calcolo energia
# Em = np.sum(YQ[mask])/Omega




    #definisco maschera con valori maggiori di zero
    mask = np.abs(Y) > 0
    #calcolo il quadrato del modulo
    YQ = (np.abs(Y))**2
    #conto elementi maggiori di zero
    Omega = np.sum(mask)








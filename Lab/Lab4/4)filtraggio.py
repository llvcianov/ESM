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

"filtraggio in frequenza"
x = np.float64(io.imread(path_immagini/"lena.jpg"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray');
X = np.fft.fft2(x)
X = np.fft.fftshift(X)
plt.figure('trasformata lena');
plt.imshow(np.log(1+np.abs(X)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));

""" creo la griglia """
M,N = x.shape
m = np.fft.fftshift(np.fft.fftfreq(M))
n = np.fft.fftshift(np.fft.fftfreq(N))
l,k = np.meshgrid(n,m)

""" definisco il filtro
    D è un generico punto del grafico il
    cui centro del sistema di coordinate è in 0,0 """
    
D = np.sqrt(k**2+ l**2) 
D0 = 0.1;
H = (D <= D0)
plt.figure('filtro');
plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));

#filtraggio
Y = H * X
plt.figure('trasformata filtrata');
plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));

#ricostruisco dalla trasformata filtrata
Y = np.fft.ifftshift(Y)
y = np.real(np.fft.ifft2(Y))
plt.figure('lena filtrata');
plt.imshow(y, clim=[0,255], cmap='gray');

















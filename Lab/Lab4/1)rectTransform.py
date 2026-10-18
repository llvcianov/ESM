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

"trasformata di una rect + visualizzazione"
x = np.float64(io.imread(path_immagini/"rettangolo.jpg"))
plt.subplot(1,3,1); plt.imshow(x, clim=None, cmap='gray');
X = np.fft.fft2(x)
plt.subplot(1,3,2); plt.imshow(np.abs(X), clim=None, cmap='gray');

""" Problema frequenze basse sono negli angoli quindi facciamo shift
    per visualizzarla tra -1/2 e 1/2. 
    E successivamente il log dello spettro di ampiezza
    per visualizzare il grafico correttamente uso parametro extent """
    
Y = np.log(1+np.abs(np.fft.fftshift(X)))
plt.subplot(1,3,3); plt.imshow(Y, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));

""" codice per visualizzare il grafico 3d della trasformata """

from mpl_toolkits.mplot3d import Axes3D

"""creo la griglia di coordinate"""
(M,N) = Y.shape
m = np.fft.fftshift(np.fft.fftfreq(M))
n = np.fft.fftshift(np.fft.fftfreq(N))
l,k = np.meshgrid(n,m)

"""plotto la figura sul grafico"""
ax = Axes3D(plt.figure()); # crea una figura per i grafici 3d
ax.plot_surface(l,k,Y, linewidth=0, cmap='jet')











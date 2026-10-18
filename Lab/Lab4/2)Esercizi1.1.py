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

"1.1.1 confronto immagine e trasformata"
# x = np.float64(io.imread(path_immagini/"anelli.tif"))
# plt.figure(); plt.imshow(x, clim=None, cmap='gray');

# X = np.log(1 + abs(np.fft.fftshift(np.fft.fft2(x))))
# plt.figure(); plt.imshow(X, clim=None, cmap='gray', extent = (-0.5,+0.5,-0.5,+0.5));


"1.1.2 visualizzazione spettro di ampiezza e fase + ricostruzione"
x = np.float64(io.imread(path_immagini/"lena.jpg"))
plt.figure(); plt.imshow(x, clim=None, cmap='gray');

#calcolo trasformata normale e shiftata
X = np.fft.fft2(x)
X_shift = np.fft.fftshift(X)

#visualizzazione spettro d'ampiezza e fase
Y = np.log(1+np.abs(X_shift))
plt.figure(); plt.imshow(Y, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));

Z = np.angle(X_shift)
plt.figure(); plt.imshow(Z, clim=[-np.pi,np.pi], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));

#ricostruisco direttamente da quella non shiftata
#N.B. per ricostruire da quella shiftata va usato il comando ifftshift
Xfase = np.exp(1j * np.angle(X))
Xampiezza = np.abs(X) * np.exp(1j*1)
Xcompleta = np.abs(X) * np.exp(1j * np.angle(X))

Yfase = np.real(np.fft.ifft2(Xfase))
Yampiezza = np.real(np.fft.ifft2(Xampiezza))
Ycompleta = np.real(np.fft.ifft2(Xcompleta))

plt.figure(7)
plt.subplot(1,3,1); plt.imshow(Yfase, clim=None, cmap='gray');
plt.subplot(1,3,2); plt.imshow(Yampiezza, clim=None, cmap='gray');
plt.subplot(1,3,3); plt.imshow(Ycompleta, clim=None, cmap='gray');

"1.1.2 ricostruzione con ampiezza e fase dell'immagine rettangolo"

w = np.float64(io.imread(path_immagini/"rettangolo.jpg"))
plt.figure(); plt.imshow(w, clim=None, cmap='gray');

W = np.fft.fft2(w)
W_shift = np.fft.fftshift(W)
W_visual = np.log(1 + np.abs(W_shift))
plt.figure(); plt.imshow(W_visual, clim=None, cmap='gray', extent=(-0.5,+0.5,-0.5,+0.5))

XfaseRect = np.abs(X) * np.exp(1j * np.angle(W))
XampiezzaRect = np.abs(W) * np.exp(1j * np.angle(X))

YfaseRect = np.real(np.fft.ifft2(XfaseRect)) 
YampiezzaRect = np.real(np.fft.ifft2(XampiezzaRect))
plt.figure()
plt.subplot(1,2,1); plt.imshow(YfaseRect, clim=None, cmap='gray');
plt.subplot(1,2,2); plt.imshow(YampiezzaRect, clim=None, cmap='gray');



































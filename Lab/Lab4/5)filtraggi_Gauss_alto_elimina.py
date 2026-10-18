# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab")

    
x = np.float64(io.imread(path_immagini/"lena.jpg"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

"""trasformo"""
X = np.fft.fft2(x)
X = np.fft.fftshift(X)
X_visual = np.log(1+np.abs(X))
plt.figure('trasformata'); plt.imshow(X_visual, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))

"""griglia"""
M,N = x.shape
m = np.fft.fftshift(np.fft.fftfreq(M))
n = np.fft.fftshift(np.fft.fftfreq(N))
l,k = np.meshgrid(n,m)

"""filtro passa basso gaussiano """
# D = np.sqrt(k**2 + l**2)
# sigma = 0.10    
# H = np.exp(-(D**2)/(2*(sigma**2)))
# plt.figure('filtro'); plt.imshow(H, clim=None, cmap='gray', # extent=(-0.5, +0.5, +0.5, -0.5))

"""filtro passa alto ideale"""
# D = np.sqrt(k**2 + l**2)
# D0 = 0.1
# H = (D >= D0)
# plt.figure('filtro'); plt.imshow(H, clim=None, cmap='gray', extent=(-0.5, +0.5, +0.5, -0.5))

""" filtro elimina banda ideale
    N.B IMPORTANTE STIAMO DEFINENDO I PUNTI CHE PASSANO, 
    NON I PUNTI CHE NON PASSANO (cioè I PUNTI CHE NON APPARTENGONO ALL'ANELLO)
    PER QUESTO MOTIVO USO LA OR """
    
D = np.sqrt(k**2 + l**2)
D0 = 0.25
D1 = 0.3
H = (D <= D0) | (D >= D1)
#H = ~(~(D <= D0) & ~(D >= D1))
plt.figure('filtro'); plt.imshow(H, clim=None, cmap='gray', extent=(-0.5, +0.5, +0.5, -0.5))


"""filtro e visualizzo"""
Y = H * X
plt.figure('trasformata filtrata'); plt.imshow(np.log(1+np.abs(Y)), clim=None, 
                                                cmap='gray', extent=(-0.5, +0.5, +0.5, -0.5))

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))
plt.figure('immagine filtrata'); plt.imshow(y, clim=None, cmap='gray')



# def gaussLPF(x, sigma):
#     X = np.fft.fft2(x)
#     X = np.fft.fftshift(X)
    
#     M,N = x.shape
#     m = np.fft.fftshift(np.fft.fftfreq(M))
#     n = np.fft.fftshift(np.fft.fftfreq(N))
#     l,k = np.meshgrid(n,m)
    
#     D = np.sqrt(k**2 + l**2)  
#     H = np.exp(-(D**2)/(2*(sigma**2)))
#     Y = H * X
    
#     return np.real(np.fft.ifft2(np.fft.ifftshift(Y)))

# sigma = 0.13
# y = gaussLPF(x, sigma)
# plt.figure('testo filtrato'); plt.imshow(y, clim=None, cmap='gray')




































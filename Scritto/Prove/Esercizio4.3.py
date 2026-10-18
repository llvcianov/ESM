# -*- coding: utf-8 -*-

import numpy as np
import scipy.ndimage as ndi
import skimage.io as io
from skimage.color import rgb2gray
import skimage.metrics as met
import matplotlib.pyplot as plt
from seg_utils import zero_crossing
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")
plt.close('all')

x1 = np.float64(io.imread(path_immagini/"img1.png"))
plt.figure('originale1'); plt.imshow(x1, clim=None, cmap='gray')

# x2 = np.float64(io.imread(path_immagini/"img2.png"))
# plt.figure('originale2'); plt.imshow(x2, clim=None, cmap='gray')

"filtri di Sobel"
mask1 = ([[-2,-1, 0],
          [-1, 0, 1],
          [ 0, 1, 2]])
          
mask2 = ([[ 0,-1,-2],
          [ 1, 0,-1],
          [ 2, 1, 0]])

S1 = np.array([[-1,-2,-1],
               [ 0, 0, 0],
               [ 1, 2, 1]])

S2 = np.array([[-1,0,1],
               [-2,0,2],
               [-1,0,1]])


d1_x1 = ndi.correlate(x1, mask1, mode='reflect')
#plt.figure('Sobel1'); plt.imshow(d1_x1, clim=None, cmap='gray')

d2_x1 = ndi.correlate(x1, mask2, mode='reflect')


"provo gradiente"
# G = np.sqrt(d1_x1**2 + d2_x1**2)  

# T = 1.2 * np.mean(G)    
# maskbin = G > T
# plt.figure('maschera binaria grad'); plt.imshow(maskbin, clim=None, cmap='gray')
          
"provo varianza"
# var1 = ndi.generic_filter(x1, np.var, (2,2))
# plt.figure('maschera binaria var'); plt.imshow(var1, clim=None, cmap='gray')

"provo laplace"
# l = ndi.gaussian_laplace(x1, 0.5)
# zer = zero_crossing(l)
# plt.figure('maschera binaria laplace'); plt.imshow(zer, clim=None, cmap='gray')

"provo mediano + filtro"
med = ndi.generic_filter(x1, np.median,  (25,25))
plt.figure('mediano'); plt.imshow(med, clim=None, cmap='gray')

# d_med = ndi.correlate(med, mask1)
# plt.figure('maschera derivata mediano'); plt.imshow(d_med,
#                                                     clim=None, cmap='gray')

mas_med = med < 50
plt.figure('mediano_mask'); plt.imshow(mas_med, clim=None, cmap='gray')


# "provo in frequenza"
# X1 = np.fft.fftshift(np.fft.fft2(med))
# plt.figure("trasformata"); plt.imshow(np.log(1+np.abs(X1)), clim=None, cmap='gray',
#                                       extent=(-0.5,+0.5,+0.5,-0.5))

# (M,N) = med.shape
# n = np.fft.fftshift(np.fft.fftfreq(N))
# m = np.fft.fftshift(np.fft.fftfreq(M))
# l,k = np.meshgrid(n,m)

# "cerchio"
# D0 = 0.08
# D = np.sqrt(l**2 + k**2)
# H1 = D > D0


# "striscia obliqua"
# D1 = 0.2  # Larghezza della striscia
# angle = np.pi / 4  # Angolo di inclinazione (45° in questo caso)

# # Equazione della striscia obliqua: |l * cos(angle) + k * sin(angle)| < D0/2
# H2 = np.abs(l * np.cos(angle) + k * np.sin(angle)) < D1 / 2

# H = ~(H1 & H2)

# "eseguo e visualizzo filtraggio"
# Y = H*X1
# plt.figure("filtro"); plt.imshow(np.log(1+np.abs(H*X1)), clim=None, cmap='gray',
#                                   extent=(-0.5,+0.5,+0.5,-0.5))

# "antitrasformo, estraggo la firma e calcolo MSE"
# y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))
# plt.figure("filtrata"); plt.imshow(y, clim=None, cmap='gray',
#                                   extent=(-0.5,+0.5,+0.5,-0.5))























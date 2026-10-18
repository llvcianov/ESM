# -*- coding: utf-8 -*-

import numpy as np
import scipy.ndimage as ndi
import skimage.io as io
from skimage.color import rgb2gray
import skimage.metrics as met
import matplotlib.pyplot as plt
from bitop import bitset
from bitop import bitget
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")
plt.close('all')

"import immagine e firma"
file1 = str(path_immagini/"upupa.y")
x1 = np.fromfile(file1, np.uint8)
x1 = x1.reshape(256,512)
plt.figure('originale'); plt.imshow(x1, clim=None, cmap='gray')

file2 = str(path_immagini/"firma.y")
x2 = np.fromfile(file2, np.uint8)
x2 = x2.reshape(256,512)
plt.figure('firma'); plt.imshow(x2, clim=None, cmap='gray')

"inserisco la firma nel bitplane meno significativo"
z = bitset(x1, 1, x2)

"comprimo con jpg"
io.imsave("compressa.jpg", z, quality=100)

"rileggo l'immagine e visualizzo la firma"
w = io.imread("compressa.jpg")
firmac = bitget(w, 0)
plt.figure("firma compressa"); plt.imshow(firmac, clim=None, cmap='gray')

"grafico da fare"



def filtra(z, x2, D0):
    "eseguo filtraggio passa basso sull'immagine con la firma"
    Z = np.fft.fftshift(np.fft.fft2(z))
    
    (M,N) = z.shape
    n = np.fft.fftshift(np.fft.fftfreq(N))
    m = np.fft.fftshift(np.fft.fftfreq(M))
    l,k = np.meshgrid(n,m)
    
    D = np.sqrt(l**2 + k**2)
    H = D < D0
    
    Y = H*Z
    
    "antitrasformo, estraggo la firma e calcolo MSE"
    y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))
    y = np.uint8(y)
    
    yfirma = bitget(y, 1)

    return met.mean_squared_error(x2, yfirma)
    
    
    
asseX = [0.2, 0.3, 0.4]
asseY = []

for i in range (3):
    asseY.append(filtra(z, x2, asseX[i]))
    
plt.figure('grafico')
plt.plot(asseX, asseY, "-ro")
plt.grid(True)
plt.xlabel('Frequenza di cut off')
plt.ylabel('MSE')


# "CODICE FUNZIONE"
# "eseguo filtraggio passa basso sull'immagine con la firma"
# Z = np.fft.fftshift(np.fft.fft2(z))
# plt.figure("trasformata"); plt.imshow(np.log(1+np.abs(Z)), clim=None, cmap='gray',
#                                       extent=(-0.5,+0.5,+0.5,-0.5))

# (M,N) = z.shape
# n = np.fft.fftshift(np.fft.fftfreq(N))
# m = np.fft.fftshift(np.fft.fftfreq(M))
# l,k = np.meshgrid(n,m)

# D0 = 0.2
# D = np.sqrt(l**2 + k**2)
# H = D < D0
# plt.figure("filtro"); plt.imshow(H, clim=None, cmap='gray',
#                                  extent=(-0.5,+0.5,+0.5,-0.5))

# Y = H*Z

# "antitrasformo, estraggo la firma e calcolo MSE"
# y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))
# y = np.uint8(y)
# plt.figure("antitrasformata"); plt.imshow(y, clim=None, cmap='gray')

# yfirma = bitget(y, 0)

# MSE = met.mean_squared_error(x2, yfirma)
# print(MSE)












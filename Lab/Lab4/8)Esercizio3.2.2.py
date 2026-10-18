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

"""Pattern di Moirè"""

x = np.float64(io.imread(path_immagini/"car.tif"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray'); 

X = np.fft.fftshift(np.fft.fft2(x))
plt.figure('trasformata'); plt.imshow(np.log(1+np.abs(X)), clim=None,
                                      cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))

(M,N) = x.shape
n = np.fft.fftshift(np.fft.fftfreq(N))
m = np.fft.fftshift(np.fft.fftfreq(M))
l,k = np.meshgrid(n, m)

B = 0.05
B1 = 0.08
D1 = np.sqrt((l+0.17)**2 + (k+0.16)**2)
H1 = D1 > B1

D2 = np.sqrt((l+0.156)**2 + (k-0.17)**2)
H2 = D2 > B1

D3 = np.sqrt((l-0.165)**2 + (k+0.17)**2)
H3 = D3 > B1

D4 = np.sqrt((l-0.18)**2 + (k-0.155)**2)
H4 = D4 > B1

D5 = np.sqrt((l+0.172)**2 + (k+0.323)**2)
H5 = D5 > B

D6 = np.sqrt((l+0.156)**2 + (k-0.336)**2)
H6 = D6 > B

D7 = np.sqrt((l-0.165)**2 + (k+0.337)**2)
H7 = D7 > B

D8 = np.sqrt((l-0.18)**2 + (k-0.321)**2)
H8 = D8 > B

H = H1 & H2 & H3 & H4 & H5 & H6 & H7 &H8

Y = H * X
plt.figure('filtro'); plt.imshow(np.log(1+np.abs(Y)), clim=None,
                                      cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))
plt.figure('immagine filtrata'); plt.imshow(y, clim=None, cmap='gray')
















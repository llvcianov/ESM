# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")
plt.close('all')


x = np.float64(io.imread(path_immagini/"anelli.tif"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

X = np.fft.fft2(x)
X = np.fft.fftshift(X)
plt.figure('trasformata'); plt.imshow(np.log(1+np.abs(X)), clim=None,
                                      cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))

(M,N) = x.shape
n = np.fft.fftshift(np.fft.fftfreq(N))
m = np.fft.fftshift(np.fft.fftfreq(M))
l,k = np.meshgrid(n,m)

#filtro circolare
nu = 0.2; 
mu = 0.04
B = 0.02; 
D1 = np.sqrt((k-mu)**2 + l**2)
D2 = np.sqrt((k+mu)**2 + l**2)
H = (D1 > B) & (D2 > B)

# plt.figure();
# plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
# plt.title('Riposta in frequenza del filtro circolare');

Y = H * X
plt.figure()
plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('trasformata filtrata con circolare');

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))
plt.figure(); plt.imshow(y, clim=None, cmap='gray');
plt.title('Immagine filtrata con circolare');


#filtro rettangolare da fare
centro = 0
spessore = 0.003
B = 0.01
D = np.sqrt(l**2 + k**2)
S = np.abs(l-centro)
H2 = ~((D > B) & (S < spessore))

# plt.figure();
# plt.imshow(H2, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
# plt.title('Riposta in frequenza del filtro rettangolare');

Z = H2 * X
plt.figure()
plt.imshow(np.log(1+np.abs(Z)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('trasformata filtrata con rettangolare');

z = np.real(np.fft.ifft2(np.fft.ifftshift(Z)))
plt.figure(); plt.imshow(z, clim=None, cmap='gray');
plt.title('Immagine filtrata con rettangolare');















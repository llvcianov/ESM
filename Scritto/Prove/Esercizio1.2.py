# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io
import skimage.exposure as exp
from skimage.color import rgb2yuv, yuv2rgb, rgb2hsv, hsv2rgb
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")

x = np.float64(io.imread(path_immagini/"pears_noise.png"))/255
plt.figure('rumorosa'); plt.imshow(x)

x_clean = np.float64(io.imread(path_immagini/"pears.png"))/255
plt.figure('originale'); plt.imshow(x_clean)

"converto in yuv ed estraggo la luminanza"
x_yuv = rgb2yuv(x)
y = x_yuv[:,:,0]
# x_yuv = rgb2hsv(x)
# y = x_yuv[:,:,2]



"trasformo e visualizzo"
Y = np.fft.fftshift(np.fft.fft2(y))
plt.figure('trasformata'); plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray',
                                      extent=(-0.5,+0.5,+0.5,-0.5))

"filtro"
(M,N) = y.shape
n = np.fft.fftshift(np.fft.fftfreq(N))
m = np.fft.fftshift(np.fft.fftfreq(M))
l,k = np.meshgrid(n,m)

a = 0.1
B0 = 0.02
B1 = 0.002
B2 = 0.06
B3 = 0.01

""" la tecnica è descrivere i punti interni alle
    zone nere (filtri) es esterni al centro(che voglio mantenere. 
    Fare le due condizioni in and ed infine negare il tutto """
    
D1 = np.sqrt((l-a)**2 + (k+a)**2) < B0
D2 = np.sqrt((l+a)**2 + (k-a)**2) < B0
D3 = np.sqrt(l**2 + k**2) > B2

S1 = np.abs(l-a) < B1
S2 = np.abs(k-a) < B1
S3 = np.abs(l+a) < B1
S4 = np.abs(k+a) < B1

H = ~ ((D1 | D2 | S1 | S2 | S3 | S4 ) & D3)

plt.figure('filtro'); plt.imshow(np.log(1+np.abs(H*Y)), clim=None, cmap='gray',
                                      extent=(-0.5,+0.5,+0.5,-0.5))

y_filt = np.float64(np.fft.ifft2(np.fft.ifftshift(H*Y)))

"ricompongo"

x_yuv_filt = np.stack((y_filt, x_yuv[:,:,1], x_yuv[:,:,2]), -1)
x_filt = yuv2rgb(x_yuv_filt)
plt.figure('filtrata'); plt.imshow(x_filt)

"enhancement, trasformo in HSV e aumento saturazione e intensità"
x_hsv = rgb2hsv(x_filt)

S = x_hsv[:,:,1] * 2
V = x_hsv[:,:,2] * 1.3

x_hsv[:,:,1] = S
x_hsv[:,:,2] = V

x_enhanc = hsv2rgb(x_hsv)
plt.figure('enhancement'); plt.imshow(x_enhanc)
























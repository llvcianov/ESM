# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from skimage.color import rgb2hsv, hsv2rgb, rgb2yuv, yuv2rgb
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")


"""filtraggio RGB completo separato"""

# x = io.imread(path_immagini/"Azzurro.jpg")
# x = np.float64(x)/255 # convertiamo nel range [0,1]
# plt.figure('originale'); plt.imshow(x)

# #qui devo inserire un 1 alla fine perchè così indico di usare un singolo
# #pixel lungo l'asse dei colori. Il risulttao è che il filtraggio avviene
# #separatamente lungo i 3 assi
# y = ndi.uniform_filter(x, (7,7,1))
# plt.figure('smooth'); plt.imshow(y)

"""filtraggio RGB a singola componente"""

# x = io.imread(path_immagini/"fiori.jpg")
# x = np.float64(x)/255 # convertiamo nel range [0,1]
# plt.figure('originale'); plt.imshow(x)

# #filtro RGB
# y = ndi.uniform_filter(x, (25,25,1))
# plt.figure('smoothRGB'); plt.imshow(y)

# # #filtro YUV
# # z = rgb2yuv(x)
# # zY = z[:,:,0]
# # zU = z[:,:,1]
# # zV = z[:,:,2]

# # zY_filt = ndi.uniform_filter(zY, (25,25))
# # z_filt_yuv = np.stack((zY_filt, zU, zV), -1)
# # z_filt = yuv2rgb(z_filt_yuv)

# # plt.figure('smoothYUV'); plt.imshow(z_filt)

# #filtro HSV
# z = rgb2hsv(x)
# zH = z[:,:,0]
# zS = z[:,:,1]
# zV = z[:,:,2]

# zV_filt = ndi.uniform_filter(zV, (25,25))
# z_filt_hsv = np.stack((zH, zS, zV_filt), -1)
# z_filt = hsv2rgb(z_filt_hsv)

# plt.figure('smoothHSV'); plt.imshow(z_filt)


"""enhancement a colori"""
x = io.imread(path_immagini/"fiori.jpg")
x = np.float64(x)/255 # convertiamo nel range [0,1]
plt.figure('originale'); plt.imshow(x)

#maschera per il laplaciano in 3 dimensioni
h = np.array([[0 ,-1, 0],
              [-1, 4,-1],
              [0 ,-1, 0]], np.float64) # maschera 2D

h3 = np.expand_dims(h, -1) # maschera 3D

y = ndi.correlate(x, h3, mode='reflect')
plt.figure('sharpeningRGB'); plt.imshow(y)

z = rgb2hsv(x)
zH = z[:,:,0]
zS = z[:,:,1]
zV = z[:,:,2]

zV_filt = ndi.correlate(zV, h, mode='reflect')

z_filt_hsv = np.stack((zH, zS, zV_filt), -1)
z_filt = hsv2rgb(z_filt_hsv)

plt.figure('sharpHSV'); plt.imshow(z_filt)

















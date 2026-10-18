# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from skimage.color import rgb2hsv, hsv2rgb
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")
plt.close('all')

"""Accappatoio Rosso"""
x = io.imread(path_immagini/"Azzurro.jpg")
x = np.float64(x)/255 # convertiamo nel range [0,1]
plt.figure(); plt.imshow(x)

x_hsv = rgb2hsv(x)
H = x_hsv[:,:,0]
S = x_hsv[:,:,1]
V = x_hsv[:,:,2]

plt.subplot(1,3,1); plt.imshow(H, clim=None, cmap='gray'); plt.title('Hue')
plt.subplot(1,3,2); plt.imshow(S, clim=None, cmap='gray'); plt.title('Saturation')
plt.subplot(1,3,3); plt.imshow(V, clim=None, cmap='gray'); plt.title('Value')

msk = (H < 0.61) & (S > 0.4) & (V > 0.5)
plt.figure('maschera'); plt.imshow(msk, clim=None, cmap='gray')

H[msk] = 0

rossoHSV = np.stack((H,S,V), -1)
rossoRGB = hsv2rgb(rossoHSV)
plt.figure('Azzurro rosso'); plt.imshow(rossoRGB)












# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi 
import skimage.io as io
from skimage.color import rgb2hsv, hsv2rgb
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

""" Filtraggio in frequenza nella banda I"""

x = np.float64(io.imread(path_immagini/"paesaggio.jpg"))/255
plt.figure('originale'); plt.imshow(x)

R = x[:,:,0]
G = x[:,:,1]
B = x[:,:,2]

A1 = A2 = 0.7020
A3 = 0.7098
t0 = 0.1

K = np.minimum((R/A1), (G/A2), (B/A3))
dark = ndi.generic_filter(K, np.min, (15,15))

t = 1 - (0.95 * dark)

Ry = ((R - A1)/(np.maximum(t, t0))) + A1
Gy = ((G - A2)/(np.maximum(t, t0))) + A2
By = ((B - A3)/(np.maximum(t, t0))) + A3

output = np.stack((Ry, Gy, By), -1)
plt.figure('output'); plt.imshow(output)































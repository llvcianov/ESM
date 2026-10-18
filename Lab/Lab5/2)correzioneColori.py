# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from skimage.color import rgb2hsv, hsv2rgb
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab")

"Lavoro in RGB quindi non mantengo i rapporti e le relazioni tra colori"
x = io.imread(path_immagini/"montagna.jpg")
x = np.float64(x)/255 # convertiamo nel range [0,1]
y = x ** 0.5
plt.figure();
plt.subplot(1,2,1); plt.imshow(x); plt.title('Immagine orignale');
plt.subplot(1,2,2); plt.imshow(y); plt.title('Immagine elaborata_rgb');

"Lavoro in HSI/HSV quindi mantengo i rapporti e le relazioni tra colori"
z = rgb2hsv(x)
H = z[:,:,0]
S = z[:,:,1]
V = z[:,:,2]
V = V **0.6
z_hsv = np.stack((H,S,V), -1)
z = hsv2rgb(z_hsv)
plt.figure()
plt.subplot(1,2,1); plt.imshow(x); plt.title('Immagine orignale');
plt.subplot(1,2,2); plt.imshow(z); plt.title('Immagine elaborata_hsv');


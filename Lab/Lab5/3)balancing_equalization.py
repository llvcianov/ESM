# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import skimage.exposure as exp
import scipy.ndimage as ndi
from skimage.color import rgb2hsv, hsv2rgb
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

"""Equalization"""
x = io.imread(path_immagini/"volto.tiff")
x = np.float64(x)/255 
plt.figure("originale"); plt.imshow(x)
xR = x[:,:,0]
xG = x[:,:,1]
xB = x[:,:,2]
newR = exp.equalize_hist(xR)
newG = exp.equalize_hist(xG)
newB = exp.equalize_hist(xB)
newx = np.stack((newR,newG,newB),-1)
plt.figure("egualizzatoRGB"); plt.imshow(newx)

y = rgb2hsv(x)
yH = y[:,:,0]
yS = y[:,:,1]
yV = y[:,:,2]
newV = exp.equalize_hist(yV)
newy = np.stack((yH,yS,newV),-1)
yrgb = hsv2rgb(newy)
plt.figure("egualizzatoHSV"); plt.imshow(yrgb)


"""Balancing"""
# x = io.imread(path_immagini/"foto.jpg")
# x = np.float64(x)/255 # convertiamo nel range [0,1]
# plt.figure('originale'); plt.imshow(x)

# x_cmy = my.rgb2cmy(x)
# C = x_cmy[:,:,0]
# M = x_cmy[:,:,1]
# Y = x_cmy[:,:,2]
# C = C ** 1.5
# new_cmy = np.stack((C,M,Y), -1)
# y = my.cmy2rgb(new_cmy)

# plt.figure('tolto ciano'); plt.imshow(y)























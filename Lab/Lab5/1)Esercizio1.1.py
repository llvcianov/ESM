# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.color import rgb2hsv, hsv2rgb
import scipy.ndimage as ndi
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

"converti in CMY, N.B QUESTO EQUIVALE AL NEAGTIVO)"""
# def rgb2cmy(x):
#     C = 1 - x[:,:,0]
#     M = 1 - x[:,:,1]
#     Y = 1 - x[:,:,2]
#     return np.stack((C,M,Y),-1)

"converti in CMYK"
def rgbcmyk(x):
    C = 1 - x[:,:,0]
    M = 1 - x[:,:,1]
    Y = 1 - x[:,:,2]
    K = np.minimum(C,M,Y)
    newC = (C - K)
    newM = (M - K)
    newY = (Y - K)
    
    return np.stack((newC,newM,newY,K),-1)
    
    
x = np.float64(io.imread(path_immagini/"fragole.jpg"))/255
plt.figure('originale'); plt.imshow(x)

y = my.rgb2cmy(x)
plt.figure('convertita in CMYK'); plt.imshow(y)

"converti in HSI"
z = rgb2hsv(x)
plt.figure('immagine convertita in HSV'); plt.imshow(z)












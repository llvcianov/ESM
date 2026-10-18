# -*- coding: utf-8 -*-

import skimage.morphology as morph
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\immagini_lab_morfologia\DIP3E_Original_Images_CH09")

"""DA RIVEDERE MA PROB INUTILE PER LAPROVA"""
"""Provo a cercare oggetti tondi"""
x = np.float64(io.imread(path_immagini/"forme.tif"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

S1 = morph.square(55)
S2 = 1 - S1

#S1 = np.array([[0,0,0],[0,1,1],[0,1,0]], np.bool)
#S2 = np.array([[1,1,1],[1,0,0],[1,0,0]], np.bool)

C1 = morph.binary_erosion(x,S1)
C2 = morph.binary_erosion(np.logical_not(x),S2)
C = np.logical_and(C1,C2)

plt.figure('hittato'); plt.imshow(C, clim=None, cmap='gray')
# -*- coding: utf-8 -*-

from skimage.feature import local_binary_pattern
import myLibreria as my
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab")
plt.close('all')

"import delle tessiture"
brick = np.float64(io.imread(path_immagini/"brick.png"))
#plt.figure('brick'); plt.imshow(brick, clim=None, cmap='gray');

grass = np.float64(io.imread(path_immagini/"grass.png"))
#plt.figure('grass'); plt.imshow(grass, clim=None, cmap='gray');

gravel = np.float64(io.imread(path_immagini/"gravel.png"))
plt.figure('gravel'); plt.imshow(gravel, clim=None, cmap='gray');

"calcolo il LBP delle tessiture"
P = 8
R = 1

brick_hist = my.extract_feat(brick, P, R)

grass_hist = my.extract_feat(grass, P, R)

gravel_hist = my.extract_feat(gravel, P, R)

"import immagini da classificare"
x1 = np.float64(io.imread(path_immagini/"img1.jpg"))
#plt.figure('img1'); plt.imshow(x1, clim=None, cmap='gray');

x2 = np.float64(io.imread(path_immagini/"img2.jpg"))
#plt.figure('img2'); plt.imshow(x2, clim=None, cmap='gray');

x3 = np.float64(io.imread(path_immagini/"img3.jpg"))
plt.figure('img3'); plt.imshow(x3, clim=None, cmap='gray');

"""calcolo distanza SAD + classificazione
    sto a tutti gli effetti usando un knn molto semplificato manuale"""
h = my.extract_feat(x3, P ,R)

d_brick = np.sum(np.abs(h - brick_hist))
d_grass = np.sum(np.abs(h - grass_hist))
d_gravel = np.sum(np.abs(h - gravel_hist))

if (d_brick<d_grass) & (d_brick<d_gravel):
    plt.title('it is brick')
elif (d_gravel<d_brick) & (d_gravel<d_grass):
    plt.title('it is gravel')
else:
    plt.title('it is grass')













































# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage.exposure as exp
from pathlib import Path
import myLibreria as my
import skimage.transform as tras

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

"""
Ridimensionamento versione basic con rescale,
devo specificare parametro di riscalamento ed ordine di interpolazione

"""

# x = io.imread(path_immagini/"lena.jpg")
# x = np.float64(x)
# plt.figure("originale");plt.imshow(x,clim=[0,255],cmap='gray');

# y = x[::2,::2]
# plt.figure("decimazione");plt.imshow(y,clim=[0,255],cmap='gray');

# z = tras.rescale(x, 0.5, order=2)
# plt.figure("espansione");plt.imshow(z,clim=[0,255],cmap='gray');


"""
Ridimensionamento con warp

"""

# x = io.imread(path_immagini/"lena.jpg")
# I = np.float32(x)

# x = I[252:277,240:290];
# (M,N) = x.shape

# w = I[239:289, 215:315]

# A = np.array([[0.5,0,  0],
#               [0,  0.5,0],
#               [0,  0,  1]], dtype=np.float32)

# """ uso la funzione warp passando la matrice di trasformazione,
#     devo specificare anche le dimensioni di output in questo caso"""
    
# y1 = tras.warp(x, A, output_shape=(2*M,2*N), order = 0)
# y2 = tras.warp(x, A, output_shape=(2*M,2*N), order = 1)
# y3 = tras.warp(x, A, output_shape=(2*M,2*N), order = 3)

# plt.subplot(4,1,1);
# plt.imshow(w,clim=[0,255],cmap='gray'); plt.title('taglio');
# plt.subplot(4,1,2);
# plt.imshow(y1,clim=[0,255],cmap='gray'); plt.title('interpolazione nearest');
# plt.subplot(4,1,3);
# plt.imshow(y2,clim=[0,255],cmap='gray'); plt.title('interpolazione bilinear');
# plt.subplot(4,1,4);
# plt.imshow(y3,clim=[0,255],cmap='gray'); plt.title('interpolazione bicubic');


"""
Traslazioni con warp

"""

x = np.float32(io.imread(path_immagini/"lena.jpg"))
#n.b. matrice utilizzata è la trasposta di quella vista in teoria

"""sposta di 100 pixel a destra e di 50 in basso"""

A = np.array([[1,0,-100],
              [0,1,-50 ],
              [0,0,1  ]], dtype=np.float32)

y = tras.warp(x, A, order = 1, cval = 45)

plt.subplot(1,2,1);
plt.imshow(x,clim=[0,255],cmap='gray'); plt.title('originale');
plt.subplot(1,2,2);
plt.imshow(y,clim=[0,255],cmap='gray'); plt.title('traslata');


"""
Rotazioni con warp e con transform.rotate

"""
# from skimage.transform import rotate

# x = np.float32(io.imread(path_immagini/"lena.jpg"))

# A = np.array([[ np.cos(np.pi/4), np.sin(np.pi/4), 0],
#               [-np.sin(np.pi/4), np.cos(np.pi/4), 0],
#               [        0,               0,        1]], dtype=np.float32)

# y = tras.warp(x, A, order = 1)

# plt.subplot(1,3,1);
# plt.imshow(x,clim=[0,255],cmap='gray'); plt.title('originale');
# plt.subplot(1,3,2);
# plt.imshow(y,clim=[0,255],cmap='gray'); plt.title('ruotata');

# z = rotate(x, -45)
# plt.subplot(1,3,3);
# plt.imshow(z,clim=[0,255],cmap='gray'); plt.title('ruotata');



















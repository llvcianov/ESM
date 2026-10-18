# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from pathlib import Path
import myLibreria

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

"""
Offset positivo

"""
x = io.imread(path_immagini/"granelli.jpg")
x = np.float64(x)

plt.figure('granelli')
plt.subplot(1,2,1); plt.imshow(x, clim=(0,255), cmap='gray');plt.colorbar()
plt.subplot(1,2,2); plt.hist(x.flatten(), bins = 256); plt.xlim((0,255))

xoff = x - 50
plt.figure('granelli_offset_xlim')
plt.subplot(1,2,1);plt.imshow(xoff, clim = (0,255), cmap='gray');plt.colorbar()
plt.subplot(1,2,2);plt.hist(xoff.flatten(), bins = 256); plt.xlim((0,255))


"""
Offset negativo

"""
# y = io.imread(path_immagini/"vista_aerea.jpg")
# y = np.float64(y)

# plt.figure('vista_aerea')
# plt.subplot(3,2,1); plt.imshow(y, clim=[0,255], cmap='gray'); plt.colorbar()
# plt.subplot(3,2,2); plt.hist(y.flatten(), bins=256); plt.xlim((0,255))

# yoff = y - 150
# plt.subplot(3,2,3); plt.imshow(yoff, clim=[0,255], cmap='gray'); plt.colorbar()
# plt.subplot(3,2,4); plt.hist(yoff.flatten(), bins=256); plt.xlim((0,255))

# mask = yoff < 0 
# yoff[mask] = 0
# plt.subplot(3,2,5); plt.imshow(mask); plt.colorbar()









 






















#codice full scale istogram skretch
# def fshs(x):
#     x_min = np.min(x)
#     x_max = np.max(x)
#     y = 255*(x-x_min)/(x_max-x_min)
#     return y
    

# x = io.imread('granelli.jpg')
# x = np.float64(x)

# plt.figure(1)
# plt.imshow(x, clim = [0,255], cmap = 'gray')

# y = fshs(x)

# plt.figure(2)
# plt.imshow(y, None, cmap = 'gray')

# z = x**3




#codice enhancement

# x = io.imread('filamento.jpg')
# x = np.float64(x)

# plt.figure(1)
# plt.imshow(x, clim = [0,255], cmap = 'gray')
# plt.title('input')

# med = np.mwan(x) #media globale
# dev = np.std(x) #std globale
# MED = ndi.generic_filter(x, np.std)

# mask = (MED<=0.4*med)) & (DEV<=0.4*dev)) & (DEV>=0.02*dev)
    
# y = mask*(4*x) + (1-mask)*x
# plt.figure(1)
# plt.imshow(y, clim = None= 'gray')
# plt.title('enhancement')



# #codice bit plane
# from bitop import bitget
# x = io.imread('frattale.jpg')
# # x = np.float64(x)

# # plt.figure(1)
# # plt.imshow(x, clim = [0,255], cmap = 'gray')
# # plt.title('input')

# for index in range(8):
#     B = bitget(x, index) # estrazione bit-plane pi`u significativo
#     plt.subplot(2,4,index+1)
#     plt.figure(index + 2)
#     plt.imshow(B, clim=[0,1], cmap='gray') # visualizzazione del bit-plane

#codice marchio
# from bitop import bitset

# x = np.fromfile('lena.y', np.uint8)
# x = np.reshape(x, (512,512))
# x = x[0:350, 0:350]

# plt.figure(1)
# plt.imshow(x, clim = [0,255], cmap = 'gray')
# plt.title('input')

# m = np.fromfile('marchio.y', np.uint8)
# m = np.reshape(m, (350,350))

# plt.figure(2)
# plt.imshow(m, clim = None, cmap = 'gray')
# plt.title('marchio')

# y = bitset(x,2,m)

# plt.figure(3)
# plt.imshow(y, clim = None, cmap = 'gray')
# plt.title('output')

#codice ridimensionamento
# from skimage.transform import warp
# x = np.float32(io.imread('lena.jpg'))
# x = x[252:277,240:290];
# M = x.shape[0]; N = x.shape[1]

# A = np.array([ [0.5,0,0], [0,0.5,0], [0,0,1]], dtype=np.float32)
# y1 = warp(x, A, output_shape=(2*M,2*N), order = 0)
# y2 = warp(x, A, output_shape=(2*M,2*N), order = 1)
# y3 = warp(x, A, output_shape=(2*M,2*N), order = 3)

# plt.subplot(3,1,1);
# plt.imshow(y1,clim=[0,255],cmap='gray'); plt.title('interpolazione nearest');
# plt.subplot(3,1,2);
# plt.imshow(y2,clim=[0,255],cmap='gray'); plt.title('interpolazione bilinear');
# plt.subplot(3,1,3);
# plt.imshow(y3,clim=[0,255],cmap='gray'); plt.title('interpolazione bicubic');

#codice rotazione
# x = np.float32(io.imread('lena.jpg'))
# A = np.array([ [1,0,100], [0,1,50], [0,0,1]], dtype=np.float32)
# y = warp(x, A, order = 1)
# plt.subplot(1,2,1);
# plt.imshow(x,clim=[0,255],cmap='gray'); plt.title('originale');
# plt.subplot(1,2,2);
# plt.imshow(y,clim=[0,255],cmap='gray'); plt.title('traslata');
































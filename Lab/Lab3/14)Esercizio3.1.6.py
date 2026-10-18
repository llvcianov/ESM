# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
import pathlib as path
import myLibreria as my

path_immagini = path.Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

x = np.float64(io.imread(path_immagini/"tetto.png"))
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

V = np.array([[0,-1,0],
              [0, 1,0],
              [0, 0,0]])

H = np.array([[0, 0,0],
              [-1,1,0],
              [0, 0,0]])

D1 = np.array([[-1,0,0],
               [ 0,1,0],
               [ 0,0,0]])

D2 = np.array([[0,0,-1],
               [0,1, 0],
               [0,0, 0]])

"""calcolo derivate"""
filtro_V = ndi.correlate(x, V, mode = 'reflect')
filtro_H = ndi.correlate(x, H, mode = 'reflect')
filtro_D1 = ndi.correlate(x, D1, mode = 'reflect')
filtro_D2 = ndi.correlate(x, D2, mode = 'reflect')

"""calcolo medie dei valori al quadrato"""
QV = ndi.uniform_filter((filtro_V)**2, (5,5), mode='reflect')
QH = ndi.uniform_filter((filtro_H)**2, (5,5), mode='reflect')
QD1 = ndi.uniform_filter((filtro_D1)**2, (5,5), mode='reflect')
QD2 = ndi.uniform_filter((filtro_D2)**2, (5,5), mode='reflect')

"""determino l'immagine con i valori minimi tra le 4"""
Qmin = np.minimum.reduce([QV, QH, QD1, QD2])

""" determino il massimo su finestre scorrevoli e creo la mappa """
MQmin = ndi.generic_filter(Qmin, np.max, (3,3), mode = 'reflect')

#mappa = np.logical_and((MQmin > 20), MQmin == Qmin )
mappa = (MQmin > 20) & (MQmin == Qmin)
plt.figure('mappa'); plt.imshow(mappa, clim=None, cmap='gray')



































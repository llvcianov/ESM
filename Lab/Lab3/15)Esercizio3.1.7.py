# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
import pathlib as path
import myLibreria as my

path_immagini = path.Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

def medie_diff(block):
    
    block = block.reshape((7,7))
    
    mask1 = (np.array([[0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [1,1,1,1,1,1,1],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0]]) > 0)

    mask2 = (np.array([[0,0,0,1,0,0,0],
                       [0,0,0,1,0,0,0],
                       [0,0,0,1,0,0,0],
                       [0,0,0,1,0,0,0],
                       [0,0,0,1,0,0,0],
                       [0,0,0,1,0,0,0],
                       [0,0,0,1,0,0,0]]) > 0) 

    mask3 = (np.array([[1,0,0,0,0,0,0],
                       [0,1,0,0,0,0,0],
                       [0,0,1,0,0,0,0],
                       [0,0,0,1,0,0,0],
                       [0,0,0,0,1,0,0],
                       [0,0,0,0,0,1,0],
                       [0,0,0,0,0,0,1]]) > 0) 

    mask4 = (np.array([[0,0,0,0,0,0,1],
                       [0,0,0,0,0,1,0],
                       [0,0,0,0,1,0,0],
                       [0,0,0,1,0,0,0],
                       [0,0,1,0,0,0,0],
                       [0,1,0,0,0,0,0],
                       [1,0,0,0,0,0,0]])>0) 
    
    """ per ogni maschera calcolo la media dei valori solo nelle posizioni con gli 1
        e solo nelle posizioni con gli 0.
        Valuto poi la differenza tra questi due valori"""
        
    media_mask1_1 = np.mean(block[mask1])
    media_mask1_0 = np.mean(block[np.logical_not(mask1)])
    diff1 = media_mask1_1 - media_mask1_0
    
    media_mask2_1 = np.mean(block[mask2])
    media_mask2_0 = np.mean(block[np.logical_not(mask2)])
    diff2 = media_mask2_1 - media_mask2_0
    
    media_mask3_1 = np.mean(block[mask3])
    media_mask3_0 = np.mean(block[np.logical_not(mask3)])
    diff3 = media_mask3_1 - media_mask3_0
    
    media_mask4_1 = np.mean(block[mask4])
    media_mask4_0 = np.mean(block[np.logical_not(mask4)])
    diff4 = media_mask4_1 - media_mask4_0
    
    return np.min([diff1, diff2, diff3, diff4])


x = np.float64(io.imread(path_immagini/"retina.tif"))/255
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

G = x[:,:,1]
plt.figure('banda verde'); plt.imshow(G, clim=None, cmap='gray')

x_filt = ndi.generic_filter(G, medie_diff, (7,7), mode='reflect')
plt.figure('filtrato'); plt.imshow(x_filt, clim=None, cmap='gray')

T = -5
mask = x_filt > -5/255 #perchè lo devo fare
plt.figure('mappa'); plt.imshow(mask, clim=None, cmap='gray')
























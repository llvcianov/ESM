# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage.exposure as exp
from pathlib import Path
from bitop import bitget
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

x = io.imread(path_immagini/"barbara.gif")
y = np.float64(x)
my.vediIstogrammaStretchato(y, 256)


def vedi_bit_plane(x):
    """
    Estrae i bit plane della matrice immagine in input
    Input: matrice immagine
    Return: matrice contenente le matrici bitplane
    
    """
    (M,N) = x.shape
    """struttura per gli 8 bit plane"""
    bitplane = np.zeros((M,N,8), dtype=x.dtype)
    plt.figure()
    for i in range(8):
        bitplane[:,:,i] = bitget(x, i)
        plt.subplot(2,4,i+1); plt.imshow(bitget(x,i), clim=[0,1], cmap='gray')
        
    return bitplane

my.vedi_bit_plane(x)


















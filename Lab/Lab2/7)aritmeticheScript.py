# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage.exposure as exp
from pathlib import Path
from bitop import bitget
from bitop import bitset
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

x = io.imread(path_immagini/"frattale.jpg")
y = np.float64(x)
my.vediIstogrammaStretchato(y, 256)

(M,N) = x.shape
m = np.zeros((M,N), x.dtype)

""" creo una copia di x in cui pongo a zero i 4 bit plane meno significativi"""
z = np.copy(x)
for i in range(4):
    z = bitset(z, i, m)
    
my.vedi_bit_plane(z)

z = np.float64(z)
my.vediIstogrammaStretchato(z, 256)

"""effettuo sottrazione per notare le differenze"""
d = x - z
my.vediIstogrammaStretchato(d, 256)




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

"""
Esercizio 1

"""
x = io.imread(path_immagini/"lena.jpg")
y = np.float64(x)
my.vediIstogrammaStretchato(y, 256)

"""creo matrice di zeri con dimensioni e tipo di x"""
(M,N) = x.shape
m = np.zeros((M,N), x.dtype)

"""assegno la matrice al bitplane di indice 3"""
z = bitset(x, 3, m)
my.vedi_bit_plane(z)

z = np.float64(z)
my.vediIstogrammaStretchato(z, 256)

"""
Esercizio 2

"""

""" l'immagine è .y quindi devo specificare tipo nella lettura ed effettuare 
     il reshape per visualizzarla correttamente"""
     
file1 = str(path_immagini/"lena.y")
x = np.fromfile(file1, np.uint8)
x = np.reshape(x, (512,512))
x = x[0:350,0:350]

file2 = str(path_immagini/"marchio.y")
m = np.fromfile(file2, np.uint8)
m = np.reshape(m, (350,350))

y = bitset(x, 2, m)
my.vedi_bit_plane(y)

x = np.float64(x)
y = np.float64(y)
my.vediIstogrammaStretchato(x, 256)
my.vediIstogrammaStretchato(y, 256)












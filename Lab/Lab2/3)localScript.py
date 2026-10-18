# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage.exposure as exp
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

"""
Statistiche locali

"""
x = io.imread(path_immagini/"filamento.jpg")
x = np.float64(x)
my.vediIstogrammaStretchato(x, 256)


"""calcolo media e deviazione standard locale"""
MED = ndi.generic_filter(x, np.mean, (3,3), mode = 'reflect')
#my.vediIstogrammaStretchato(MED, 256)
DEV = ndi.generic_filter(x, np.std, (3,3), mode = 'reflect')
#my.vediIstogrammaStretchato(DEV, 256)

"""calcolo media e deviazione standard globale"""
M = np.mean(x)
D = np.std(x)

""" maschera co statistiche locali, la zona è in ombra quindi ha una media
    minore della globale. E' a basso contrasto ma non tanto da essere uniforme"""


mask = ((MED <= 0.4 * M) & (DEV <= 0.4 * D) & (DEV >= 0.02 * D))

y = mask * (4*x) + (1-mask)*x
my.vediIstogrammaStretchato(y, 256)





















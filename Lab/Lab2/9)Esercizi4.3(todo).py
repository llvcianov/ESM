# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.exposure import equalize_hist
import skimage.transform as tf
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

#TODO ultimi esercizi in Ex2, vedi anche Script 11


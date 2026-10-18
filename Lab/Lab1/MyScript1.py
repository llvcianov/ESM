# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from pathlib import Path
import myLibreria as myLib1

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini")

x = myLib1.vediJpg(path_immagini/"dorian.jpg") 

y = myLib1.vediRAW(path_immagini/"house.y", 512, 512, np.uint8)

#mylib.vediRGBdivisi(path_immagini/"fragole.jpg")

#mylib.annullaComponente(path_immagini/"colori.jpg", 'B')

#mylib.vediRGB(path_immagini/"Washington_red.tif", path_immagini/"Washington_green.tif", 
#             path_immagini/"Washingyon_blue.tif", path_immagini/"Washington_infrared.tif" )

#mylib.media(path_immagini/"dorian.jpg", 3)

#mylib.varianza(path_immagini/"dorian.jpg", 5)

#mylib.istogramma(path_immagini/"dorian.jpg")







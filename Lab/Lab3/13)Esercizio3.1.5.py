# -*- coding: utf-8 -*-
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage.exposure as exp #equalizzazione istogramma
from skimage.util import random_noise #rumore
from skimage.transform import warp #geometriche
from pathlib import Path
import myLibreria as my

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab")

def filtro_guidato(x,g,B):
    """normalizzo"""
    
    x = exp.rescale_intensity(x, in_range='image', out_range=(0,1))
    g = exp.rescale_intensity(g, in_range='image', out_range=(0,1))
    
    """medie e varianza"""
    media_locale_x = ndi.uniform_filter(x, (B,B), mode='reflect')
    media_locale_g = ndi.uniform_filter(g, (B,B), mode='reflect')
    var_locale_g = ndi.generic_filter(g, np.var, (B,B), mode='reflect')
    
    """calcolo le correlazioni locali"""
    corr_gx = ndi.uniform_filter(g*x, (B,B))
    
    """immagini ricavate da formula date da traccia"""
    a = (corr_gx - (media_locale_x * media_locale_g))/ (var_locale_g + 2**(-60))
    b = media_locale_x - a * media_locale_g
    
    """medio localmente e ritorno valore"""
    media_a = ndi.uniform_filter(a, (B,B), mode='reflect')
    media_b = ndi.uniform_filter(b, (B,B), mode='reflect')
    
    return media_a * g + media_b
    

guida = np.float64(io.imread(path_immagini/"guida.png"))
mask = np.float64(io.imread(path_immagini/"mask.png"))

plt.figure('guida'); plt.imshow(guida, clim=None, cmap='gray')
plt.figure('con maschera normale'); plt.imshow(mask*guida, clim=None, cmap='gray')

y = filtro_guidato(mask, guida, 10)
plt.figure('con maschera_elaborata'); plt.imshow(y*guida, clim=None, cmap='gray')












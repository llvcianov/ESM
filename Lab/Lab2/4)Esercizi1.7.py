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
Esercizio 1.7

"""

"""
Equalizzazione globale, uso funzione equalize_hist

"""
x = io.imread(path_immagini/"quadrato.tif")
x = np.float64(x)
my.vediIstogrammaStretchato(x, 256)

y = exp.equalize_hist(x)
my.vediIstogrammaStretchato(y, 256)


"""
Equalizzazione locale

uso ndi.generic_filter per scorrere l'immagine ma questa prende in input una funzione
che restituisce un singolo valore e equalize_hist invece restituisce un immagine
creo la funzione local_equalization3x3 che applica equalize alla finestra
e restituisce il pixel centrale

"""

def local_equalization3x3(block):
    """
    Esegue equalizzazione locale di un blocco 3x3 di un immagine.
    da usare in combo con ndi.generic-filter
    Input: la finestra scorrevole di generic_filter
    Return: il pixel centrale dell'elaborazione
    
    """
    """ Reshape in 3 x 3, ndi.generic-filter passa i dati come array 1-D ma
        equalize si aspetta una matrice """
        
    block = block.reshape((3,3))  
    #block = np.reshape(block, (3,3)) alternativa
    eq_block = exp.equalize_hist(block)  
    return eq_block[1,1]  

z = ndi.generic_filter(x, my.local_equalization3x3, (3,3), mode='reflect')        
my.vediIstogrammaStretchato(z, 256)       




















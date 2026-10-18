# -*- coding: utf-8 -*-

import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import skimage.exposure as exp
import skimage.io as io
import skimage.metrics as met
from bitop import bitget
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\esercitazione_250411\esercitazione_250411")
plt.close('all')

def test(x):
    #inserisci codice sotto nella funzione
    xlarge = io.imread(path_immagini/"1.png")
    


xlarge = io.imread(path_immagini/"1.png")
plt.figure(); plt.imshow(xlarge, clim=None, cmap='gray'); plt.title('large')
x = xlarge[0:512,0:512]
plt.figure(); plt.imshow(x, clim=None, cmap='gray'); plt.title('originale')
(M,N) = x.shape

B2 = bitget(x,1)

#calcolo F1 ed F2
#dubbi sul calcolo della feature 1 e 2, posso fare la derivata?
mask1 = np.array([[0, 1,0],
                  [0,-1,0],
                  [0, 0,0]])

f1 = np.sum(np.abs(ndi.correlate(B2, mask1))/((M-1)*N))

#aggiusta maschera e filtro
mask2 = np.array([[0, 1,0],
                  [0,-1,0],
                  [0, 0,0]])

f2 = np.abs(ndi.correlate(B2, mask1))/((M-1)*N)


y = ndi.gaussian_filter(x, 0.5)

X = np.fft.fft2(x)
Y = np.fft.fft2(y)

f3 = 10 * np.log10(met.mean_squared_error(np.abs(X), np.abs(Y)))

f4 = 10 * np.log10(met.mean_squared_error(np.angle(X), np.angle(Y)))

f = 0.7*f1 + 1.5*f2 + 0.01*f3 + 0.001*f4

# if (f > 1.5):
#     return 1
# else:
#     return 2



#controlla soluzione prof
































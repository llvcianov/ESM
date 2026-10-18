# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from pathlib import Path

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Prove\immagini")


def filtra(x):
    "trasformata"
    X = np.fft.fftshift(np.fft.fft2(x))
    
    "progetto il filtro"
    (M,N) = x.shape
    n = np.fft.fftshift(np.fft.fftfreq(N))
    m = np.fft.fftshift(np.fft.fftfreq(M))
    l,k = np.meshgrid(n,m)

    B = 0.15 #grandezza monolatera del filtro

    # D1 = 2*np.abs(np.sqrt((l+0.25)**2 + (k-0.25)**2) - 0.25) < B
    # D2 = np.sqrt((l+0.25)**2 + (k+0.25)**2) < B
    # D3 = np.sqrt((l-0.25)**2 + (k+0.25)**2) < B
    # D4 = np.sqrt((l-0.25)**2 + (k-0.25)**2) < B

    # H = D1 | D2 | D3 | D4
    
    D = np.abs(np.sqrt(l**2 + k**2) - 0.25) #punti maggiori o minori a 0.25 dal centro
    H = D < (B/2) #punti maggiori o minori di B/2 a 0.25 dal centro. 
    
    "filtro"
    Y = H * X
    
    "antitrasformo"
    y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))
    
    return y, H
    

"import immagine"
x = np.float64(io.imread(path_immagini/"fiori.jpg"))/255
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray')

"estraggo le bande"
r = x[:,:,0]
g = x[:,:,1]
b = x[:,:,2]

"filtro ogni banda e stack"
lista_bande = [r,g,b]
lista_bande_filtrate = []
    
for i in range(3):
    a, H = filtra(lista_bande[i])
    lista_bande_filtrate.append(a)

z = np.stack((lista_bande_filtrate[0], lista_bande_filtrate[1],
              lista_bande_filtrate[2]), -1)
plt.figure('filtrata'); plt.imshow(z)

plt.figure('filtro'); plt.imshow(H, clim=[0,1],
                                      cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))

   
# "creo il grafico 3d"
# from mpl_toolkits.mplot3d import Axes3D

# ax = Axes3D(plt.figure()); # crea una figura per i grafici 3d
# ax.plot_surface(l,k,H, linewidth=0, cmap='gray')
    
    
    
    
"codice funzione"
# "trasformata"
# R = np.fft.fftshift(np.fft.fft2(r))
# plt.figure('trasformata'); plt.imshow(np.log(1+np.abs(R)), clim=None,
#                                       cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))


# "progetto il filtro"
# (M,N) = r.shape
# n = np.fft.fftshift(np.fft.fftfreq(N))
# m = np.fft.fftshift(np.fft.fftfreq(M))
# l,k = np.meshgrid(n,m)

# B = 0.15

# D1 = np.sqrt((l+0.25)**2 + (k-0.25)**2) < B
# D2 = np.sqrt((l+0.25)**2 + (k+0.25)**2) < B
# D3 = np.sqrt((l-0.25)**2 + (k+0.25)**2) < B
# D4 = np.sqrt((l-0.25)**2 + (k-0.25)**2) < B

# H = D1 | D2 | D3 | D4
# plt.figure('filtro'); plt.imshow(H, clim=[0,1],
#                                       cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))




















































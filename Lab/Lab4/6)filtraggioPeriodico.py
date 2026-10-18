# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
from skimage.exposure import equalize_hist
from skimage.transform import warp
from pathlib import Path
import myLibreria as my

plt.close('all')
path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab")

"filtraggio di un rumore periodico"

"leggo l'immagine"
file = str(path_immagini/"lenarumorosa_verticale.y")
x = np.float64(np.fromfile(file, np.int16))
x = x.reshape(512,512)
plt.figure('originale'); plt.imshow(x, clim=None, cmap='gray');

"trasformo"
X = np.fft.fftshift(np.fft.fft2(x))
plt.figure('trasformata'); 
plt.imshow(np.log(1+np.abs(X)), clim=None, cmap='gray', extent=(-0.5,+0.5,-0.5,+0.5));

"creazione della griglia"
(M,N) = x.shape
n = np.fft.fftshift(np.fft.fftfreq(N)) # n = indice colonne, cioè sono le x
m = np.fft.fftshift(np.fft.fftfreq(M)) # m = indice righe, cioè sono le y
l,k = np.meshgrid(n,m)

"definizione del filtro"

# "circolare elimina banda per lena verticale"
# nu = 0.2; #offset frequenza sulle x
# B = 0.03; #grandezza del filtro circolare

# D1 = np.sqrt((l-nu)**2 + k**2) #radice di (x-x0)^2 + y^2 per shiftare a destra il centro
# D2 = np.sqrt((l+nu)**2 + k**2) #radice di (x+x0)^2 + y^2 per shiftare a sinistra il centro

# H = (D1>B) & (D2>B)

#circolare elimina banda per lena
# nu = 0.2; #offset frequenza sulle x
# B = 0.02; #B = distanza dal centro
# mu = -0.2 #offset frequenza sulle y
# D1 = np.sqrt((k-mu)**2+(l-nu)**2)
# D2 = np.sqrt((k+mu)**2+(l+nu)**2)
# H = (D1>B) & (D2>B)

"filtro striscia e cerchio combinati"
centro = 0
spessore = 0.0007
D0 = 0.09

"coordinate per la striscia. S è un generico punto distante k dal centro"
S = np.abs(k - centro) 

"coordinate per il cerchio"
D = np.sqrt(l**2 + k**2)

"and tra le condizioni, N.B. il not è perchè quelli sono punti in cui è 0"
H = ~((D >= D0) & (S <= spessore))

plt.figure();
plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Riposta in frequenza del filtro');


"Filtraggio"
Y = X * H;
plt.figure();
plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Trasformata di Fourier immagine filtrata');
y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)));

plt.figure(); plt.imshow(y, clim=[0,256], cmap='gray');
plt.title('Immagine filtrata');

"Calcolo MSE rispetto all'immagine originale"
fileo = str(path_immagini/"lena.y")
xo = np.fromfile(fileo, np.uint8)
xo = np.reshape(xo, [512,512])
xo = np.float64(xo)

plt.figure(); plt.imshow(xo, clim=[0,256], cmap='gray');
plt.title('immagine originale');

MSE = np.mean((xo-y) ** 2)

# import skimage.metrics as metr
# metr.mean_squared_error(xo, y)

print(MSE)























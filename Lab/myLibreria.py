# -*- coding: utf-8 -*-

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage.exposure as exp
from skimage.feature import local_binary_pattern
from bitop import bitget

def vediJpg(nomefile):
    """
    legge un file jpg in scala di grigi
    Input: path immagine
    Return: matrice immagine
    
    """
    x = io.imread(nomefile)
    plt.figure()
    plt.imshow(x, clim=None, cmap = 'gray')
    plt.colorbar()
    return x
     
def vediRAW(nomefile, nrighe, ncolonne, tipo):
    """
    legge un file raw
    Input: path immagine, risoluzione, tipo di dato per livelli di grigio
    Return: matrice immagine
    
    """
    nomefile = str(nomefile)  
    x = np.fromfile(nomefile, tipo) 
    x = np.reshape(x, (nrighe, ncolonne))
    plt.figure()
    plt.imshow(x, clim = None, cmap = 'gray')
    plt.colorbar()
    return x
    
def vediRGB(R, G, B):
    """
    Consente di vedere l'immagine RGB completa a partire dalle sue componenti
    Input: immagini componenti R, G, B
    Return: matrici immagine RGB e IGB
    
    """
    plt.figure()
    plt.subplot(2,3,1); plt.imshow(R, clim = None, cmap = 'gray'); plt.colorbar()
    plt.subplot(2,3,2); plt.imshow(G, clim = None, cmap = 'gray'); plt.colorbar()
    plt.subplot(2,3,3); plt.imshow(B, clim = None, cmap = 'gray'); plt.colorbar()
    y = np.stack((R,G,B), -1)
    plt.subplot(2,3,5); plt.imshow(y)
    return y

def vediFalsiColori(I, G, B):
    """
    Consente di vedere l'immagine IGB completa a partire dalle sue componenti
    Input: immagini componenti R, G, B
    Return: matrici immagine RGB e IGB
    
    """
    plt.figure()
    plt.subplot(2,3,1); plt.imshow(I, clim = None, cmap = 'gray'); plt.colorbar()
    plt.subplot(2,3,2); plt.imshow(G, clim = None, cmap = 'gray'); plt.colorbar()
    plt.subplot(2,3,3); plt.imshow(B, clim = None, cmap = 'gray'); plt.colorbar()
    y = np.stack((I,G,B), -1)
    plt.subplot(2,3,5); plt.imshow(y)
    return y
        
def dividiRGB(x):
    """
    Consente di vedere le componenti RGB dell'immagine jpeg
    Input: matrice immagine
    Return: matrici immagini R, G e B
    
    """
    plt.figure()
    plt.subplot(2,3,2); plt.imshow(x);
    
    R = x[:,:,0]
    plt.subplot(2,3,4); plt.imshow(R, clim = None, cmap='gray')
    plt.title('componente rossa')
    
    G = x[:,:,1]
    plt.subplot(2,3,5); plt.imshow(G, clim= None, cmap='gray')
    plt.title('componente verde')
    
    B = x[:,:,2]
    plt.subplot(2,3,6); plt.imshow(B, clim= None, cmap='gray')
    plt.title('componente blu')
    return R, G, B
    
def annullaComponenteRGB(x, tipo):
    """
    Consente di annullare una componente RGB dell'immagine jpeg
    Input: matrice immagine, tipo componente
    Return: matrice immagine con la componente annullata
    
    """
    M = x.shape[0]; N = x.shape[1] 
    R = x[:,:,0];   G = x[:,:,1];   B = x[:,:,2]
    
    if tipo == 'R':
        R = np.zeros((M,N), x.dtype)
    elif tipo == 'G':
        G = np.zeros((M,N), x.dtype)
    elif tipo == 'B':
        B = np.zeros((M,N), x.dtype)
    else:
        print("Tipo non valido! Usa 'R', 'G' o 'B'.")
        return
    
    y = np.stack((R,G,B), -1)
    plt.figure(); 
    plt.subplot(1,2,1); plt.imshow(x);
    plt.subplot(1,2,2); plt.imshow(y);
    return y
    
def media(x,k):
    """
    Applica filtro media locale all'immagine
    Input: matrice immagine in float e dimensione kernel
    Return: matrice immagine-media

    """
    #alternativa
    #xIm = io.imread(x)
    #xIm = np.float64(xIm)
    #MED = ndi.generic_filter(xIm, np.mean, (k,k), mode = 'reflect')
    
    (M,N) = x.shape
    MED = np.zeros((M,N)) 
    h = (k-1)//2
    xext = np.pad(x, ((h,h),(h,h)), constant_values = 0) #gestisco padding
    #alternativamente xImext = np.pad(xIm, ((h,h),(h,h)), mode = 'symmetric')
    for i in range (M):
        for j in range(N):
            MED[i,j] = np.mean(xext[i:i+k,j:j+k])
    plt.figure()
    plt.subplot(1,2,1); plt.imshow(x, clim=None, cmap='gray')
    plt.subplot(1,2,2); plt.imshow(MED, clim=None, cmap='gray')
    return MED
    
def varianza(x,k):
    """
    Applica filtro varianza locale all'immagine'
    Input: matrice immagine in float e dimensione kernel
    Return: matrice immagine-varianza

    """
    VAR = ndi.generic_filter(x, np.var, (k,k), mode = 'constant')
    return VAR
    
def vediIstogramma(x):
    """
    genera l'istogramma dell'immagine in input'
    Input: matrice immagine

    """
   #alternativa
   #x = io.imread(nomefile)
   #plt.figure()
   #plt.subplot(1,2,1); plt.imshow(z, clim=None, cmap = 'gray')
   #plt.subplot(1,2,2); plt.hist(z.flatten(), bins = 256); plt.xlim((0,255))    
    
    n, b = np.histogram(x, np.arange(257)); # istogramma
    plt.figure();
    plt.subplot(1,2,2); plt.imshow(x, clim=[0,255], cmap='gray')
    plt.subplot(1,2,1)
    plt.bar(np.arange(256), n); # grafico a barre
    plt.axis([0,255,0,1.1*np.max(n)]); # estremi per ascisse e ordinate   
    
def fshs(x, k):
    """
    stretcha l'istogramma dell'immagine in input
    Input: matrice immagine e valore massimo di colore
    return: l'immagine stretch
    """
    minimo = np.min(x)
    massimo = np.max(x)
    y = (k - 1) * (x - minimo)/(massimo - minimo)
    return y

def vediIstogrammaStretchato(x,k):
    """
    genera l'istogramma stretchato dell'immagine in input'
    Input: matrice immagine

    """
    y = fshs(x,k)
    plt.figure()
    plt.subplot(1,2,1); plt.imshow(y, clim=[0,255], cmap = 'gray')
    plt.subplot(1,2,2); plt.hist(y.flatten(), bins = 256); plt.xlim((0,255))    
    
   
def vedi_bit_plane(x):
    """
    Estrae i bit plane della matrice immagine in input
    Input: matrice immagine
    Return: matrice contenente le matrici bitplane
    
    """
    (M,N) = x.shape
    bitplane = np.zeros((M,N,8), dtype=x.dtype)
    plt.figure()
    for i in range(8):
        bitplane[:,:,i] = bitget(x, i)
        plt.subplot(2,4,i+1); plt.imshow(bitget(x,i), clim=[0,1], cmap='gray')
        
    return bitplane

def local_equalization3x3(block):
    """
    Esegue equalizzazione locale di un blocco 3x3 di un immagine.
    da usare in combo con ndi.generic-filter
    Input: la finestra scorrevole di generic_filter
    Return: il pixel centrale dell'elaborazione
    
    """
    # Reshape in 3 x 3, ndi.generic-filter passa i dati come array 1-D ma
    #equalize si aspetta una matrice
    block = block.reshape((3,3))  
    eq_block = exp.equalize_hist(block)  
    return eq_block[1,1]  

def smooth(x):
    h = np.array[[1,2,1],[2,4,2],[1,2,1]]
    y = ndi.correlate(x, h, mode = 'reflect')
    return y

def enhanc(x,mask,k):
    X1 = mask * x
    a = 0.073
    b = 0.177
    # h = ([[a,b,a],
    #       [b,0,b],
    #       [a,b,a]])
    
    h = ([[a,b,b,b,b,a],
          [b,0,0,0,0,b],
          [b,0,0,0,0,b],
          [b,0,0,0,0,b],
          [b,0,0,0,0,b],
          [a,b,b,b,b,a]])
    
    for i in range(k):
        X2 = ndi.convolve(X1, h, mode = 'reflect') #immagine filtrata
        X1 = (1-mask)*X2 + mask*X1 #nuova immagine
        
    return X1
        
def gaussLPF(x, sigma):
    """
    Esegue low pass filter gaussiano.
    Input: immagine e deviazione standard
    Return: immagine filtrata
    
    """
    X = np.fft.fft2(x)
    X = np.fft.fftshift(X)
    
    M,N = x.shape
    m = np.fft.fftshift(np.fft.fftfreq(M))
    n = np.fft.fftshift(np.fft.fftfreq(N))
    l,k = np.meshgrid(n,m)
    D = np.sqrt(k**2 + l**2)
    sigma = 0.2    
    H = np.exp(-(D**2)/(2*(sigma**2)))
    Y = H * X
    
    return np.real(np.fft.ifft2(np.fft.ifftshift(Y)))


def rgb2cmy(x):
    """converte immagine RGB in CMY"""
    C = 1 - x[:,:,0]
    M = 1 - x[:,:,1]
    Y = 1 - x[:,:,2]
    return np.stack((C,M,Y),-1)

def cmy2rgb(x):
    """converte immagine CMY in RGB"""
    R = 1 - x[:,:,0]
    G = 1 - x[:,:,1]
    B = 1 - x[:,:,2]
    return np.stack((R,G,B),-1)
    
def extract_feat(x,P,R):
    "estrae il vettore di feature dall'immagine mediante LBP"
    y = local_binary_pattern(x, P, R, method='ror')
    h,b = np.histogram(y, bins=np.arange(257), density=True)
    return h
    
        
    
    
    
    
    
    
    
    
    
    
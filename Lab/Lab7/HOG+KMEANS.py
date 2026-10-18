# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from skimage.feature import hog
from sklearn.cluster import k_means
plt.close('all')

x = np.float32(io.imread(r'C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab\textures.png'))

"visualizzazione dei gradienti"
y, hog_image = hog(x, pixels_per_cell=(8, 8), visualize=True)
plt.figure(1)
plt.subplot(1,2,1); plt.imshow(x, clim=[0,255], cmap='gray')
plt.subplot(1,2,2); plt.imshow(np.log(hog_image+1), clim=None, cmap='gray')
# plt.show()

"estrazione feature tramite HOG"
y = hog(x, feature_vector=False)

"applico k-means sull'immagine dei gradienti"
k = 4
M = y.shape[0]
N = y.shape[1]
y = np.reshape(y, (M*N,-1))
centroid, idx, sum_var = k_means(y, k)
idx = np.reshape(idx, (M,N))

plt.figure()
plt.imshow(idx, clim=[0,k-1], cmap='jet')


















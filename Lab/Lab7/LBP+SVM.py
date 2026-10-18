# -*- coding: utf-8 -*-

from skimage.feature import local_binary_pattern
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.feature import local_binary_pattern
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import LinearSVC
from pathlib import Path
from glob import glob

path_immagini = Path(r"C:\Users\lucia\Desktop\FilePc\Uni\Magistrale\ESM\Laboratorio\Immagini_lab")
plt.close('all')

P = 8
R = 1
method = 'default'
def extract_feat(x):
    y = local_binary_pattern(x, P, R, method=method)
    h,b = np.histogram(y, bins=np.arange(257), density=True)
    return h

""" USO DI LBP + SVM PER CLASSIFICAZIONE TUMORI"""

"import dataset etichettato + vettori di feature del dataset"
train_label = np.load(path_immagini/'train_label.npy')
train_feat = np.load(path_immagini/'train_lbp_8_1_default.npy')

"Normalizzo i vettori di feature"
mu = np.mean(train_feat, 0)
sigma = np.std(train_feat, 0)
train_feat = (train_feat - mu)/(sigma + 1e-15)

"Addestro il classificatore"
classifier = LinearSVC().fit(train_feat, train_label) # training-phase

"provo a determinare la classe per un immagine test"
x = io.imread(path_immagini/'test_breakhis.png')
plt.figure(); plt.imshow(x, clim=None, cmap='gray')
feat = extract_feat(x)

feat = (feat - mu)/(sigma + 1e-15)
#trasformo vettore colonna in vettore riga per mandarlo in input al modello
feat = np.reshape(feat, (1, -1))

predizione = classifier.predict(feat)
if predizione==1:
    plt.title('tumore maligno')
    print('tumore maligno')
else:
    plt.title('tumore benigno')
    print('tumore benigno')


"provo a determinare la classe con un dataset di test per valutare l'accuracy"

"creo due liste di test, una con tumori benigni e una con tumori maligni"
list_filenames_0 = glob(str(path_immagini/'test_set/testset/benign/*.png'))
list_filenames_1 = glob(str(path_immagini/'test_set/testset/malignant/*.png'))

"calcolo per ogni immagine il vettore di feature e definisco le etichette"
list_feat = []
list_label = []

for filename in list_filenames_0:
    x = np.float64(io.imread(filename))
    f = extract_feat(x)
    list_feat.append(f)
    list_label.append(0)
    
for filename in list_filenames_1:
    x = np.float64(io.imread(filename))
    f = extract_feat(x)
    list_feat.append(f)
    list_label.append(1)

test_label = np.array(list_label)
test_feat = np.stack(list_feat, 0)

"normalizzo"
test_feat = (test_feat - mu)/(sigma + 1e-15)

"predico"
pred = classifier.predict(test_feat)

"calcolo metriche confrontando le predizioni fatte con la lista di etichette"
"del test"
acc = np.mean(test_label==pred)
#oppure
Acc = accuracy_score(test_label, pred)
print(Acc)
print(acc)

print(classification_report(test_label, pred))



























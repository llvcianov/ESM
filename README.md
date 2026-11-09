# ESM — Elaborazione di Segnali Multimediali

Coursework for **Elaborazione di Segnali Multimediali (ESM)**, Master's Degree in Computer Engineering, University of Naples Federico II.

## [Progetto/](Progetto) — Depth Estimation

Monocular depth estimation project based on the [DenseDepth](Progetto/DenseDepth.pdf) architecture (a DenseNet encoder + upsampling decoder), trained on the NYU Depth v2 dataset.

- [`DenseDepth_Progetto04.ipynb`](Progetto/DenseDepth_Progetto04.ipynb) — the project notebook: data loading, model, training and evaluation.
- [`DepthEstimation_Progetto04.pptx`](Progetto/DepthEstimation_Progetto04.pptx) — presentation slides.
- [`DepthAnything.ipynb`](Progetto/DepthAnything.ipynb) — a quick demo of [Depth Anything V2](Progetto/DepthAnythingv1.pdf), a more recent depth-estimation model, used as a reference point for comparison.
- References: [`DenseDepth.pdf`](Progetto/DenseDepth.pdf), [`DenseNet.pdf`](Progetto/DenseNet.pdf), [`DepthAnythingv1.pdf`](Progetto/DepthAnythingv1.pdf), [`paperEigenEtAl.pdf`](Progetto/paperEigenEtAl.pdf) (an earlier, classic approach to depth estimation from a single image).

## [Lab/](Lab) — Image Processing Labs

Weekly lab exercises in Python (NumPy/SciPy/scikit-image), one folder per session, each paired with its assignment sheet:

| Folder | Topic |
|---|---|
| [`Lab1`](Lab/Lab1) | Basic image representation (histogram, mean, variance) |
| [`Lab2`](Lab/Lab2) | Point, arithmetic and geometric operations |
| [`Lab3`](Lab/Lab3) | Spatial filtering (smoothing, sharpening, non-linear filters) |
| [`Lab4`](Lab/Lab4) | Frequency-domain processing (2D DFT, frequency filtering) |
| [`Lab5`](Lab/Lab5) | Color image processing |
| [`Lab6`](Lab/Lab6) | Morphological operations |
| [`Lab7`](Lab/Lab7) | Local descriptors for image classification (LBP, HOG, KNN/SVM/K-means) |
| [`DeepLearningBasics`](Lab/DeepLearningBasics) | Intro deep-learning exercises on Colab: LeNet from scratch, pretrained ImageNet models, and fine-tuning on a custom dataset |

[`Lab/Immagini/`](Lab/Immagini) and [`Lab/Immagini_morfologia/`](Lab/Immagini_morfologia) hold only the specific test images each script actually loads (not the full set handed out for the course).

`Lab/bitop.py`, `Lab/color_convertion.py`, `Lab/color_cube.py`, and `Lab/seg_utils.py` are course-provided utility modules that the lab scripts import; `Lab/myLibreria.py` is my own, built up over the course from what started as separate per-lab helper files.

## [Scritto/](Scritto) — Written Exam Practice

[`Scritto/Prove/`](Scritto/Prove) collects practice at solving past written exam papers (`esm_provaN.pdf`) and one lab exercise session (`esm_esercitazione.pdf`), each with my own Python solution(s) and the images they need, under `Scritto/Prove/immagini/`.

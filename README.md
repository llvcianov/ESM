# ESM — Elaborazione di Segnali Multimediali

Coursework for **Elaborazione di Segnali Multimediali (ESM)**, Master's Degree in Computer Engineering, University of Naples Federico II.

## Progetto — Depth Estimation

Monocular depth estimation project based on the [DenseDepth](DenseDepth.pdf) architecture (a DenseNet encoder + upsampling decoder), trained on the NYU Depth v2 dataset.

- [`DenseDepth_Progetto04.ipynb`](DenseDepth_Progetto04.ipynb) — the project notebook: data loading, model, training and evaluation.
- [`DepthEstimation_Progetto04.pptx`](DepthEstimation_Progetto04.pptx) — presentation slides.
- [`DepthAnything.ipynb`](DepthAnything.ipynb) — a quick demo of [Depth Anything V2](DepthAnythingv1.pdf), a more recent depth-estimation model, used as a reference point for comparison.
- References: [`DenseDepth.pdf`](DenseDepth.pdf), [`DenseNet.pdf`](DenseNet.pdf), [`DepthAnythingv1.pdf`](DepthAnythingv1.pdf), [`paperEigenEtAl.pdf`](paperEigenEtAl.pdf) (an earlier, classic approach to depth estimation from a single image).

## Lab — Image Processing Labs

Weekly lab exercises in Python (NumPy/SciPy/scikit-image), one folder per session, each paired with its assignment sheet:

| Folder | Topic |
|---|---|
| [`Lab1`](Lab1) | Basic image representation (histogram, mean, variance) |
| [`Lab2`](Lab2) | Point, arithmetic and geometric operations |
| [`Lab3`](Lab3) | Spatial filtering (smoothing, sharpening, non-linear filters) |
| [`Lab4`](Lab4) | Frequency-domain processing (2D DFT, frequency filtering) |
| [`Lab5`](Lab5) | Color image processing |
| [`Lab6`](Lab6) | Morphological operations |
| [`Lab7`](Lab7) | Local descriptors for image classification (LBP, HOG, KNN/SVM/K-means) |
| [`DeepLearningBasics`](DeepLearningBasics) | Intro deep-learning exercises on Colab: LeNet from scratch, pretrained ImageNet models, and fine-tuning on a custom dataset |

[`Immagini/`](Immagini) and [`Immagini_morfologia/`](Immagini_morfologia) hold only the specific test images each script actually loads (not the full set handed out for the course).

`bitop.py`, `color_convertion.py`, `color_cube.py`, and `seg_utils.py` at the root of this folder are course-provided utility modules that the lab scripts import; `myLibreria.py` is my own, built up over the course from what started as separate per-lab helper files.

## Scritto — Written Exam Practice

[`Prove/`](Prove) collects practice at solving past written exam papers (`esm_provaN.pdf`) and one lab exercise session (`esm_esercitazione.pdf`), each with my own Python solution(s) and the images they need, under [`Prove/immagini/`](Prove/immagini).

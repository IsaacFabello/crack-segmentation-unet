# crack-segmentation-unet
Master's Thesis Source Code: Crack Segmentation using U-Net, ResNet18, ViT, and Attention Gates

# Crack Segmentation using Deep Learning 🏗️🔍
*(Scroll down for the Spanish version / Versión en español más abajo)*

This repository contains the source code for my Master's Thesis (TFM). The project focuses on the semantic segmentation of structural cracks using Deep Learning, evaluating the performance of different architectural variations based on U-Net.

## 📂 Dataset
The dataset used to train and evaluate the models includes both real and synthetic crack images. Due to storage limits, the images and ground truth masks are not hosted directly in this repository.

👉 **[Download Synthetic Dataset from Google Drive](https://drive.google.com/drive/folders/1Uiydeyf5VtW0hwKut71ppWnxM5KkKEg_?usp=sharing)**

## 🏗️ Model Architectures
This project explores four different network architectures to compare their effectiveness in identifying crack boundaries:

* **Model 1:** U-Net with ResNet18 backbone.
* **Model 2:** U-Net + ResNet18 + Vision Transformer (ViT) at the bottleneck.
* **Model 3:** U-Net + ResNet18 + ViT + Attention Gates (AG) in the decoder.
* **Model 4:** U-Net + ResNet18 + Spatial Attention (SA) module + Attention Gates (AG).

## 📁 Repository Structure
The repository is divided into two main categories:

* **`/models_colab`**: Contains Jupyter Notebooks (`.ipynb`) ready to run on Google Colab. These include the training loops, custom loss functions (Focal, Tversky, Boundary Loss), and evaluation metrics (Precision, Recall, F1-Score, IoU).
* **`/data_processing`**: Contains Python scripts (`.py`) for data wrangling, including sequential renaming, image resizing, binary mask generation, and watermark removal.

# Segmentación de Grietas con Deep Learning 🏗️🔍

Este repositorio contiene el código fuente de mi Trabajo de Fin de Máster (TFM). El proyecto se centra en la segmentación semántica de grietas estructurales utilizando Deep Learning, evaluando el rendimiento de diferentes variaciones arquitectónicas basadas en U-Net.

## 📂 Dataset
El conjunto de datos utilizado para entrenar y evaluar los modelos incluye tanto imágenes de grietas reales como sintéticas. Debido a los límites de almacenamiento, las imágenes y las máscaras (ground truth) no están alojadas directamente en este repositorio.

👉 **[Descargar Dataset Sintético desde Google Drive](https://drive.google.com/drive/folders/1Uiydeyf5VtW0hwKut71ppWnxM5KkKEg_?usp=sharing)**

## 🏗️ Arquitecturas de los Modelos
Este proyecto explora cuatro arquitecturas de red diferentes para comparar su efectividad en la identificación de los bordes de las grietas:

* **Modelo 1:** U-Net con ResNet18 como backbone.
* **Modelo 2:** U-Net + ResNet18 + Vision Transformer (ViT) en el cuello de botella.
* **Modelo 3:** U-Net + ResNet18 + ViT + Attention Gates (AG) en el decodificador.
* **Modelo 4:** U-Net + ResNet18 + Módulo de Atención Espacial (SA) + Attention Gates (AG).

## 📁 Estructura del Repositorio
El repositorio está dividido en dos categorías principales:

* **`/models_colab`**: Contiene cuadernos de Jupyter (`.ipynb`) listos para ejecutarse en Google Colab. Incluyen los bucles de entrenamiento, funciones de pérdida personalizadas (Focal, Tversky, Boundary Loss) y métricas de evaluación (Precisión, Recall, F1-Score, IoU).
* **`/data_processing`**: Contiene scripts de Python (`.py`) para la preparación de datos, incluyendo renombrado secuencial, redimensionado de imágenes, generación de máscaras binarias perfectas y eliminación de marcas de agua.



---
**Autor:** Isaac Fabello
**Fecha:** 2026

import cv2
import os
import glob

# 1. Configura tus rutas
carpeta_origen = 'D:\Radiance\TFM\Segmented_cracks'
carpeta_destino = 'D:\Radiance\TFM\Segmented_cracks_sin_marca'

# Crear la carpeta de destino si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# 2. Define las coordenadas de la mancha (en píxeles)
# x1, y1: coordenada de la esquina superior izquierda
# x2, y2: coordenada de la esquina inferior derecha
x1, y1 = 343, 342  
x2, y2 = 369, 369  

for i in range(325, 326):
    nombre_archivo = f"Segmented{i}.jpg" 
    ruta = os.path.join(carpeta_origen, nombre_archivo)

    # Leer la imagen
    img = cv2.imread(ruta)
    
    if img is not None:
        # A. REDIMENSIONAR LA IMAGEN
        # cv2.resize recibe el tamaño como una tupla (ancho, alto)
        img_redimensionada = cv2.resize(img, (378, 378))

        # Poner los píxeles en color negro (BGR: 0, 0, 0)
        # Nota: en OpenCV y Numpy, el orden de los ejes es [Y, X]
        img_redimensionada[y1:y2, x1:x2] = [0, 0, 0]
        
        # Obtener el nombre del archivo original
        nombre_archivo = os.path.basename(ruta)
        ruta_guardado = os.path.join(carpeta_destino, nombre_archivo)
        
        # Guardar la nueva imagen
        cv2.imwrite(ruta_guardado, img_redimensionada)
        print(f"Procesada con éxito: {nombre_archivo}")
    else:
        print(f"Error al leer: {ruta}")

print("¡Todas las imágenes han sido procesadas!")
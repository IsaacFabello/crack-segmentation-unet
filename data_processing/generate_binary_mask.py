import cv2
import os
import glob

def binarize_masks(input_folder, output_folder, threshold=127):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Buscar todas las imágenes en la carpeta de entrada (puedes añadir más extensiones si lo necesitas)
    image_paths = glob.glob(os.path.join(input_folder, '*.*'))
    valid_extensions = {'.png', '.jpg', '.jpeg', '.tif', '.tiff', '.bmp'}

    for img_path in image_paths:
        # Comprobar que el archivo es una imagen
        ext = os.path.splitext(img_path)[1].lower()
        if ext not in valid_extensions:
            continue
            
        # Leer la imagen en escala de grises
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        
        if img is None:
            print(f"Error al leer la imagen: {img_path}")
            continue

        # Aplicar el umbral: 
        # Si el píxel es mayor que el 'threshold', se convierte a 255 (blanco)
        # Si es menor o igual, se convierte a 0 (negro)
        _, binary_mask = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

        # Obtener el nombre del archivo y crear la ruta de salida
        filename = os.path.basename(img_path)
        output_path = os.path.join(output_folder, filename)

        # Guardar la nueva máscara binarizada (preferiblemente en formato PNG para evitar pérdida de calidad)
        # Si la imagen original era JPG, la guardamos como PNG cambiando la extensión
        if ext in ['.jpg']:
            output_path = os.path.splitext(output_path)[0] + '.png'
            
        cv2.imwrite(output_path, binary_mask)
        print(f"Procesada y guardada: {output_path}")

# --- Configuración ---
# Cambia estas rutas por las carpetas reales de tu ordenador
CARPETA_ENTRADA = 'D:\Radiance\TFM\Segmented_cracks_sin_marca'
CARPETA_SALIDA = 'D:\Radiance\TFM\Segmented_cracks_sin_marca_png'

# Valor del umbral (0 a 255). 
# 127 es el punto medio. Si quieres que los grises claros sean blancos, bájalo. 
# Si quieres que solo los grises muy claros sean blancos, súbelo.
UMBRAL = 85 

# Ejecutar la función
binarize_masks(CARPETA_ENTRADA, CARPETA_SALIDA, threshold=UMBRAL)
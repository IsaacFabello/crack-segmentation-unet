import os
import cv2

def redimensionar_con_cv2(carpeta_origen, carpeta_destino, tamaño=(448, 448)):
    # Crear la carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        print(f"Se ha creado la carpeta: {carpeta_destino}")

    # Extensiones de imagen soportadas
    extensiones_validas = ('.jpg', '.png')
    
    procesadas = 0

    for nombre_archivo in os.listdir(carpeta_origen):
        if nombre_archivo.lower().endswith(extensiones_validas):
            ruta_origen = os.path.join(carpeta_origen, nombre_archivo)
            ruta_destino = os.path.join(carpeta_destino, nombre_archivo)
            
            # OpenCV lee la imagen (por defecto en formato BGR)
            img = cv2.imread(ruta_origen)
            
            # cv2.imread devuelve None si hay un problema al leer el archivo
            if img is not None:
                # Inter_AREA es el método de interpolación recomendado para reducir imágenes.
                # Si se quiere aumentar el tamaño de las imágenes, cv2.INTER_CUBIC suele ser mejor.
                img_redimensionada = cv2.resize(img, tamaño, interpolation=cv2.INTER_AREA)
                
                # Guardar la imagen
                cv2.imwrite(ruta_destino, img_redimensionada)
                print(f"✅ Éxito: {nombre_archivo} -> {tamaño}")
                procesadas += 1
            else:
                print(f"❌ Error: No se pudo leer la imagen {nombre_archivo}")

    print(f"\nProceso terminado. Se han redimensionado {procesadas} imágenes con OpenCV.")

# --- Configuración ---
carpeta_entrada = "D:\Radiance\TFM\Segmented_cracks_sin_marca_png"
carpeta_salida = "D:\Radiance\TFM\Segmented_cracks_sin_marca_png_resize448"

# Ejecutar la función
redimensionar_con_cv2(carpeta_entrada, carpeta_salida)
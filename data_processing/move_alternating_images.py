import os
import shutil

def seleccionar_imagenes_alternadas(carpeta_origen, carpeta_destino, guardar=10, saltar=10):
    """
    Copia imágenes de una carpeta a otra alternando según las cantidades indicadas.
    """
    # 1. Crear la carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # 2. Definir extensiones de imagen válidas (puedes añadir más si lo necesitas)
    extensiones_validas = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')

    # 3. Obtener los archivos de la carpeta de origen y filtrarlos
    archivos = [f for f in os.listdir(carpeta_origen) if f.lower().endswith(extensiones_validas)]
    
    # 4. Ordenar alfabéticamente para mantener la consistencia en el patrón
    archivos.sort() 

    imagenes_copiadas = 0
    imagenes_saltadas = 0

    # 5. Iterar sobre las imágenes y aplicar la lógica de alternancia
    for i, archivo in enumerate(archivos):
        # La suma de 'guardar' + 'saltar' crea el tamaño de nuestro bloque cíclico (ej. 10 + 10 = 20).
        # Si el resto de la división (i % 20) es menor que 10, guardamos. Si es 10 o mayor, saltamos.
        if i % (guardar + saltar) < guardar:
            ruta_origen = os.path.join(carpeta_origen, archivo)
            ruta_destino = os.path.join(carpeta_destino, archivo)
            
            # shutil.copy2 copia el archivo conservando los metadatos originales (fecha, etc.)
            shutil.copy2(ruta_origen, ruta_destino)
            imagenes_copiadas += 1
        else:
            imagenes_saltadas += 1

    # Resumen final
    print("--- Resumen del proceso ---")
    print(f"Total de imágenes encontradas: {len(archivos)}")
    print(f"Imágenes copiadas: {imagenes_copiadas}")
    print(f"Imágenes ignoradas: {imagenes_saltadas}")


# Rutas de las carpetas
ruta_origen = "D:/Radiance/TFM/Generated_cracks+dataset_real/masks_recortadas_resize448"
ruta_destino = "D:/Radiance/TFM/Generated_cracks+dataset_real/masks_recortadas_resize448_2"

# Ejecuta la función (guarda 10, salta 10)
seleccionar_imagenes_alternadas(ruta_origen, ruta_destino, guardar=10, saltar=10)
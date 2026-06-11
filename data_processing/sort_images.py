import os
import re

def ordenar_naturalmente(lista):
    # Ordena textos con números de forma humana (ej: 1, 2, 10, 11 en vez de 1, 10, 11, 2) 
    convertir = lambda texto: int(texto) if texto.isdigit() else texto.lower()
    clave_alfanumerica = lambda clave: [convertir(c) for c in re.split('([0-9]+)', clave)]
    return sorted(lista, key=clave_alfanumerica)

def renombrar_imagenes_secuencialmente(carpeta, prefijo="Segmented", nuevo_prefijo = "Crack", extension=".png"):
    # 1. Obtener la lista de imágenes en la carpeta
    archivos = [f for f in os.listdir(carpeta) 
                if f.lower().startswith(prefijo.lower()) and f.lower().endswith(extension.lower())]
    
    if not archivos:
        print("No se encontraron imágenes con ese prefijo y extensión.")
        return

    # 2. Ordenarlas de forma natural
    archivos_ordenados = ordenar_naturalmente(archivos)
    
    print(f"Se encontraron {len(archivos_ordenados)} imágenes. Iniciando proceso...")

    # 3. Paso Intermedio: Renombrar a nombres temporales para evitar colisiones
    rutas_temporales = []
    for i, nombre_archivo in enumerate(archivos_ordenados, 1):
        ruta_antigua = os.path.join(carpeta, nombre_archivo)
        nombre_temporal = f"temp_borrar_{i}{extension}"
        ruta_temporal = os.path.join(carpeta, nombre_temporal)
        
        os.rename(ruta_antigua, ruta_temporal)
        rutas_temporales.append(ruta_temporal)

    # 4. Paso Final: Renombrar al formato definitivo (Imagen1.jpg, Imagen2.jpg...)
    for i, ruta_temporal in enumerate(rutas_temporales, 1):
        nombre_nuevo = f"{nuevo_prefijo}{i}{extension}"
        ruta_nueva = os.path.join(r"D:\Radiance\TFM\Generated_cracks+dataset_real\masks_recortadas", nombre_nuevo)
        
        os.rename(ruta_temporal, ruta_nueva)
    
    print("¡Proceso completado! Todas las imágenes han sido renombradas sin huecos.")

# === CONFIGURACIÓN ===
# ruta de la carpeta. 
ruta_carpeta = r"D:\Radiance\TFM\Segmented_cracks_sin_marca_png" 

renombrar_imagenes_secuencialmente(ruta_carpeta)
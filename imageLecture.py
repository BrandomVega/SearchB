import pytesseract
from PIL import Image
import re
import time
import os
def encontrar_texto_entre_comillas(cadena):
    patron = r'"(.*?)"'
    coincidencias = re.findall(patron, cadena)
    return coincidencias


def imageToText(textoNormalizado, path):
    inicio = time.time()
    print(f"Buscando para: {path}")
    imagen = Image.open(path)
    texto = pytesseract.image_to_string(imagen).lower()
    textoWords = texto.split()
    cuenta = 0
    for palabra in textoNormalizado:
        if palabra in textoWords: 
            cuenta+=1

    end = time.time()
    print(f"    Tiempo {round(end-inicio, 4)} segundos ")

    print(f"    Coincidencia: {cuenta/len(textoNormalizado)*100}%")


extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp']

texto = input("Buscar: \n>> ")
textoNormalizado = encontrar_texto_entre_comillas(texto)[0].lower().split()

direccionCarpeta = input("Ingresa el path de la carpeta a buscar: ").strip()
print("")
#print(direccionCarpeta)

#carpeta = r"C:\Users\Brandom\Pictures\Screenshots"
nombres_archivos = os.listdir(direccionCarpeta)
for nombre_archivo in nombres_archivos:
    ext = os.path.splitext(nombre_archivo)[-1].lower()
    if ext in extensiones_imagen:
        imageToText(textoNormalizado, direccionCarpeta + "\\" +nombre_archivo)
    else:
        #print("--------------   ESTE NO:",nombre_archivo)
        continue

    #"C:\Users\Brandom\Pictures\forProyect\epico.jpg"






#Practica 2 Algoritmo de enjambre de particulas
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

    print(textoWords)

    cuenta = 0
    for palabra in textoNormalizado:
        if palabra in textoWords: 
            cuenta+=1

    end = time.time()
    print(f"    Tiempo {round(end-inicio, 4)} segundos ")

    print(f"    Coincidencia: {cuenta}")



#PROCESO: ENCUENTRA TEXTO EN IMAGENES
from gui import selectDirectory as getDir

directoryPath = getDir.getDirectory()
print(directoryPath)

textQuery= input("Buscar: \n>> ")
searchText = encontrar_texto_entre_comillas(textQuery)[0].lower().split()

extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp']

nombres_archivos = os.listdir(directoryPath)
for nombre_archivo in nombres_archivos:
    ext = os.path.splitext(nombre_archivo)[-1].lower()
    if ext in extensiones_imagen:
        imageToText(searchText, directoryPath + "\\" +nombre_archivo)
    else:
        #print("--------------   ESTE NO:",nombre_archivo)
        continue



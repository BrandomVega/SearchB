import pytesseract
from PIL import Image
import re
import time
import os

def automatonCoincidenceWords(searchWord, text):
    searchWord = list(searchWord)
    cuenta = 0

    for letter in text: 
        if searchWord[cuenta] == letter:
            cuenta+=1
            if cuenta == len(searchWord):
                return True
        else:
            cuenta = 0

    if cuenta != 0:
        return True
    return False

def encontrar_texto_entre_comillas(cadena):
    patron = r'"(.*?)"'
    coincidencias = re.findall(patron, cadena)
    return coincidencias

def imageToText(textoBusqueda, path):
    inicio = time.time()
    #print(f"Buscando para: {path}")
    imagen = Image.open(path)
    texto = pytesseract.image_to_string(imagen).lower()
    textoWords = texto.split()

    
    
    cuenta = 0
    for palabra in textoBusqueda:
        for texto in textoWords:
            if automatonCoincidenceWords(palabra, texto):
                cuenta+=1

    end = time.time()
    #print(f"    Tiempo {round(end-inicio, 4)} segundos ")

    #print(f"    Coincidencia: {cuenta}")
    return cuenta



#PROCESO: ENCUENTRA TEXTO EN IMAGENES
# archivo2.py
import sys
sys.path.append(r"C:\Users\Brandom\Documents\1Proyecto")


from gui import selectDirectory as getDir

directoryPath = getDir.getDirectory()
print(directoryPath)

textQuery= input("Buscar: \n>> ")
searchText = encontrar_texto_entre_comillas(textQuery)[0].lower().split()

extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp']


bestCoincidence = {'path':"a", 'cuenta':0}
nombres_archivos = os.listdir(directoryPath)
for nombre_archivo in nombres_archivos:
    ext = os.path.splitext(nombre_archivo)[-1].lower()
    if ext in extensiones_imagen:
        path = directoryPath + "\\" +nombre_archivo
        cuenta = imageToText(searchText, path)
        if cuenta > bestCoincidence["cuenta"]:
            bestCoincidence['path'] = path
            bestCoincidence['cuenta'] = cuenta

print(f"    > Resultados: \n   path: {bestCoincidence['path']}")




from PIL import Image
from ultralytics import YOLO
import json 
import os

#Import proyectLibraries
import sys
sys.path.append(r'C:\Users\Brandom\Documents\1Proyecto')
from gui import selectDirectory as getDir




#Get directory to search
directoryPath = getDir.getDirectory()
extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp']
nombres_archivos = os.listdir(directoryPath)
    
#Load yolo Model
model = YOLO('yolov8n.pt')

#For each image, data will be stored as json
resultData = []

#Iterate file with the extension for images
for nombre_archivo in nombres_archivos:
    ext = os.path.splitext(nombre_archivo)[-1].lower()
    if ext in extensiones_imagen:
        path = directoryPath + "\\" +nombre_archivo
        results = model(path)  #Evaluate YOLO model
        for indvResults in results:
            resultData.append(json.loads(indvResults.tojson()))


#Show data found

for i, imageData in enumerate(resultData):
    print(f"Imagen {i}: Clases encontradas")
    last = ""
    for object in imageData:
        if last != object['name']:
            last = object['name']
            print("     >Nombre:", object['name'])
        
        #print("     >Clase:", object['class'])
        #print("     >Confianza:", object['confidence'])
        #print("     >Coordenadas de la caja delimitadora:", object['box'])
    print("\n\n")

from PIL import Image
from ultralytics import YOLO
import json 
import os

import matplotlib.pyplot as plt
import matplotlib.patches as patches

import sys

sys.path.append(r'C:\Users\Brandom\Documents\1Proyecto')

from gui import selectDirectory as getDir
#Get directory to search
directoryPath = getDir.getDirectory()
extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp']
nombres_archivos = os.listdir(directoryPath)
#Load yolo Model
model = YOLO(r"C:\Users\Brandom\Documents\1Proyecto\yolo\scenario\runs\detect\train\weights\best.pt")
#For each image, data will be stored as json
resultData = []
crudeResults  = []
#Iterate file with the extension for images
for nombre_archivo in nombres_archivos:
    ext = os.path.splitext(nombre_archivo)[-1].lower()
    if ext in extensiones_imagen:
        path = os.path.join(directoryPath, nombre_archivo)
        results = model(path, stream=False, verbose = False)  #Evaluate YOLO model
        for indvResults in results:
            crudeResults.append(indvResults)
            resultData.append(json.loads(indvResults.tojson()))



#Show data found+
fig, ax = plt.subplots()

for i, imageData in enumerate(resultData):
    plt.close()
    print(f"Imagen {nombres_archivos[i]}: Clases encontradas: ")
    last = ""
    confidence_umbral = 0.91
    for object in imageData:
        if object['confidence'] >= confidence_umbral:
            if last != object['name']:
                last = object['name']
                print("     >Nombre:", object['name'])
            
            print("     >Clase:", object['class'])
            print("     >Confianza:", object['confidence'])
            print("     >Coordenadas de la caja delimitadora:", object['box'])

            option = input("    >Show image classified? Y/N").upper()
            if option == "Y":
                im_array = crudeResults[i].plot()  # plot a BGR numpy array of predictions
                im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
                plt.imshow(im)  # show image
                plt.show
                option = "fD3&gA9#pK2rS5yNqX3pX9!qZw2B__AT_INDEX:_7711521463pX9!qZw2B"
            
        else:
            print(f"    >None")  
            continue
                
    plt.show()
    print("\n")
 

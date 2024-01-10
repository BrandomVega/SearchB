from PIL import Image
from ultralytics import YOLO
import json 
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
sys.path.append(r'C:\Users\Brandom\Documents\1Proyecto')


from gui import selectDirectory as getDir

#Get directory to search
def searchDirectory():
    directoryPath = getDir.getDirectory()
    nombres_archivos = os.listdir(directoryPath)
    return directoryPath, nombres_archivos
#Apply model to each image
def runYolo(directoryPath, nombres_archivos):
    #model = YOLO("../weightsTrain1.pt")
    model = YOLO("./yolov8n.pt")
    
    resultFormatedData = []
    results  = []

    extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp']
    

    for nombre_archivo in nombres_archivos:
        ext = os.path.splitext(nombre_archivo)[-1].lower()
        if ext in extensiones_imagen:
            path = os.path.join(directoryPath, nombre_archivo)
            resultsModel = model(path, stream=False, verbose = False)  #Evaluate YOLO model
            for indvResults in resultsModel:
                results.append(indvResults)
                resultFormatedData.append(json.loads(indvResults.tojson()))

    return results, resultFormatedData
def processResults(resultData, nombres_archivos, objectsNLP, directoryPath):   
    bestCoincidence = {'img':"",'score':0,'yoloData': []}
    for i, imageData in enumerate(resultData):
        print(f"Imagen {nombres_archivos[i]}: Clases encontradas: \n")
        count = 0
        for object in imageData:
            if object['confidence'] >= confidence_umbral:
                print("     >Nombre:", object['name'])
                print("     >Clase:", object['class'])
                print("     >Confianza:", object['confidence'])
                print("     >Coordenadas de la caja delimitadora:", object['box'])
                print("\n")
                clase = object['name']
                for alterClass in objectsNLP:
                    if clase in alterClass:
                        count+=1
            else: 
                continue
        if count > bestCoincidence['score']:
            bestCoincidence['score']=count
            bestCoincidence['img']=os.path.join(directoryPath, nombres_archivos[i])
            bestCoincidence['yoloData']=resultData[i]
    return bestCoincidence


def showImage(data):
    results = data['yoloData'][0]
    image = data['img']
    class_name = results['name']
    confidence = results['confidence']
    box = results['box']

    # Display the information
    print(f"Class: {class_name}, Confidence: {confidence}")
    print(f"Bounding Box: {box}")

    # Assuming you have an image, you can display it using matplotlib
    fig, ax = plt.subplots()
    # Replace the following line with your actual image plotting code
    im_array = plt.imread(image)  
    plt.imshow(im_array)

    # Draw bounding box on the image
    rect = patches.Rectangle((box['x1'], box['y1']), box['x2'] - box['x1'], box['y2'] - box['y1'], linewidth=2, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

    # Display class name and confidence on the plot
    plt.text(box['x1'], box['y1'] - 5, f"{class_name} (Confidence: {confidence:.2f})", color='white', fontsize=10, backgroundcolor='red')

    plt.show()
    
def plot_bounding_boxes(resultsModel, image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Create a figure and axes
    fig, ax = plt.subplots(1)
    ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Matplotlib uses RGB, OpenCV uses BGR
    
    # Extract bounding box information from the resultsModel
    for result in resultsModel:
        class_id, confidence, (x, y, w, h) = result
        
        # Convert the box coordinates from YOLO format to corner coordinates
        x = int((x - w / 2) * image.shape[1])
        y = int((y - h / 2) * image.shape[0])
        w = int(w * image.shape[1])
        h = int(h * image.shape[0])
        
        # Create a Rectangle patch
        bbox = patches.Rectangle((x, y), w, h, linewidth=2, edgecolor='r', facecolor='none')
        
        # Add the patch to the Axes
        ax.add_patch(bbox)
        
        # Add label with class and confidence
        label = f"Class {class_id} ({confidence:.2f})"
        plt.text(x, y - 5, label, color='r', fontsize=8, backgroundcolor='none')

    # Show the image with bounding boxes
    plt.show()


confidence_umbral = 0.5
def main(objects):
    print("="*60)
    print("Processing into yolo")
    print("="*60)
    dir, files = searchDirectory()
    results, resultData= runYolo(dir, files)
    coincidence = processResults(resultData=resultData, nombres_archivos=files, objectsNLP=objects, directoryPath=dir)
    print("="*60)
    print("Resultado")
    print("="*60)

    if coincidence:
        showImage(coincidence)
    
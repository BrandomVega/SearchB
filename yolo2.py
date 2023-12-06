from PIL import Image
from ultralytics import YOLO

from gui import selectDirectory as getDir
import os


model = YOLO('yolov8n.pt')




directoryPath = getDir.getDirectory()
print(directoryPath)



extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp']


nombres_archivos = os.listdir(directoryPath)

for nombre_archivo in nombres_archivos:

    ext = os.path.splitext(nombre_archivo)[-1].lower()

    if ext in extensiones_imagen:
        path = directoryPath + "\\" +nombre_archivo
        results = model(path)  # results list
        for r in results:
            r.save_txt(txt_file=r"C:\Users\Brandom\Documents\1Proyecto\yoloResults")

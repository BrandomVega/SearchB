from ultralytics import YOLO
import pandas
import PIL
import json 
# Load a model
model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model

# Run batched inference on a list of images
results = model(['target\computers.jpg', 'target\perro.jpg',"target\limon.jpg"], stream=True)  # return a list of Results objects


resultData = []

for r in results:
    resultData.append(json.loads(r.tojson()))
    

print(resultData)
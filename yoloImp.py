from ultralytics import YOLO
import pandas
import PIL
# Load a model
model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model

# Run batched inference on a list of images
results = model(['target\computers.jpg', 'target\perro.jpg',"target\limon.jpg"], stream=True)  # return a list of Results objects

for r in results:
    print(r.tojson())
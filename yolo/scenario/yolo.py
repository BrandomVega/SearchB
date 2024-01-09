#This file pretends to test the training open image dataset
#Hopefully i can train scene detection with this model and to fully understand what this is capapble of 
from ultralytics import YOLO

import os


def main():
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Or the GPU index you want to use

    myModel = r"C:\Users\Brandom\Documents\1Proyecto\yolo\scenario\runs\detect\train\weights\best.pt"

    print("Init ...")
    model = YOLO(myModel)
    print("Model...")
    results = model.train(data="myDataset.yaml", epochs=2, device='0')


if __name__ == '__main__': #torch bugs if i dont put this 
    main()
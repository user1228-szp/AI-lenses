#Just to detect blocks in the image, in the command window are the results
import cv2
import matplotlib.pyplot as plt
import numpy as np
from ultralytics import YOLO

def process_image_2(image_path, model_path):
    # Cargar el modelo YOLOv8
    model = YOLO(model_path)

    # Cargar la imagen
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: no se pudo cargar la imagen en {image_path}")
        exit()

    # Realizar la predicción
    results = model(image)

    # Filtrar detecciones con confianza mayor a 0.5
    filtered_indices = np.where(results[0].boxes.conf.cpu().numpy() > 0.5)[0]

    # Obtener las cajas correspondientes a las detecciones filtradas
    boxes = results[0].boxes.xyxy.cpu().numpy()[filtered_indices].astype(int)

    # Dibujar las detecciones en la imagen
    for (xmin, ymin, xmax, ymax) in boxes:
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color=(0, 255, 0), thickness=2)

    # Mostrar la imagen usando matplotlib
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

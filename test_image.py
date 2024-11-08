# Solo para detectar bloques en la imagen; los resultados se mostrarán en la ventana de comandos
import cv2
import matplotlib.pyplot as plt
import numpy as np
from ultralytics import YOLO

def process_image_2(image_path, model_path):
    # Cargar el modelo
    model = YOLO(model_path)    
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: no se pudo cargar la imagen en {image_path}")
        return []  
    results = model(image)
    detections = []
    
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            class_name = model.names[class_id]
            confidence = float(box.conf)
            
            detections.append({
                "class_name": class_name,
                "confidence": confidence   
            })
    filtered_indices = np.where(results[0].boxes.conf.cpu().numpy() > 0.5)[0]
    boxes = results[0].boxes.xyxy.cpu().numpy()[filtered_indices].astype(int)

    for (xmin, ymin, xmax, ymax) in boxes:
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color=(0, 255, 0), thickness=2)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
    
    return detections


# analyze_image.py
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

def process_image(image_path, model_path):
    model = YOLO(model_path)
    image = cv2.imread(image_path)

    # Verifica si la imagen se cargó correctamente
    if image is None:
        print("Error: No se pudo cargar la imagen.")
        return []  # Devuelve una lista vacía si la imagen no se carga

    results = model(image)
    detections = []

    # Extrae información sobre cada detección
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)  
            class_name = model.names[class_id]
            confidence = float(box.conf)
              
            detections.append({
                "class_name": class_name,
                "confidence": confidence   
            })
             
    annotated_image = results[0].plot()
    plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    return detections  

            

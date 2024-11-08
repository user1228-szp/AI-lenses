# analyze_image.py
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
from collections import Counter

def process_image(image_path, model_path):
    model = YOLO(model_path)
    image = cv2.imread(image_path)

    if image is None:
        print("Error: No se pudo cargar la imagen.")
        return ""

    results = model(image)
    detections_summary = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            class_name = model.names[class_id]
            detections_summary.append(class_name)

    # Agrupar y contar los objetos detectados
    counts = Counter(detections_summary)
    summary_text = ", ".join(f"{count} {name}" for name, count in counts.items())

    # Mostrar la imagen con anotaciones
    annotated_image = results[0].plot()
    plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    return summary_text  # Asegúrate de que esta línea está aquí



            
    plt.show()

    return detections  

            

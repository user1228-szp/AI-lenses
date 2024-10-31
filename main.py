import sys
sys.path.append(r'path')

from analyze_image import process_image 
from test_image import process_image_2
from analyze_video import process_video
from voz import read_text, initialize_engine, speak

image_path = r"pathh_image"
video_path = r"path_video"

model_path = 'yolov8s.pt'

def main():
    engine = initialize_engine()
    breakpoint
    # Menú interactivo
    print("Selecciona una opción:")
    print("1. Imagen guardada con identificación")
    print("2. Imagen guardada sin identificación")
    print("3. Video guardado")
    print("4. Voz")
    print("5. Salir")
    
    option = input("\n>> ")

    if option == '1':
        speak("imagen con identificación", engine)
        detections = process_image(image_path, model_path)
                
        if detections:
            for detection in detections:
                name = detection["class_name"]
                confidence = detection["confidence"]
                print(f"Objeto detectado: {name} con precisión de {confidence:.2f}")
                speak(f"objetc {name} with precisión {confidence:.2f}", engine)

    elif option == '2':
        speak("imagen sin identificación", engine)
        process_image_2(image_path, model_path)

    elif option == '3':
        speak("Video guardado", engine)
        process_video(video_path, model_path)
        
    elif option == '4':
        speak("prueba voz", engine)
        read_text()
        
        
    elif option == '5':
        speak("Programa terminado", engine)
        print("OFF")

    
    else:
        print("Again")
        speak("Again", engine)

if __name__ == '__main__':
    main()

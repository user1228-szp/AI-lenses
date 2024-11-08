import sys
sys.path.append(r'path')

from collections import Counter

from analyze_image import process_image 
from test_image import process_image_2
from analyze_video import process_video
from analyze_video_2 import process_video_2
from voice import read_text, initialize_engine, speak

image_path = r"path imagen_2.jpg"
video_path = r"path video_2.mp4"

model_path = 'model'

def main():
    engine = initialize_engine()
    breakpoint
    # Menú interactivo
    print("Selecciona una opción:")
    print("1. Imagen guardada con identificación")
    print("2. Imagen guardada sin identificación")
    print("3. Video guardado")
    print("4. video con identificación")
    print("5. Voz")
    print("6. Salir")
    
    option = input("\n>> ")

    if option == '1':
        speak("imagen con identificación", engine)
        detections_summary = process_image(image_path, model_path)  # Llama a process_image
        print(f"Objetos encontrados: {detections_summary}")  # Imprime el resumen aquí
        speak(f"Objets: {detections_summary}",engine)
        
        #####
        #if detections:
            #object_counts = {}
            #for detection in detections:
                #name = detection["class_name"]
                #confidence = detection["confidence"]
                #print(f"object: {name} with precision {confidence:.2f}")
                #speak(f"object {name} with precision {confidence:.2f}", engine)
        #####
        
                
    elif option == '2':
        speak("imagen sin identificación", engine)
        detections = process_image_2(image_path, model_path) or []  # Asigna una lista vacía si `None`
        
        #detection by one by in order 
        if detections:  
            for detection in detections:
                name = detection["class_name"]
                confidence = detection["confidence"]
                print(f"object: {name} with precision {confidence:.2f}")
                speak(f"object {name} with precision {confidence:.2f}", engine)
        
        
    elif option == '3':
        speak("Video guardado", engine)
        process_video(video_path, model_path)
        
    elif option == '4':
        speak("Video guardado con identificacion", engine)
        process_video_2(video_path, model_path)
    
    elif option == '6':
        speak("prueba voz", engine)
        read_text()
        
        
    elif option == '7':
        speak("Programa terminado", engine)
        print("OFF")

    
    else:
        print("Again")
        speak("Again", engine)

if __name__ == '__main__':
    main()


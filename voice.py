import pyttsx3

def initialize_engine(language_code="es"):
    """Inicializa el motor de síntesis de voz."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidad de la voz (150 palabras/minuto)
    engine.setProperty('volume', 1)  # Volumen de la voz (1 = máximo)
    
    for voice in engine.getProperty('voices'):
        if language_code in voice.languages or language_code in voice.id:
            engine.setProperty('voice', voice.id)
            break

    return engine

def speak(text, engine):
    engine.say(text)
    engine.runAndWait()
    
def read_text():
    """Inicializa el motor de voz y permite ingresar texto para procesarlo y leerlo en voz alta."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidad de la voz (150 palabras/minuto)
    engine.setProperty('volume', 1)  # Volumen máximo

    print("Ingresa un texto y presiona Enter (escribe 'salir' para terminar):")

    while True:
        user_input = input("\n>> ")

        if user_input.strip().lower() == "salir":
            print("¡Programa terminado!")
            engine.say("Programa terminado")
            engine.runAndWait()
            break

        upper_text = user_input.upper()
        print(f"\nTexto Original: {user_input}")
        print(f"Texto en Mayúsculas: {upper_text}")

        # Leer el texto en voz alta
        engine.say(upper_text)
        engine.runAndWait()

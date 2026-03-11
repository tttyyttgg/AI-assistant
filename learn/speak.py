import pyttsx3

def speak(text):
    """Speak the given text"""
    try:
        # Engine ko har baar initialize karna h
        engine = pyttsx3.init("sapi5")
        engine.setProperty('rate', 150)    # Speed
        engine.setProperty('volume', 1.0)  # Volume
        
        print(f"Speaking: {text}")
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        
    except Exception as e:
        print(f"Speak Error: {e}")
        print(f"[VOICE]: {text}")

import speech_recognition as sr

mic = sr.Microphone()
rec = sr.Recognizer()

def listen():
    """Listen to user voice and return text"""
    with mic as source:
        rec.adjust_for_ambient_noise(source, duration=1)
        audio = rec.listen(source)
    
    try:
        text = rec.recognize_google(audio)
        print(f"You: {text}")
        return text
    
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        return ""

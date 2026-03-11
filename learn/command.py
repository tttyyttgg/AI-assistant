import webbrowser
import time
from camera import camera
from speak import speak
from brain import brain

def command(text):
    """Process user commands"""
    text = text.lower()

    # YOUTUBE
    if "youtube" in text:
        print("Got it sir")
        time.sleep(0.5)
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # GOOGLE
    elif "google" in text:
        print("Got it sir")
        time.sleep(0.5)
        speak("Opening Google")
        webbrowser.open("https://google.com")

    # CHATGPT
    elif "chat" in text:
        print("Got it sir")
        time.sleep(0.5)
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    # GEMINI
    elif "gem" in text:
        print("Got it sir")
        time.sleep(0.5)
        speak("Opening Gemini")
        webbrowser.open("https://gemini.google.com/app/224c910c8238156f")

    # CLAUDE
    elif "claud" in text or "cloud" in text:
        print("Got it sir")
        time.sleep(0.5)
        speak("Opening Claude")
        webbrowser.open("https://claude.ai/chat/4d0264fc-003a-492d-b2fc-02a26c19cc13")

    # GENERAL OPEN
    elif "open camera" in text:
        print("Got it sir")
        time.sleep(0.5)
        speak("Opening camera ")
        camera()

    elif "off camera" in text or "close camera" in text:
        print("Got it sir")
        time.sleep(0.5)
        speak("closing camera ")
        off_camera()

    # NOT RECOGNIZED
    else:
        ai_reply = brain(text)
        print(ai_reply)
        speak(ai_reply)

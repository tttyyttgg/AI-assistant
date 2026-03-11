from listen import listen
from speak import speak
from command import command

if __name__ == "__main__":
    print("Voice Assistant Started!")
    speak("Initializing sir")
    
    # Continuous listening loop
    while True:
        print("\nListening...")
        text = listen()
        
        # If no text captured, continue listening
        if text == "":
            continue
        
        # Exit command
        if "exit" in text.lower() or "quit" in text.lower():
            speak("Goodbye sir")
            print("Shutting down...")
            break
        
        # Process the command
        command(text)
        

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()  # Creates a new Recognizer instance, which represents a collection of speech recognition functionality.
engine = pyttsx3.init()  # ise initial ho jayega

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # listen for the wake word "Jarvis"
        # Obtain auido from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                word = r.recognize_google(audio)
            if(word.lower() == "hello"):
                speak("yes how can i help you")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")

                    processCommand(command)
        

        except Exception as e:
            print("error : {0}".format(e))




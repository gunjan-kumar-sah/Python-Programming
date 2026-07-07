import speech_recognition as sr
import pyttsx3
import datetime
import os
import sys

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 17:
        speak("Good afternoon!")
    elif 17 <= hour < 22:
        speak("Good evening!")
    else:
        speak("Hello!")
    speak("I am your offline assistant. How can I help you today?")

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_sphinx(audio)  # Offline recognition
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
        return ""
    except sr.RequestError as e:
        speak("Speech recognition error; check your setup.")
        print(e)
        return ""

def process_command(command):
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "notepad" in command:
        speak("Opening Notepad")
        if sys.platform == "win32":
            os.system("notepad")
        elif sys.platform == "linux":
            os.system("gedit &")
        else:
            speak("Notepad is not supported on this OS.")
    elif "hello" in command or "hi" in command:
        speak("Hello! How can I assist you?")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I can't do that yet.")

# Main loop
if __name__ == "__main__":
    greet_user()
    while True:
        cmd = listen_command()
        if cmd:
            process_command(cmd)

import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib  # for sending emails
import speech_recognition as sr

USERNAME = "Elvis"
BOTNAME = "JARVIS"

# Set Talktime
try:
    engine = pyttsx3.init('espeak')
except ImportError:
    print("Error: espeak not installed or unable to initialize.")
    exit(1)
except RuntimeError:
    print("Error: Unable to initialize pyttsx3 with espeak.")
    exit(1)

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak(f"Good morning {USERNAME}!")
    elif 12 <= hour < 18:
        speak(f"Good afternoon {USERNAME}!")
    else:
        speak(f"Good evening {USERNAME}!")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()

    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that. Can you please repeat?")
        return "None"

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('elvismuhinyia8858@gmail.com', 'ec061796')  # Update with your email credentials
    server.sendmail('costelloelvis775@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wish_me()
    
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'Music'  # Update with your music directory
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, random.choice(songs)))
            else:
                speak("No music found in your directory.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "receiver-email@gmail.com"  # Update with recipient's email
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'quit' in query:
            speak("Goodbye, sir!")
            exit()

        elif 'joke' in query:
            jokes = ["Why was the math book sad? Because it had too many problems.",
                     "I told my wife she was drawing her eyebrows too high. She looked surprised.",
                     "Why don't scientists trust atoms? Because they make up everything."]
            speak(random.choice(jokes))

        else:
            speak("Sorry, I didn't understand that. Can you please repeat?")
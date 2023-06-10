import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 178)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning{username}")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon{username}")
    else:
        speak(f"Good Evening{username}")
    speak("I am Jarvis you voice assistant i will help you to make your work easy lets give a go  ")
speak("Please enter  you name before we start.")
username=input("Name:")

def takeCommand():
    #its take microphone input return output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Say that again please...")
        return takeCommand()
    return query
if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "what's your name" in query:
            speak(f'my name is Jarvis {username}')

        elif 'How much do you love me' in query:
            speak('Your the one i loved the most')
        elif 'Will  you love me' in query:
            speak('I Love you till the earth die')
        elif'how can you help me' in query:
            speak(f"I can make your work easy and efficiant!! is there any thing else {username}")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif "what's the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is:{strTime}")
            print(strTime)

        elif 'play music' in query:
            path="C:\\Users\\Charan N\\AppData\\Local\\Programs\\Resso\\Resso.exe"
            os.startfile(path)
        
        elif '' in query:
            speak(f"Here some information i get")
            path="https://www.google.com/search?q="+ query
            os.startfile(path)
            break
        
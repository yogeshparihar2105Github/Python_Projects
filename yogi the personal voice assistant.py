import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        print("Good Morining sir")
        speak("Good Morining sir")
    if hour>=12 and hour<18:
        print("Good Afternoon sir")
        speak("Good Afternoon sir")
    if hour >= 18 and hour < 0:
        print("Good Evening sir")
        speak("Good Evening sir")

    print("what can I do for you")
    speak("what can i do for you")

def takeCommand():
    #ye microphone se input lega

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Speak: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again...pleeeaassseee.......")
        return "None"

    return query



if __name__ == "__main__":

    wishMe()

    while True:
     if 1:
        query = takeCommand().lower()
        speak("you speak")
        speak(query)


    #yaha par hum lagayenge logic for executing task based on query

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            print("opening youtube...")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            print("opening google...")
            speak("opening google")

        elif 'play music' in query:
            music_dir = 'E:\\music\\new music'
            songs = os.listdir(music_dir)
            playing_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, playing_song))
            #print(songs)
            #os.startfile(os.path.join(music_dir, songs[1]))
            print("playing music...")
            speak("playing music")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is{strTime}")
            print(strTime)

        elif 'open chrome' in query:
            chromePath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
            print("opening chrome...")
            speak("opening chrome")

        elif "who are you" in query:
            print("I am yogi the virtual assistant of Mr.Yogesh Parihar")
            speak("I am yogi the virtual assistant of Mr.Yogesh Parihar")

        elif "how are you" in query:
            speak("I am fine How are you by the way")
            print("I am fine How are you by the way")

        elif "what are you doing" in query:
            speak("I am waiting for you")
            print("I am waiting for you")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'quit' in query:
            print("Bye Bye! ")
            speak("Bye Bye! ")
            exit()


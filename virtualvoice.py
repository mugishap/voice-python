import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

filename = 'no-thats-not-gonna-do-it.wav'

with sr.AudioFile(filename) as source:

    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)

    friend = pyttsx3.init()
    voices = friend.getProperty('voices')
    friend.setProperty('rate', 150)
    friend.setProperty('voice', voices[2].id)
    friend.say(text)
    friend.runAndWait()
    friend.stop()

    
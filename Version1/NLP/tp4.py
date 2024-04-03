import pyttsx3
from tp3 import *
from tp2 import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


query = voice_recognition()
text = search(query)
speak(text)
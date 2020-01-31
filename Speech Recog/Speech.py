import speech_recognition as sr
import sounddevice as sd
from scipy.io import wavfile
import numpy as np

#r.recognize_google(audio, language="fr-FR") french example
mic = sr.Microphone()

r = sr.Recognizer()

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
try:
    print(r.recognize_google(audio))
except sr.RequestError:
    print('Connection to API failed')
    
except sr.UnknownValueError:
    print('Unable to recognize speech')

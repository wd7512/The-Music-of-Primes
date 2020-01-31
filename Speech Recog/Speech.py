import speech_recognition as sr
import sounddevice as sd
from scipy.io import wavfile
import numpy as np

#r.recognize_google(audio, language="fr-FR") french example


r = sr.Recognizer()

'''
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
'''

def convert_speech(source):

    output = False
    
    try:
        output = r.recognize_google(audio)
        
    except sr.RequestError:
        print('Connection to API failed')
    
    except sr.UnknownValueError:
        print('Unable to recognize speech')

    return output    
    
audio_file = sr.AudioFile('basic.wav')
with audio_file as source:
    audio = r.record(source)




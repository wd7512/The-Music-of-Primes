import speech_recognition as sr
import sounddevice as sd
from scipy.io import wavfile
import numpy as np
import time

#r.recognize_google(audio, language="fr-FR") french example




def convert_speech(audio):
    r = sr.Recognizer()

    output = False
    
    try:
        output = r.recognize_google(audio)
        
    except sr.RequestError:
        print('Connection to API failed')
    
    except sr.UnknownValueError:
        print('Unable to recognize speech')

    return output    

def existing_audio(filename):
    r = sr.Recognizer()
    audio_file = sr.AudioFile(filename)
    with audio_file as source:
        audio = r.record(source)

    return audio

def using_mic():

    r = sr.Recognizer()
    mic = sr.Microphone()
    
    countdown = 3
    for i in range(countdown):
        print('Speak in '+str(countdown-i))
        time.sleep(1)
    print('Mic on')
    
    
    with mic as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    print('Mic off')

    return audio


convert_speech(using_mic())

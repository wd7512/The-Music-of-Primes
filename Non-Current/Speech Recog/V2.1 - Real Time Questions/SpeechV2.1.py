import speech_recognition as sr
import sounddevice as sd
from scipy.io import wavfile
import numpy as np
import time
import googletrans

#r.recognize_google(audio, language="fr-FR") french example


def convert_speech(audio,lang):
    r = sr.Recognizer()

    output = False
    
    try:
        
        output = r.recognize_google(audio, language=lang)
        
    except sr.RequestError:
        print('Connection to API failed')
    
    except sr.UnknownValueError:
        print('Unable to recognize speech')

    return output    

def using_mic():

    r = sr.Recognizer()
    mic = sr.Microphone()
    
    countdown = 3
    for i in range(countdown):
        time.sleep(1)
        print('Speak in '+str(countdown-i))
        
    print('Mic on')
    
    
    with mic as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    print('Mic off')

    return audio

def demo():

    
                 
    answers = []
    
    Langs = ['Language,languageCode,Language (English name)', 'Afrikaans (Suid-Afrika),af-ZA,Afrikaans (South Africa)', 'Bahasa Indonesia (Indonesia),id-ID,Indonesian (Indonesia)', 'Bahasa Melayu (Malaysia),ms-MY,Malay (Malaysia)', 'Català (Espanya),ca-ES,Catalan (Spain)', 'Ceština (Ceská republika),cs-CZ,Czech (Czech Republic)', 'Dansk (Danmark),da-DK,Danish (Denmark)', 'Deutsch (Deutschland),de-DE,German (Germany)', 'English (Great Britain),en-GB,English (United Kingdom)', 'Español (España),es-ES,Spanish (Spain)', 'Euskara (Espainia),eu-ES,Basque (Spain)', 'Filipino (Pilipinas),fil-PH,Filipino (Philippines)', 'Français (France),fr-FR,French (France)', 'Galego (España),gl-ES,Galician (Spain)', 'Hrvatski (Hrvatska),hr-HR,Croatian (Croatia)', 'IsiZulu (Ningizimu Afrika),zu-ZA,Zulu (South Africa)', 'Íslenska (Ísland),is-IS,Icelandic (Iceland)', 'Italiano (Italia),it-IT,Italian (Italy)', 'Latviešu (latviešu),lv-LV,Latvian (Latvia)', 'Lietuviu (Lietuva),lt-LT,Lithuanian (Lithuania)', 'Magyar (Magyarország),hu-HU,Hungarian (Hungary)', 'Nederlands (Nederland),nl-NL,Dutch (Netherlands)', 'Polski (Polska),pl-PL,Polish (Poland)', 'Português (Portugal),pt-PT,Portuguese (Portugal)', 'Româna (România),ro-RO,Romanian (Romania)', 'Slovencina (Slovensko),sk-SK,Slovak (Slovakia)', 'Slovenšcina (Slovenija),sl-SI,Slovenian (Slovenia)', 'Urang (Indonesia),su-ID,Sundanese (Indonesia)', 'Swahili (Tanzania),sw-TZ,Swahili (Tanzania)', 'Swahili (Kenya),sw-KE,Swahili (Kenya)', 'Suomi (Suomi),fi-FI,Finnish (Finland)', 'Svenska (Sverige),sv-SE,Swedish (Sweden)', 'Türkçe (Türkiye),tr-TR,Turkish (Turkey)']
    for i in range(len(Langs)):
        line = Langs[i].split(',')
        flan = line[0]
        elan = line[2]
        spaces = ''
        for k in range(30-len(flan)):
            spaces = spaces + ' '
        if i < 10:
            print('('+str(i)+')  '+flan + spaces + elan)
        else:
            print('('+str(i)+') '+flan + spaces + elan)

    
    lan_code = Langs[int(input('\nWhich language is needed?(number): '))].split(',')[1]
    #print(lan_code)

    keep_going = 'y'
    first_q = ask_ques()
    questions = [first_q]

    while keep_going == 'y':
        ans = question(questions[-1],lan_code)
        answers.append(ans)
        keep_going = str(input('Do you want to ask another? (y/n): '))
        if keep_going == 'y':
            
            questions.append(ask_ques())
        else:
            pass



    return answers,questions

def ask_ques():
    
    check = 'n'
    while check == 'n':
        quest = str(input('Question: '))
        check = str(input('You want to ask:\n'+quest+'\n\nis this correct? (y/n):'))

    return quest

def question(ques,lan):
    t = googletrans.Translator()
    new_ques = t.translate(ques,src='en',dest=lan[:2])
    
    print('\nQuestion for patient:\n'+str(new_ques.text))

    
    sp_out = False
    while sp_out == False:
        cont = input('\nPress enter to start:')
        sp_out = convert_speech(using_mic(),lan)
        if sp_out == False:
            pass
        else:
            t_var = t.translate('Is this correct? (1=yes,0=no):',src='en',dest=lan[:2])
            corr = int(input('\n'+sp_out+'\n'+t_var.text))
            
            if corr == 0:
                sp_out = False
            else:
                pass
        
    #print('Patient Said: '+str(sp_out))

    en_out = t.translate(sp_out,src=lan[:2],dest='en')
    output = en_out.text
    print("Patient Said: "+str(output)+' ('+str(sp_out)+')')
    return str(output)
    



out = demo()
print('\n####Final Report####\n')
output = zip(out[1],out[0])


f = open('Report.csv','w')
f.write('Question,Answer\n')
for o in output:
    line = str(o)
    print(line)
    f.write(line[1:-1]+'\n')
f.close()




end = input('Press enter to quit:')
quit()

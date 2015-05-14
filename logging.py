#!python3

import time

def log_it(log_text):
    print( time.strftime("%d-%m-%Y %H:%M:%S") + " | " + log_text )
    with open("log.txt", "a") as log_file:
    log_file.write( time.strftime("%d-%m-%Y %H:%M:%S") + " | " + log_text )

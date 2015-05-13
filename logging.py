#!python3

import time

def cmd_log(log_text):
  print( time.strftime("%d-%m-%Y %H:%M:%S") + " | " + log_text )

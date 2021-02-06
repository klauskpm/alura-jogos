import os
import time
from collections import defaultdict
from sys import argv

DEBUG_MODE = 'debug' in argv[1:]

def sleep(seconds):
    if (not DEBUG_MODE):
        time.sleep(seconds)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def normalize(word):
    return word.strip().upper()

import os
import time
import playsound
import speech_recognition as sr
from gtts import *

filename = 'voice.mp3'
def say(text):
    tts = gTTS(text=text, lang='en-uk')
    tts.save(filename)
    playsound.playsound(filename)

say('Welcome to bob voice assistant')
os.remove('voice.mp3')

import VoiceAssistant

import os
import time
import playsound
import speech_recognition as sr
import random
from gtts import *
import Admin
import sys
import subprocess
from datetime import datetime

def say(text):
    tts = gTTS(text=text, lang='en-uk')
    fname = random.randint(1, 10000)
    filename = 'voice%s.mp3'% fname
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('Error!')
    return said
while True:
    print('listening...')
    time.sleep(1)
    get_audio()
    text = get_audio()
    if 'hello' in text:
        say('Hello user')

    elif 'what can you do' in text:
        say('I can do anything!')

    elif 'what languages' in text:
        say('i know english and nothing more')

    elif 'time' in text:
        now = datetime.now()
        current_time = now. strftime("%H hours %M minutes")
        say("The current time is %s"% current_time)
    elif 'what day' in text:
        d = datetime.today()
        today = d.strftime('%dth - %m - %y20 ')
        say(today)
    elif 'a joke' in text:
        nm = random.randint(1, 5)
        if nm == 1:
            say('Why did the chicken cross the road?')
            time.sleep(1)
            say('Because it wanted to get to the other side')
        if nm == 2:
            say('What do you get when you cross a vampire with a snowman?')
            time.sleep(1)
            say('Frostbite!')
        if nm == 3:
            say('What do you call a can opener that doesn’t work?')
            time.sleep(1)
            say('A can’t opener!')
        if nm == 4:
            say('Did you hear about the Italian chef who died?')
            time.sleep(1)
            say('He pasta-way!')
        if nm == 5:
            say('I sold my vacuum the other day')
            time.sleep(1)
            say('All it was doing was collecting dust')
    elif 'a fact' in text:
        nmf = random.randint(1, 10)
        if nmf == 1:
            say("North Korea and Cuba are the only places you can't buy Coca-Cola")
        if nmf == 2:
            say('The hottest chili pepper in the world is so hot it could kill you')
        if nmf == 3:
            say('More people visit France than any other country')
        if nmf == 4:
            say("The world's most densely populated island is the size of two football fields")
        if nmf == 5:
            say("There are only three countries in the world that don't use the metric system")
        if nmf == 6:
            say("The longest place name on the planet is 85 letters long")
        if nmf == 7:
            say("Did you know that bob assistant is better than any other voice assistant")
        if nmf == 8:
            say("Four babies are born every second")
        if nmf == 9:
            say("Japan is the world's most earthquake prone country")
        if nmf == 10:
            say("Only two countries use purple in their national flags")
    elif 'who let the dogs out' in text:
        say('Who, who, who')
    elif 'I love you' in text:
        say('I know you do')
    elif 'talk to me' in text:
        say('Im sorry, im not a human so i cant do that')
    elif 'a good boy' in text:
        say('Ollie is')
    else:
        say('I dont know how to do that')

#from jmespath import search
import speech_recognition as sr
import webbrowser
import time 
import random
import os
from gtts import gTTS
import playsound
from time import ctime
r=sr.Recognizer()
def record_audio(ask= False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        voice_data= ''
        audio=r.listen(source)
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, i did not hear that! ')
        except sr.RequestError:
            speak('Sorry my speech service is down!')
        return voice_data
def speak(audio_string):
    tts=gTTS(text=audio_string, lang='en')
    r=random.randint(1, 1000000)
    audio_file='audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
def respond(voice_data):
    if 'what is your name' in voice_data:
        speak("My name is none")
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'who created you' in voice_data:
        speak("god")
    if 'search' in voice_data:
        search=record_audio('what do you want to search')
        url='https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak("Here is what i found for: "+ search)
    if 'find location' in voice_data:
        location=record_audio('What do you want to find')
        url='https://google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak("Here is location of : "+ location)
    if 'stop' in voice_data:
        exit()
time.sleep(1)
speak('How can i help you')
while 1:
    voice_data=record_audio()
    respond(voice_data)
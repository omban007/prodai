#!/usr/bin/env python3                                                                                

import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
print ("say something2")
with sr.Microphone() as source:                # use the default microphone as the audio source
    r.adjust_for_ambient_noise(source)  # here
    print ("say something3")
    audio = r.listen(source,timeout=3)
try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

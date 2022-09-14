import language_tool_python

import sys 

from textblob import TextBlob

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Now Speak :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")

a=text

print("original text: "+str(a))

b = TextBlob(a)

# prints the corrected spelling
print("corrected text: "+str(b.correct()))
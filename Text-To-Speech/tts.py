from gtts import gTTS
import os

g = input("Hey, What do you want me to Speak?\n") 
text=g
language='en'
speech=gTTS(text= text, lang = language,slow = False)
speech.save("test.mp3")
os.system("start test.mp3")
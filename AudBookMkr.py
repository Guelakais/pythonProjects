#!/usr/bin/env python
# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os
from pathlib import Path

def inputManager():
    while 1:
        userInput = input("Hello, I'm here to help you to convert a text files to audio files. \n Please tell me the path of your File: ")
        my_file = Path(userInput)
        if my_file.is_file():
            userInput2 = input("Where do you want to save the file? [/path/Filename] \n Disclaimer: Ending is always mp3 ")
            AudBookMkr(userInput, userInput2+".mp3")
            break
        else:
            print("no such path found, please try again")

def AudBookMkr(file, audio):
    with open(file, "r") as fh:
        output = gTTS(text=fh.read().replace("\n", " "), lang='en', slow=False)
        output.save(audio)

inputManager()
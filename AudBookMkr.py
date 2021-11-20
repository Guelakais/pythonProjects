# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os
from pathlib import Path

def inputManager():
    while True:
        userInput = input("Hello, I'm here to help you to convert a text files to audio files. \n Please tell me the path of your File: ")
        my_file = Path(userInput)
        if my_file.is_file():
            userInput2 = input("Where do you want to save the file? [/path/Filename] \n Disclaimer: Ending is always mp3 ")
            end = ".mp3"
            realOutput = userInput2 + end
            AudBookMkr(userInput, realOutput)
            break
        else:
            print("no such path found, please try again")

def AudBookMkr(file, audio):
    fh = open(file, "r")
    myText = fh.read().replace("\n", " ")
    # Language we want to use 
    language = 'en'
    output = gTTS(text=myText, lang=language, slow=False)
    output.save(audio)
    fh.close()

inputManager()
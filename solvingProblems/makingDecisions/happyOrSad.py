#!/usr/bin/env python
#dmoj = ccc15j2

def happyOrSad(sentence):
    return 'none' if(
        emojiValidater(sentence)==False
    )else 'happy' if(
        emojiCount(sentence)>0
    )else 'sad' if(
        emojiCount(sentence)<0
    ) else 'unsure'

def emojiCount(sentenceI):
    return sentenceI.count(':-)')-sentenceI.count(':-(')

def emojiValidater(letter):
    return letter.count(':-)') != 0 or letter.count(':-(') != 0

print(happyOrSad(input()))
#!/usr/bin/env python
#import module
from tkinter import *

# initialize window
root = Tk()
root.geometry('300x300')
root.title('DataFlair-Mad Libs Generator')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
Label(root, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)


################Stories##############

def madlib1():

    print(
        f"say {input('food name: ')}, the photographer said as the camera flashed! "\
        f"{input('enter a name: ')} and I had gone to {input('enter a place name: ')}"\
        " to get our photos taken today. The first photo we really wanted was a picture"\
        f" of us dressed as {input('enter a animal name : ')} pretending to be a "\
        f"{input('enter a profession name: ')} .when we saw the second photo, it was"\
        f" exactly what I wanted. We both looked like {input('enter a thing name: ')}"\
        f" wearing {input('enter a piece of cloth name: ')} and {input('enter a verb in ing form: ')}"\
        f" --exactly what I had in mind"
        )



def madlib2():

    print(
        f"Last night I dreamed I was a  {input('enter a adjactive : ')}  butterfly with"\
        f"  {input('enter a color name : ')}  splocthes that looked like {input('enter a person name : ')}  .I flew"\
        f" to  {input('enter a place name : ')}  with my bestfriend and {input('enter a person name : ')}  who was a"\
        f" {input('enter adjective : ')}   {input('enter a insect name : ')} .We ate some"\
        f"  {input('enter a food name : ')}  when we got there and then decided to {input('enter a verb name : ')}"\
        f"  and the dream ended when I said-- lets  {input('enter a verb name : ')} ."
        )
    


def madlib3():
   
    print(
        f"Today we picked apple from {input('enter person name: ')}s Orchard."\
        f" I had no idea there were so many different varieties of apples. I ate {input('enter color : ')}"\
        f" apples straight off the tree that tested like {input('enter food name: ')}. Then there was a"\
        f" {input('enter aa adjective name: ')} apple that looked like a {input('enter a thing name : ')}"\
        f".When our bag were full, we went on a free hay ride to {input('enter place : ')} and back. It ended"\
        f" at a hay pile where we got to {input('enter verb : ')} {input('enter adverb : ')}. I can hardly wait"\
        f" to get home and cook with the apples. We are going to make appple {input('enter food name : ')} and {input('enter a thing name : ')} pies!."
        )  



######buttons   
#Button(root, text= 'The Photographer', font ='arial 15', command= madlib1(), bg = 'ghost white').place(x=60, y=120)
#Button(root, text= 'apple and apple', font ='arial 15', command = madlib3() , bg = 'ghost white').place(x=70, y=180)
#Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2(), bg = 'ghost white').place(x=80, y=240)
madlib1()
root.mainloop()

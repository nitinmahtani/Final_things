import cv2
###############################################################################
# Part 1 - collecting speech
################################################################################

def speech_recognition():
    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak to me :")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))

    except:
        print("Sorry could not recognize what you said")





###############################################################################
# Part 2 - GUI, takes in speech
###############################################################################
from tkinter import *


def create_menu():
    root = Tk()
    top_frame = Frame(root)
    top_frame.pack(side=TOP)
    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM)

    text_menu1 = Label(top_frame, text="Type to Translate: ")

    text_menu2 = Label(bottom_frame, text="or Record to Translate:")

    start_button = Button(bottom_frame, text="Start", fg='black',
                          command = speech_recognition)

    text_menu1.pack(side=TOP)

    text_menu2.pack(side=TOP)
    start_button.pack(side=BOTTOM)

    root.mainloop()


def create_video():
    vid_obj = make_video()
    root = Tk()
    frame = Frame(root)
    frame.pack()

    canvas = Canvas(frame, height=900, width=900)
    canvas.create_window(0, 0)
    canvas.pack()

    root.mainloop()
    replay_or_menu()


def replay_or_menu():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    button_replay = Button(frame, text='Replay', command=create_video)
    button_menu = Button(frame, text=' Menu ', fg='black', command=create_menu)

    button_replay.pack(side=LEFT)
    button_menu.pack(side=LEFT)

    root.mainloop()

##############################################################################
# Part 3 - compiling videos based on text (main program)
###############################################################################
import os

# this function takes input from the text-to-speech function:
def video_file_maker(text1: str):
    sid = 'qwertyuiopasdfghjklzxcvbnm'
    f = open('files_to_stitch.txt', 'w+')
    text1.strip('.')
    for letter in text1:
        char = letter.lower()
        if char in sid:
            f.write("file '{}.mp4'\n".format(char))
        else:
            print("Not a recognised character")
    f.close()


def make_video():
    os.system(r'cmd /c "cd C:\Users\nitin\Documents\csc148\Final_things"')
    os.system(r'ffmpeg -f concat -i files_to_stitch.txt -c copy output.mp4')
    return cv2.VideoCapture("output.mp4")

if __name__ == '__main__':

    print("Enter a string: ")
    x = input()
    video_file_maker(x)
    # os.system(r'cmd /c "cd C:\Users\nitin\Documents\csc148\Final_things"')
    # os.system(r'ffmpeg -f concat -i files_to_stitch.txt -c copy output.mp4')

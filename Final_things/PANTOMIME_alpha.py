from tkinter import *
import cv2
import os

root1 = Tk()
global_text = ''
replay0_menu1 = 0


# FIRST STEP - OPEN MENU
def create_menu():
    frame = Frame(root1)
    frame.pack(side=TOP)
    photo = PhotoImage(file='output-onlinepngtools.png')
    text_menu2 = Label(frame, text="Record to Translate:")

    # start button will listen
    start_button = Button(frame, text="Start", fg='black',
                          image=photo,
                          command=listen)
    close_button = Button(frame, text='Close', fg='black',
                          command=root1.destroy)
    start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
    close_button.pack(side=BOTTOM)
    text_menu2.pack(side=TOP)
    start_button.pack(side=TOP)

    root1.attributes("-fullscreen", True)

    root1.mainloop()


# SECOND STEP - LISTEN
def listen():
    root1.quit()
    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak to me :")
        audio = r.listen(source)

    try:
        global global_text
        text = r.recognize_google(audio)
        global_text = text
        print("You said : {}".format(text))



    except:
        print("Sorry could not recognize what you said")


# THIRD STEP - CREATE THE LIST OF VIDEOS AND GET VIDEO OBJ

def video_file_maker(text1: str):
    text1 = text1.lower()
    sid = 'qwertyuiopasdfghjklzxcvbnm'
    f = open('../Final_things/files_to_stitch.txt', 'w+')
    text1.strip('.')
    i = 0
    if text1 == 'hello welcome to new hacks':
        f.write("file '{}.mp4'\n".format('hello'))
        f.write("file '{}.mp4'\n".format('welcome'))
        text1 = 'new hacks'
    if len(text1) > 5 and text1[:5] == 'hello':
        f.write("file '{}.mp4'\n".format('hello'))
        text1 = text1[5:]
    if len(text1) > 7 and text1[:7] == 'welcome':
        f.write("file '{}.mp4'\n".format('welcome'))
        text1 = text1[7:]
    if text1 == 'hello':
        f.write("file '{}.mp4'\n".format('hello'))
        text1 = ''
    if text1 == 'hi':
        f.write("file '{}.mp4'\n".format('hello'))
        text1 = ''
    if text1 == 'welcome':
        f.write("file '{}.mp4'\n".format('welcome'))
        text1 = ''
    if text1 == 'how are you':
        f.write("file '{}.mp4'\n".format('howareyou'))
        text1 = ''
    if text1 == 'hello welcome':
        f.write("file '{}.mp4'\n".format('hello'))
        f.write("file '{}.mp4'\n".format('welcome'))
        text1 = ''

    while i < len(text1):
        # if len(text1) <= i + 5 and text1[i: i + 6] == 'hello':
        #     f.write("file '{}.mp4'\n".format('hello'))
        #     text1 = text1[:i] + text1[i + 5:]
        # if len(text1) < i + 2 and text1[i: i + 2] == 'hi':
        #     f.write("file '{}.mp4'\n".format('hello'))
        #     text1 = text1[:i] + text1[i+2]
        # if len(text1) < i + 11 and text1[i: i + 11] == 'how are you':
        #     f.write("file '{}.mp4'\n".format('howareyou'))
        #     text1 = text1[:i] + text1[i + 11]
        char = text1[i].lower()
        if char in sid:
            f.write("file '{}.mp4'\n".format(char))
        else:
            print("Not a recognised character")
        if char == ' ':
            f.write("file '{}.mp4'\n".format('space'))
        i = i + 1

    f.close()


# FOURTH STEP - MAKE THE VIDEO, PUT IT IN AN OBJ

def make_video():
    os.system(r'cmd /c "cd C:\Users\nitin\Documents\csc148\Final_things"')
    os.system(r'ffmpeg -f concat -i files_to_stitch.txt -c copy output.mp4')
    return cv2.VideoCapture("output.mp4")


# FIFTH STEP - TAKE THE VIDEO OBJ, MAKE THE VIDEO PANEL
def create_video_panel(vidobj):
    # root = Tk()
    # frame = Frame(root)
    # frame.pack()
    #
    # canvas = Canvas(frame, height=900, width=900)
    # canvas.create_window(0, 0)
    # canvas.pack()
    #
    # root.mainloop()
    # replay_or_menu()
    while True:
        ret, frame = vidobj.read()

        try:
            cv2.imshow('window', frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        except cv2.error:
            global vid
            cv2.destroyAllWindows()
            vid.release()
            if os.path.isfile('output.mp4'):
                os.remove("output.mp4")
            sys.exit()

            # create_menu()


# helper functions
#
# def keep_going_True():
#     global keep_going
#     keep_going = True
#
# def set_global_menu():
#     global replay0_menu1
#     replay0_menu1 = 1
#
#
# LAST STEP - REPLAY? OR MENU?
# def replay_or_menu():
#     root = Tk()
#     frame = Frame(root)
#     frame.pack()
#     button_replay = Button(frame, text='Replay', command= keep_going == True)
#     button_menu = Button(frame, text=' Menu ', fg='black', command= keep_going == False)
#
#     button_replay.pack(side=LEFT)
#     button_menu.pack(side=LEFT)
#
#     root.mainloop()


if __name__ == '__main__':
    create_menu()
    # print(global_text)
    video_file_maker(global_text)
    vid = make_video()
    create_video_panel(vid)

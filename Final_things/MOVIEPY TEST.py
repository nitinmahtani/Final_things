import os




# this function takes input from the text-to-speech function:
def stitch_video(text1: str, sid: str):
    f = open('files_to_stitch.txt', 'w+')
    text1.strip('.')
    for letter in text1:
        char = letter.lower()
        if char in sid:
            f.write("file '{}.mp4'\n".format(char))
        else:
            print("Not a recognised character")
    f.close()



if __name__ == '__main__':
    d = 'qwertyuiopasdfghjklzxcvbnm'
    print("Enter a string: ")
    x = input()
    stitch_video(x, d)
    os.system(r'cmd /c "cd C:\Users\nitin\Documents\csc148\Final_things"')
    os.system(r'ffmpeg -f concat -i files_to_stitch.txt -c copy output.mp4')

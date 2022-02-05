import time
import threading
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root = Tk()

root.title("Recorder")

C = Canvas(root,height=10,width=10)
filename = ImageTk.PhotoImage(Image.open(r'micro.jpg'))
background_label = Label(root,image=filename )
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack(side="bottom",)
root.geometry("350x370")

hour=StringVar()
minute=StringVar()
second=StringVar()
hour.set("00")
minute.set("00")
second.set("00")

Label(root,text="Voice Recorder",font=("Forte", 30),foreground='maroon').pack(pady=10)
hourEntry= Entry(root, width=3, font=("Arial",21,""),
				textvariable=hour)
hourEntry.place(x=120,y=125)

minuteEntry= Entry(root, width=3, font=("Arial",21,""),
				textvariable=minute)
minuteEntry.place(x=170,y=125)

secondEntry= Entry(root, width=3, font=("Arial",21,""),
				textvariable=second)
secondEntry.place(x=220,y=125)


def submit():
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    
    except:
        print("Please input the right value")
    while temp >-1:
        mins,secs = divmod(temp,60)
        hours=0
        if mins >60:
            hours, mins = divmod(mins, 60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        
        
        if (temp == 0):
            messagebox.showinfo("Saved", "RECORDING DONE\nSUCESSFULLY")
        temp -= 1
def voice():
    temp1 = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())

    import sounddevice
    from scipy.io import wavfile
    fs=44100
    print("Recording started.......\n")
    record=sounddevice.rec(int(temp1*fs),samplerate=fs,channels=2)
    sounddevice.wait()
    wavfile.write("out.wav",fs,record)
def stop():
    exit()
def sub():
    threading.Thread(target=voice).start()
    threading.Thread(target=submit).start()

btn = Button(root, text='START RECORDING', bd='5',font = ("Times New Roman", 11,'bold'),
			command= sub)
btn.place(x = 100,y = 250)
btn1 = Button(root, text='STOP', bd='5',font = ("Times New Roman", 11,'bold'),
			command= stop)
btn1.place(x = 160,y = 320)
root.mainloop()

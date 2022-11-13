import datetime
import winsound
from time import sleep
from tkinter import *
from tkinter import ttk


def alarm():
    while True:
        sleep(1)
        if datetime.datetime.now().strftime("%H:%M:%S") == \
                f"{hourTime.get()}:{minTime.get()}:{secTime.get()}":
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
 
def timer():
    sleep((((int(hour.get())*60) + int(Min.get()))*60) + int(sec.get()))
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)


if __name__ == '__main__':
    Root = Tk()
    Root.title("Clock")
    Root.geometry("250x200")
    TabControl = ttk.Notebook(Root)
    
    Tab1 = ttk.Frame(TabControl)
    Frame1 = Frame(Tab1)
    Label(Frame1, text="Hour : ").grid(row=0, column=0, padx=6)
    hourTime = Entry(Frame1, width=10)
    hourTime.grid(row=0, column=1, padx=1)
    Frame1.pack(side=TOP, anchor=N, padx=10, pady=2)

    Frame2 = Frame(Tab1)
    Label(Frame2, text="Minute : ").grid(row=0, column=0)
    minTime = Entry(Frame2, width=10)
    minTime.grid(row=0, column=1)
    Frame2.pack(side=TOP, anchor=N, padx=10, pady=2)
    
    Frame3 = Frame(Tab1)
    Label(Frame3, text="Second : ").grid(row=0, column=0)
    secTime = Entry(Frame3, width=10)
    secTime.grid(row=0, column=1)
    Frame3.pack(side=TOP, anchor=N, padx=10, pady=2)
    
    Button(Tab1, text="Set Alarm", fg="red", width=10, command=alarm)\
        .pack(side=TOP, anchor=N, padx=10, pady=5)
    TabControl.add(Tab1, text='Alarm Clock')

    Tab2 = ttk.Frame(TabControl)
    Frm1 = Frame(Tab2)
    Label(Frm1, text="Hour : ").grid(row=0, column=0, padx=6)
    hour = Entry(Frm1, width=10)
    hour.grid(row=0, column=1, padx=1)
    Frm1.pack(side=TOP, anchor=N, padx=10, pady=2)

    Frm2 = Frame(Tab2)
    Label(Frm2, text="Minute : ").grid(row=0, column=0)
    Min = Entry(Frm2, width=10)
    Min.grid(row=0, column=1)
    Frm2.pack(side=TOP, anchor=N, padx=10, pady=2)

    Frm3 = Frame(Tab2)
    Label(Frm3, text="Second : ").grid(row=0, column=0)
    sec = Entry(Frm3, width=10)
    sec.grid(row=0, column=1)
    Frm3.pack(side=TOP, anchor=N, padx=10, pady=2)

    Button(Tab2, text="Start Timer", fg="red", width=10, command=timer)\
        .pack(side=TOP, anchor=N, padx=10, pady=5)
    TabControl.add(Tab2, text='Timer')
    
    TabControl.pack(expand=1, fill=BOTH)
    Root.mainloop()

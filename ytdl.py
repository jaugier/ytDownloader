#!/usr/bin/env python

#(C) COPYRIGHT © Jordan "Shokk" Augier 2020
from tkinter import *
import tkinter as tk
import pytube
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
        
def go_download(vUrl):
        yt = pytube.YouTube(vUrl)
        print(yt.title)
        video = yt.streams.first()
        video.download()

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("500x500")
        self.title("Youtube Downloader")
        self.entry = tk.Entry(self)
        self.entry.place(x=240,y=130)
        self.button = tk.Button(self, text="Download", command=self.on_button,width=20,bg="black",fg='white').place(x=180,y=380)
        self.label = tk.Label(self, text="Video's URL", width=20,font=("bold",10))
        self.label.place(x=80,y=130)

    def on_button(self):
        print(self.entry.get())
        go_download(self.entry.get())

def main():
        if is_admin():
            app = SampleApp()
            app.mainloop()
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
if __name__ == "__main__":
    main()
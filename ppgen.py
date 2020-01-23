#!/usr/bin/env python

import Tkinter as tk
from efflist import words
import sys, random

class hzapp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        toolbar = tk.Frame(self)
        toolbar.pack(side="top")

        b9 = tk.Button(self, text="9 Words", height=2, width=10, relief ='flat', bg ='white', command=self.print_stdout9)
        b9.pack(in_=toolbar, side="top")
        b8 = tk.Button(self, text="8 Words", height=2, width=10, relief ='flat', bg ='white', command=self.print_stdout8)
        b8.pack(in_=toolbar, side="top")
        b7 = tk.Button(self, text="7 Words", height=2, width=10, relief ='flat', bg ='white', command=self.print_stdout7)
        b7.pack(in_=toolbar, side="top")
        b6 = tk.Button(self, text="6 Words", height=2, width=10, relief ='flat', bg ='white', command=self.print_stdout6)
        b6.pack(in_=toolbar, side="top")
        b5 = tk.Button(self, text="5 Words", height=2, width=10, relief ='flat', bg ='white', command=self.print_stdout5)
        b5.pack(in_=toolbar, side="top")
        b4 = tk.Button(self, text="4 Words", height=2, width=10, relief ='flat', bg ='white', command=self.print_stdout4)
        b4.pack(in_=toolbar, side="top")
        bquit = tk.Button(self, text="QUIT", height=2, width=10, relief ='flat', bg ='white', command=quit)
        bquit.pack(in_=toolbar, side="top")
        self.text = tk.Text()
        self.text.pack()
        sys.stdout = TextRedirector(self.text, "stdout")

    def print_stdout9(self):
        print ' '.join(random.sample(words, 9)) #random.sample unique elements/no repeats

    def print_stdout8(self):
        print ' '.join(random.sample(words, 8))

    def print_stdout7(self):
        print ' '.join(random.sample(words, 7))

    def print_stdout6(self):
        print ' '.join(random.sample(words, 6))

    def print_stdout5(self):
        print ' '.join(random.sample(words, 5))

    def print_stdout4(self):
        print ' '.join(random.sample(words, 4)

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="normal")

app = hzapp()
app.mainloop()
quit()

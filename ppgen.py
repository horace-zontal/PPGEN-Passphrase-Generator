#!/usr/bin/env python

import Tkinter as tk
import sys, random
from efflist import words

class hzapp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        toolbar = tk.Frame(self)
        toolbar.pack(side="top")
        b9 = tk.Button(self, text="9", height=2, width=10, relief ='flat', bg ='white', command=self.print_stdout9)
        b9.pack(in_=toolbar, side="left")
        b8 = tk.Button(self, text="8", height=2, width=10, relief ='flat', bg ='white', command=self.print_stdout8)
        b8.pack(in_=toolbar, side="left")
        b7 = tk.Button(self, text="7", height=2, width=10, relief ='flat', bg ='white', command=self.print_stdout7)
        b7.pack(in_=toolbar, side="left")
        b6 = tk.Button(self, text="6", height=2, width=10, relief ='flat', bg ='white', command=self.print_stdout6)
        b6.pack(in_=toolbar, side="left")
        bq = tk.Button(self, text="QUIT", height=2, width=10, relief ='flat', bg ='white', command=quit)
        bq.pack(in_=toolbar, side="right")
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

#!/usr/bin/env python

import Tkinter as tk
import sys, random
from efflist import words

class hzapp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        toolbar = tk.Frame(self)
        toolbar.pack(side="top")
        b1 = tk.Button(self, text="GENERATE", height=2, width=10, relief ='flat', bg ='white', command=self.print_stdout)
        b1.pack(in_=toolbar, side="left")
        b2 = tk.Button(self, text="QUIT", height=2, width=10, relief ='flat', bg ='white', command=quit)
        b2.pack(in_=toolbar, side="right")
        self.text = tk.Text()
        self.text.pack()
        sys.stdout = TextRedirector(self.text, "stdout")
        
    def print_stdout(self):
        print ' '.join(random.sample(words, 7)) #random.sample unique elements/no repeats

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

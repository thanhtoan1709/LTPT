import tkinter as tk
from tkinter import ttk
win = tk.Tk()
#title
win.title("Python Gui")
def click_me():
    action.configure(text="**I have been clicked")
    a_label.configure(foreground='red')
    a_label.configure(text='a Red Label')
#label
a_label=ttk.Label(win,text="A label")
a_label.grid(column=0,row=0)
#

#add button 
action = ttk.Button(win,text="click me !!!", command=click_me)
action.grid(column=1,row=0)
#end
win.mainloop()
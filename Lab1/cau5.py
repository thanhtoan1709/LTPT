import tkinter as tk
from tkinter import ttk
win = tk.Tk()
#title
win.title("Python Gui")
#label
ttk.Label(win,text="Enter A name").grid(column=0,row=0)
#def
def click_me():
    action.configure(text="Hello "+ name.get())
#button
action = ttk.Button(win,text="click me !!!", command=click_me)
action.grid(column=1,row=1)
#variable
name = tk.StringVar()
name_ent = ttk.Entry(win,width=12,textvariable=name)
name_ent.grid(column=0,row=1)
#end
win.mainloop()
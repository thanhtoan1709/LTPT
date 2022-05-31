import tkinter as tk
from tkinter import ttk
win = tk.Tk()
#title
win.title("Python Gui")
#label
ttk.Label(win,text="A label").grid(column=0,row=0)
#end
win.mainloop()
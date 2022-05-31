import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
win =tk.Tk()
win.title("Python Gui")
tabControl = ttk.Notebook(win)
#tab1
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1,text="tab_1")
tabControl.pack(expand=1,fill="both")
#content tab1
mighty = ttk.LabelFrame(tab1,text='Mighty Python')
mighty.grid(column=0,row=0,padx=8,pady=4)
#label
ttk.Label(mighty,text="Enter A name").grid(column=0,row=0,sticky='W')
ttk.Label(mighty,text="Choose a number").grid(column=1,row=0)
#def
def click_me():
    action.configure(text="Hello "+ name.get() +" " +number.get())
#button
action = ttk.Button(mighty,text="click me !!!", command=click_me)
action.grid(column=2,row=1)
#VARIABLE
name = tk.StringVar()
name_ent = ttk.Entry(mighty,width=12,textvariable=name)
name_ent.grid(column=0,row=1,sticky='W')
number = tk.StringVar()
number_chose = ttk.Combobox(mighty,width=12,textvariable=number)
number_chose.grid(column=1,row=1)
number_chose['values']= (1,2,4,6,42)
number_chose.current(0)
#Scroll
scW = 30
scH = 3
scr = scrolledtext.ScrolledText(mighty,width=scW,height=scH,wrap=tk.WORD)
scr.grid(column=0,row=3,columnspan=3,sticky='WE')
#tab2
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text="tab_2")
tabControl.pack(expand=2,fill="both")
Snake = ttk.LabelFrame(tab2,text='The Snake')
Snake.grid(column=0,row=0,padx=8,pady=4)
#variable disable - check
varDis = tk.IntVar()
check1 = tk.Checkbutton(Snake,text="Disable",variable=varDis,state='disable')
check1.grid(column=0,row=2,sticky=tk.W)
check1.select()
varUn = tk.IntVar()
check2 = tk.Checkbutton(Snake,text="Unchecked",variable=varUn)
check2.deselect()
check2.grid(column=1,row=2)
varEn = tk.IntVar()
check3 = tk.Checkbutton(Snake,text="Enable",variable=varEn)
check3.select()
check3.grid(column=2,row=2)
#color
#variable COLOR
radVar = tk.IntVar()
#Def color

rad1 = tk.Radiobutton(Snake,variable=radVar,value=1,text='Red')
rad2 = tk.Radiobutton(Snake,variable=radVar,value=2,text='Blue')
rad3 = tk.Radiobutton(Snake,variable=radVar,value=3,text='Gold')
#hello
rad1.grid(column=0,row=5,sticky=tk.W,columnspan=3)
rad2.grid(column=1,row=5,sticky=tk.W,columnspan=3)
rad3.grid(column=2,row=5,sticky=tk.W,columnspan=3)
#Frame
#labelframe
buttons_frame = ttk.LabelFrame(Snake,text='Labels in a frame')
buttons_frame.grid(column=0,row=7)
#ttk frame
ttk.Label(buttons_frame,text="Label1").grid(column=0,row=0,sticky=tk.W)
ttk.Label(buttons_frame,text="Label2").grid(column=1,row=0,sticky=tk.W)
ttk.Label(buttons_frame,text="Label3").grid(column=2,row=0,sticky=tk.W)
for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8 ,pady=4)
name_ent.focus()
win.mainloop()
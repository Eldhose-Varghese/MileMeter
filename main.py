import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile = entry_int.get()
    km = round(mile * 1.61,2)
    output_string.set(km)


root = ttk.Window(themename="journal")
root.eval('tk::PlaceWindow . center')
root.title("MileMeter")
root.geometry('600x350')

title_label = ttk.Label(root,text="Welcome to MileMeter",font='Calibri 20 bold')
title_label.pack()
tagline_label = ttk.Label(root,text="Your ultimate solution to distance conversion ...",font='rockwell 10')
tagline_label.pack()

entry_frame = ttk.Frame(root)
entry_int = tk.IntVar()
entry = ttk.Entry(entry_frame,textvariable=entry_int)
entry.pack(side='left',padx=10)
convert_button = ttk.Button(entry_frame,text="Convert",command=convert)
convert_button.pack(side='left',padx=10)
entry_frame.pack(pady=10)

output_string = tk.StringVar()
output_label = ttk.Label(root,text=" ",textvariable=output_string)
output_label.pack(pady=10)



root.mainloop()
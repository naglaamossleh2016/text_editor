import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile, asksaveasfile


def open_file():
    filepath=askopenfile(filetypes=[("Text Files","*.txt"),("All Flies","*.")])
    
    if not filepath:
        return
    txt_edit.delete(1.0,tk.END)
    with open(filepath.name,"r") as input_file:
        text=input_file.read()
        txt_edit.insert(tk.END,text)
    window.title(f"Text editor {filepath}")

def save_file():
    filepath=asksaveasfile(
        defaultextension="txt",
        filetypes=[("Text Files","*.txt"),("All Flies","*.")])
    with open(filepath.name,"w") as output_file:
        text=txt_edit.get(1.0,tk.END)
        output_file.write(text)
    window.title(f"Text editor {filepath}")

window=tk.Tk()
window.minsize(width=600,height=800)
txt_edit=tk.Text(window)
frame_buttons=tk.Frame(window,relief=tk.RAISED)
btn_open=tk.Button(frame_buttons,text="Open File",command=open_file)
btn_save=tk.Button(frame_buttons,text="Save File",command=save_file)

btn_open.grid(column=0,row=0,sticky="ew",padx=5,pady=5)
btn_save.grid(column=0,row=1,sticky="ew",padx=5)
frame_buttons.grid(column=0,row=0,sticky="ns")
txt_edit.grid(column=1,row=0,sticky="nsew")
window.mainloop()

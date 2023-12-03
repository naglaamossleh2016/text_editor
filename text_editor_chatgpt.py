import tkinter as tk
from tkinter import filedialog

def open_file():
    """
    Open a text file and display its content in the text editor.
    """
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    if not file_path:
        return  # User canceled the file dialog

    txt_edit.delete(1.0, tk.END)
    
    try:
        with open(file_path, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
            window.title(f"Text Editor - {file_path}")
    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred while opening the file:\n{str(e)}")

def save_file():
    """
    Save the content of the text editor to a text file.
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not file_path:
        return  # User canceled the file dialog

    try:
        with open(file_path, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
            window.title(f"Text Editor - {file_path}")
    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred while saving the file:\n{str(e)}")

# Create the main window
window = tk.Tk()
window.title("Text Editor")
window.minsize(width=600, height=800)

# Create text editor and buttons
txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED)
btn_open = tk.Button(frame_buttons, text="Open File", command=open_file)
btn_save = tk.Button(frame_buttons, text="Save File", command=save_file)

# Grid layout
btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
btn_save.grid(column=0, row=1, sticky="ew", padx=5)
frame_buttons.grid(column=0, row=0, sticky="ns")
txt_edit.grid(column=1, row=0, sticky="nsew")

# Allow text editor to expand with the window
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)

# Start the GUI event loop
window.mainloop()

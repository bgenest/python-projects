##tkinter.py


import tkinter as tk

label = tk.Label(
    text="Hello, Tkinter",
    foreground="#FFFFFF",  # Set the text color to white
    background="#000000",  # Set the background color to black
    width = 10,
    height = 10
)

button = tk.Button(
    text="Click me!",
    foreground = "black",
    background = "blue",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

entry = tk.Entry(
    fg="yellow", 
    bg="blue", 
    width=50)
label.pack()

entry.pack()
##name = entry.get()
##entry.delete(0,4)

window = tk.Tk()
text_box = tk.Text()
text_box.pack()

##text_box.get("1.0", "1.5")

button.pack()



label.mainloop()




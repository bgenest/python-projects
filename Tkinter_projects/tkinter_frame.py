##tkimter_frame.py
## https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

"""import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()
"""

<<<<<<< HEAD:tkinter_frame.py
=======
##Boarder effects

>>>>>>> aff370b347e9294032bdca80ff0bd9b2e78e175f:Tkinter_projects/tkinter_frame.py
import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()
"""

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="white")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, width=100, height=100, bg="blue")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, width=100, height=100, bg="red")
frame3.pack(fill=tk.X)

window.mainloop()
<<<<<<< HEAD:tkinter_frame.py

=======
>>>>>>> aff370b347e9294032bdca80ff0bd9b2e78e175f:Tkinter_projects/tkinter_frame.py
"""
import sqlite3
import tkinter as tk
from tkinter import *
import time
import numpy as np

import os
from PIL import Image  
from PIL import Image, ImageTk

root = tk.Tk()
# Increase the window size
root.geometry("1300x700")
# Set the title
root.title("Cyberattack Detection Using ML")

# Get screen width and height
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# Set the window size to cover the entire screen
root.geometry("%dx%d+0+0" % (w, h))



#-------function------------------------

def reg():

##### tkinter window ######
    
    print("reg")

    from subprocess import call

    call(["python", "registration.py"])   



def login():

##### tkinter window ######
    
    print("log")

    from subprocess import call

    call(["python", "login.py"])   

    


# Configure background color
root.configure(background="seashell2")

# Load background image
image2 = Image.open("dd.png")
# Resize the image to fit the screen
image2 = image2.resize((w, h))
background_image = ImageTk.PhotoImage(image2)

# Create a label for the background image
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
# Place the label at (0, 0) to cover the entire window
background_label.place(x=0, y=0)

# Create a label for the title
lbl = tk.Label(
    root,
    text="Cyberattack Detection Using ML",
    font=("times", 40, "bold"),
    height=1,
    width=50,
    bg="black" ,
    fg="white",
)
# Place the label at the top center of the window
lbl.place(relx=0.5, rely=0.05, anchor=CENTER)

# Create a frame for login and registration buttons
framed = tk.LabelFrame(
    root,
    text="--WELCOME--",
    width=500,
    height=210,
    bd=5,
    font=("times", 14, "bold"),
    bg="white",
)
# Place the frame in the center of the window
framed.place(relx=0.5, rely=0.50, anchor=CENTER)

# Create login button
button1 = tk.Button(
    framed,
    text="Login Now",
    width=15,
    height=2,
    bg="dark blue",
    fg="white",
    command=login,
    font="bold",
)
# Place the button at the left side of the frame
button1.place(x=30, y=65)

# Create registration button
button2 = tk.Button(
    framed,
    text="Register",
    width=15,
    height=2,
    bg="dark blue",
    fg="white",
    command=reg,
    font="bold",
)
# Place the button at the right side of the frame
button2.place(x=250, y=65)


root.mainloop()

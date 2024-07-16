"""
GUI
"""

import tkinter as tk
import cmms_druk
from PIL import Image, ImageTk
from qr_code import qr_code
import os


def print_value(key=None):

    kod = qr_code("QR.png")
    kod.clear_png()

    text = cmms_input.get()

    if text != "":
        cmms_druk.drukuj(text)

        #generowanie kodu qr
        kod = qr_code(text)
        kod.generate_qr()
        print(kod)

        display_qr()

    elif text == "":
        print("wprowadź numer CMMS")

    return text

def qr_preview(image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    return photo


def display_qr():
    if os.path.isfile("QR.png"):
        img = Image.open("QR.png")
        img = img.resize((100, 100), Image.Resampling.LANCZOS)
        qr_photo = ImageTk.PhotoImage(img)

        image_label.config(image=qr_photo)
        image_label.image = qr_photo

window = tk.Tk()
window.geometry("200x200")

# CMMS
frame_cmms = tk.Frame(master=window)
frame_cmms.grid(row=1, column=1)
cmms = tk.Label(master=frame_cmms,
                text="Wprowadź numer CMMS: ",
                width=25,
                height=1)
cmms.pack()

cmms_input = tk.Entry(master=frame_cmms)
cmms_input.pack()

#preview button
preview_button = tk.Button(master=frame_cmms,
                           text="Drukuj",
                           command=print_value)
preview_button.pack()

cmms_input.bind('<Return>', print_value)
cmms_input_value = cmms_input.get()


# Tworzenie ramki dla labela
label_frame = tk.Frame(master=window)
label_frame.grid(row=2, column=1)

# Tworzenie etykiety do wyświetlania obrazu
label_label = tk.Label(master=label_frame)
label_label.grid(row=2, column=1)

# Tworzenie ramki dla obrazu
image_frame = tk.Frame(master=window)
image_frame.grid(row=3, column=1)

# Tworzenie etykiety do wyświetlania obrazu
image_label = tk.Label(master=image_frame)
image_label.grid(row=3, column=1)



window.mainloop()

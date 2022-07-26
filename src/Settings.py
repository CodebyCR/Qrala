# from pprint import pprint
from tkinter import *
from tkinter.constants import CENTER, NONE
from tkinter.ttk import Label, Combobox, Button

import src.ConstantStyle as cs


# Colors
BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY

# Fonts
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2

def set_fill_color(color):
    cs.FILL_COLOR = color

def set_background_color(color):
    cs.BACK_COLOR = color



def switch_language(lang):
    print(lang)
    pass

def get_settings():
    settings =Tk()

    # settings.configure(background=BG_COLOR)
    settings.title('Settings')
    settings.geometry("600x330")

    # Language
    langLabel = Label(settings, text="Language:")
    langLabel.configure(background=BACKGROUND, font=FONT_1, padding=10)
    langLabel.grid(column=0, row=2)

    chooseLang = Combobox(settings, state="readonly",
                              values=["Deutsch",
                                      "English"]
                              )

    chooseLang.configure(background=BACKGROUND, font=FONT_1,
                         takefocus=NONE, justify=CENTER)
    chooseLang.grid(column=1, row=2)
    chooseLang.current(1)

    # Error Level
    errorLabel = Label(settings, text="QR-Code Error Level:")
    errorLabel.configure(background=BACKGROUND, font=FONT_1, padding=10)
    errorLabel.grid(column=0, row=3)

    chooseError = Combobox(settings, state="readonly",
                                values=["L",
                                        "M",
                                        "Q",
                                        "H"]
                                )
    chooseError.configure(background=BACKGROUND, font=FONT_1,
                            takefocus=NONE, justify=CENTER)
    chooseError.grid(column=1, row=3)
    chooseError.current(1)

    # QR Code Color Scheme
    color_label = Label(settings, text="QR-Code Color Scheme:")
    color_label.configure(background=BACKGROUND, font=FONT_1, padding=10)
    color_label.grid(column=1, row=4, columnspan=2)


    inColorLabel = Label(settings, text="Fill Color:")
    inColorLabel.configure(background=BACKGROUND, font=FONT_1, padding=10)
    inColorLabel.grid(column=0, row=5)

    chooseInColor = Combobox(settings, state="readonly",
                                values=["Black",
                                        "White"]
                                )
    chooseInColor.configure(background=BACKGROUND, font=FONT_1,
                            takefocus=NONE, justify=CENTER)
    chooseInColor.grid(column=1, row=5)
    chooseInColor.current(1)

    outColorLabel = Label(settings, text="Background Color:")
    outColorLabel.configure(background=BACKGROUND, font=FONT_1, padding=10)
    outColorLabel.grid(column=0, row=6)

    chooseOutColor = Combobox(settings, state="readonly",
                                values=["Black",
                                        "White"]
                                )
    chooseOutColor.configure(background=BACKGROUND, font=FONT_1,
                            takefocus=NONE, justify=CENTER)
    chooseOutColor.grid(column=1, row=6)
    chooseOutColor.current(1)

    # QR Code Size
    sizeLabel = Label(settings, text="QR-Code Size:")
    sizeLabel.configure(background=BACKGROUND, font=FONT_1, padding=10)
    sizeLabel.grid(column=0, row=7)

    chooseSize = Combobox(settings, state="readonly",
                                values=["Small",
                                        "Medium",
                                        "Large"]
                                )
    chooseSize.configure(background=BACKGROUND, font=FONT_1,
                            takefocus=NONE, justify=CENTER)
    chooseSize.grid(column=1, row=7)
    chooseSize.current(1)


    apply_button = Button(settings, text="Apply", command=settings.destroy)
    apply_button.grid(column=2, row=8, columnspan=2, padx=10, pady=10)
    # pprint(dict(chooseLang))
    settings.mainloop()
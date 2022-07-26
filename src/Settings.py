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

def switch_language(lang):
    print(lang)
    pass

def get_settings():
    settings =Tk()

    # settings.configure(background=BG_COLOR)
    settings.title('Settings')
    settings.geometry("600x330")

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

    apply_button = Button(settings, text="Apply", command=settings.destroy)
    apply_button.grid(column=1, row=3, columnspan=2, padx=10, pady=100)
    # pprint(dict(chooseLang))
    settings.mainloop()
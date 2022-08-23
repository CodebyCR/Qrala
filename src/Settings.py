# from pprint import pprint
import xml.etree.ElementTree as ET
import xml
from tkinter import *
from tkinter.constants import CENTER, NONE
from tkinter.ttk import Label, Combobox, Button

from qrcode import constants

import src.ConstantStyle as cs
# Colors
from src.SystemDependency import get_settings_path
from src.XML_Parser import XML_Parser

xml_parser = XML_Parser('Settings.xml')

BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY

# Fonts
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2

correctness = {
    "M": constants.ERROR_CORRECT_M,
    "L": constants.ERROR_CORRECT_L,
    "H": constants.ERROR_CORRECT_H,
    "Q": constants.ERROR_CORRECT_Q,
}


def get_correctness() -> int:
    current_correction = xml_parser.get_tag_text("error_correction")
    return correctness[current_correction]


def set_fill_color(color: any) -> None:
    cs.FILL_COLOR = color


def set_background_color(color: any) -> None:
    cs.BACK_COLOR = color


def switch_language(lang: any) -> None:
    print(lang)
    pass


def save_and_close_settings() -> None:
    # Set Language
    chosen_language = chooseLang.get()
    if chosen_language == "English":
        xml_parser.set_tag_text("language", "en")
    elif chosen_language == "Deutsch":
        xml_parser.set_tag_text("language", "de")

    # Set Error Correction
    new_error_level = choose_error_level.get()
    xml_parser.set_tag_text("error_correction", new_error_level)

    settings_win.destroy()


def get_settings() -> None:
    global settings_win
    settings_win = Tk()

    # settings_win.configure(background=BG_COLOR)
    settings_win.title('Settings')
    settings_win.geometry("600x330")
    settings_win.resizable(False, False)
    settings_win.configure(background=BACKGROUND)

    # Language
    langLabel = Label(settings_win, text="Language:")
    langLabel.configure(background=BACKGROUND, font=FONT_1, padding=10)
    langLabel.grid(column=0, row=2, sticky="w")

    global chooseLang
    chooseLang = Combobox(settings_win, state="readonly",
                          values=["Deutsch",
                                  "English"]
                          )

    chooseLang.configure(background=BACKGROUND, font=FONT_1,
                         takefocus=NONE, justify=CENTER)
    chooseLang.grid(column=1, row=2)
    lang = xml_parser.get_tag_text("language")
    if lang == "de":
        chooseLang.current(0)
    elif lang == "en":
        chooseLang.current(1)

    # Error Correction
    error_label = Label(settings_win, text="QR-Code Error Correction:")
    error_label.configure(background=BACKGROUND, font=FONT_1, padding=10)
    error_label.grid(column=0, row=3, sticky="w")

    global choose_error_level
    choose_error_level = Combobox(settings_win, state="readonly",
                                  values=["M",
                                          "L",
                                          "H",
                                          "Q"]
                                  )
    choose_error_level.configure(background=BACKGROUND,
                                 font=FONT_1,
                                 takefocus=NONE,
                                 justify=CENTER)
    choose_error_level.grid(column=1, row=3)

    current_correction = get_correctness()
    choose_error_level.current(current_correction)

    # QR Code Color Scheme
    color_label = Label(settings_win, text="QR-Code Color Scheme:")
    color_label.configure(background=BACKGROUND, font=FONT_1, padding=10)
    color_label.grid(column=1, row=4, columnspan=2)

    inColorLabel = Label(settings_win, text="Fill Color:")
    inColorLabel.configure(background=BACKGROUND, font=FONT_1, padding=10)
    inColorLabel.grid(column=0, row=5, sticky="w")

    chooseInColor = Combobox(settings_win, state="readonly",
                             values=["Black",
                                     "White"]
                             )
    chooseInColor.configure(background=BACKGROUND, font=FONT_1,
                            takefocus=NONE, justify=CENTER)
    chooseInColor.grid(column=1, row=5)
    chooseInColor.current(0)

    outColorLabel = Label(settings_win, text="Background Color:")
    outColorLabel.configure(background=BACKGROUND, font=FONT_1, padding=10)
    outColorLabel.grid(column=0, row=6, sticky="w")

    chooseOutColor = Combobox(settings_win, state="readonly",
                              values=["Black",
                                      "White"]
                              )
    chooseOutColor.configure(background=BACKGROUND, font=FONT_1,
                             takefocus=NONE, justify=CENTER)
    chooseOutColor.grid(column=1, row=6)
    chooseOutColor.current(1)

    # QR Code Size
    # sizeLabel = Label(settings_win, text="QR-Code Size:")
    # sizeLabel.configure(background=BACKGROUND, font=FONT_1, padding=10)
    # sizeLabel.grid(column=0, row=7, sticky="w")
    #
    # chooseSize = Combobox(settings_win, state="readonly",
    #                       values=["Small",
    #                               "Medium",
    #                               "Large"]
    #                       )
    # chooseSize.configure(background=BACKGROUND, font=FONT_1,
    #                      takefocus=NONE, justify=CENTER)
    # chooseSize.grid(column=1, row=7)
    # chooseSize.current(1)

    apply_button = Button(settings_win, text="apply", command=save_and_close_settings)
    apply_button.place(x=500, y=294)

    settings_win.mainloop()

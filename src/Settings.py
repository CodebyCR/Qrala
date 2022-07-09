from pprint import pprint
from tkinter.constants import CENTER, NONE
from tkinter.ttk import Frame, Label, Combobox
import src.ConstantStyle as cs


# Colors
BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY

# Fonts
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2

def get_frame(note, new_bg_img):
    settings = Frame(note)
    # settings.configure(background=BG_COLOR)

    # Background Img
    img_label = Label(settings, image=new_bg_img, background=BACKGROUND)
    img_label.place(x=680, y=306)

    langLabel = Label(settings, text="Language:")
    langLabel.configure(background=BACKGROUND, font=FONT_1, padding=10)
    langLabel.grid(column=0, row=2)

    chooseLang = Combobox(settings,
                              values=["Deutsch",
                                      "English"])

    chooseLang.configure(background=BACKGROUND, font=FONT_1,
                         takefocus=NONE, justify=CENTER)
    chooseLang.grid(column=1, row=2)
    chooseLang.current(1)

    pprint(dict(chooseLang))

    return settings

from tkinter import Tk
from tkinter.ttk import Label, Button

import src.ConstantStyle as Cs
import webbrowser

# https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter

# Colors
BACKGROUND = Cs.BACKGROUND
SECONDARY = Cs.SECONDARY

# Fonts
FONT_1 = Cs.FONT_1
FONT_2 = Cs.FONT_2


def callback(url):
    webbrowser.open_new(url)


def get_about() -> None:
    about_win = Tk()

    about_win.title('About')
    about_win.geometry("600x330")
    about_win.resizable(False, False)
    about_win.configure(background=BACKGROUND)

    # about label
    about_text_p1 = "Qrala is an all-in-one open-source QR-Code tool."
    about_text_p2 = "You can find the source code here."
    about_text_p3 = "If you have any questions or issues please tell them here."
    about_text_p4 = """
    Qrala Version: 0.9.9,\n
    License: GNU Affero General Public License v3.0,\n
    Written by Christoph Rohde
    """

    about_label_1 = Label(about_win, text=about_text_p1)
    about_label_1.grid(column=1, row=0, sticky="w", padx=10, pady=10)
    about_label_1.bind("<Button-1>", lambda e: callback("https://github.com/CodebyCR"))

    about_label_2 = Label(about_win, text=about_text_p2)
    about_label_2.grid(column=1, row=1, sticky="w", padx=10, pady=10)
    about_label_2.bind("<Button-1>", lambda e: callback("https://github.com/CodebyCR/Qrala"))

    about_label_3 = Label(about_win, text=about_text_p3)
    about_label_3.grid(column=1, row=2, sticky="w", padx=10, pady=10)
    about_label_3.bind("<Button-1>", lambda e: callback("https://github.com/CodebyCR/Qrala/issues"))

    about_label_4 = Label(about_win, text=about_text_p4)
    about_label_4.place(x=0, y=210)
    about_label_4.bind("<Button-1>", lambda e: callback("https://github.com/CodebyCR"))

    apply_button = Button(about_win, text="close", command=about_win.destroy)
    apply_button.place(x=500, y=294)

    about_win.mainloop()

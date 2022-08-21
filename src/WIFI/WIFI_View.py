from tkinter.constants import DISABLED, END
from tkinter.ttk import Entry, Frame, Label

import src.ConstantStyle as cs
import src.Translations as translation
from src.WIFI import WIFI_Controller as Model

# Colors
BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY

# Fonts
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2

# Const Placeholder
SSID_PLACEHOLDER = 'SSID (often WIFI-Name)'
PASSWORD_PLACEHOLDER = 'Password'


def get_wifi_text() -> str:
    wifi_text = ""
    ssid = cs.get_entry_text(wifi_name, SSID_PLACEHOLDER)
    password = cs.get_entry_text(wifi_password, PASSWORD_PLACEHOLDER)

    if ssid is not None and password is not None:
        wifi_text = Model.create_wifi_text(ssid, password)

    return wifi_text


def generate_wifi_qr() -> str:
    wifi_tuple = Model.try_current_wifi()

    wifi_name_text = wifi_tuple[0]
    wifi_name.delete(0, END)
    wifi_name.insert(0, wifi_name_text)

    wifi_password_text = wifi_tuple[1]
    print("tuple password:", wifi_password_text)
    wifi_password.delete(0, END)
    wifi_password.insert(0, wifi_password_text)

    opt_wifi_text = wifi_tuple[2]
    return opt_wifi_text


def get_frame(note: any) -> Frame:
    wifi_frame = Frame(note)
    # wifi_frame.configure(background=BG_COLOR)



    # Label
    label_In = Label(wifi_frame, background=BACKGROUND, font=FONT_2, foreground="black",
                     text='Enter your WIFI information')
    label_In.grid(column=0,
                  row=0,
                  padx=20,
                  pady=8)

    global wifi_name
    wifi_name = Entry(wifi_frame, width=30)
    wifi_name.grid(column=0,
                   row=1,
                   padx=20,
                   pady=8)
    wifi_name.insert(0, SSID_PLACEHOLDER)
    wifi_name.configure(state=DISABLED)
    wifi_name.bind("<Button-1>", lambda event: cs.removePlaceholder(event, wifi_name))

    global wifi_password
    wifi_password = Entry(wifi_frame, width=30)
    wifi_password.grid(column=0,
                       row=2,
                       padx=20,
                       pady=8)
    wifi_password.insert(0, PASSWORD_PLACEHOLDER)
    wifi_password.configure(state=DISABLED)
    wifi_password.bind("<Button-1>", lambda event: cs.removePlaceholder(event, wifi_password))

    return wifi_frame

from src.WIFI import WIFI_Controller as Model
from tkinter.constants import DISABLED
from tkinter.ttk import Entry, Frame, Label, Button
import src.ConstantStyle as cs


# Colors
BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY

# Fonts
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2

def getFrame(note, new_bg_img):
    wifi_QR = Frame(note)
    # wifi_QR.configure(background=BG_COLOR)

    # GUI
    label_In = Label(wifi_QR, background=BACKGROUND, font=FONT_2, foreground="black",
                        text="QR_Inhalt")
    #get_From_XML('QR_Inhalt')
    label_In.grid(column=0,
                  row=2,
                  padx=20,
                  pady=8)



    # Label
    label_In = Label(wifi_QR, background=BACKGROUND, font=FONT_2, foreground="black",
                        text='Enter your WIFI information')
    label_In.grid(column=0,
                  row=0,
                  padx=20,
                  pady=8)

    wifi_name = Entry(wifi_QR, width=30)
    wifi_name.grid(column=0,
                        row=1,
                        padx=20,
                        pady=8)
    wifi_name.insert(0, 'SSID (often WIFI-Name)')
    wifi_name.configure(state=DISABLED)
    wifi_name.bind("<Button-1>", lambda event: cs.removePlaceholder(event, wifi_name))

    wifi_password = Entry(wifi_QR, width=30)
    wifi_password.grid(column=0,
                        row=2,
                        padx=20,
                        pady=8)
    wifi_password.insert(0, 'Password')
    wifi_password.configure(state=DISABLED)
    wifi_password.bind("<Button-1>", lambda event: cs.removePlaceholder(event, wifi_password))

    # Button to generate QR-Codes
    get_QR_button = Button(wifi_QR,
                           text='Generate_Code',
                           # highlightbackground=BG_COLOR,
                           # padx=4,
                           #  pady=2,
                           # font=FONT_1,
                           # command=get_QR
                           )
    get_QR_button.configure()
    #get_From_XML()

    get_QR_button.grid(column=0,
                       row=4,
                       padx=10,
                       pady=18)
    cs.changeOnHover(get_QR_button, "white", SECONDARY)

    # Button to generate QR-Codes
    try_current_wifi = Button(wifi_QR,
                                 text="Try current WIFI",
                                 # highlightbackground=BACKGROUND,
                                 # padx=4,
                                 # pady=2,
                                 # font=FONT_1,
                                 command=Model.try_current_wifi)

    try_current_wifi.grid(column=1,
                        row=4,
                        padx=10,
                        pady=18)

    cs.changeOnHover(try_current_wifi, "white", SECONDARY)

    # Background Img
    img_label = Label(wifi_QR, image=new_bg_img, background=BACKGROUND)
    img_label.place(x=680, y=306)

    return wifi_QR
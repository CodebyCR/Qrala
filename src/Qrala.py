#################################################################################
#   Copyright of Christoph Rohde, 2022                                          #
#                                                                               #
#   Qrala Version: 0.9.4 ,            # #  # # # # # #   # #                    #
#   sine 2021                       #    #             #    #                   #
#                                   #   #   #      #   #   #                    #
#                                     #                  #                      #
#                                       #     ##       #                        #
#                                        #           #                          #
#                                          # # # # #                            #
#                                                                               #
#   https://github.com/CodebyCR                                                 #
#   Licence: GNU Affero General Public License v3.0                             #
#################################################################################




# TKinter

from tkinter import *

# remove following trey lines, because they are not used anymore
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import Entry
# XML
import xml.dom.minidom

#
import cv2

# max. 4296 Zeichen
import qrcode
from PIL import Image, ImageTk

from pprint import pprint


import SystemDependency as depend

BG_COLOR = "#696969"
secColor = "#b5b5b5"
FONT_1 = ("Helvetica", 14)  # ("Century Gothic", 14, BOLD)
FONT_2 = ("Helvetica", 16)


OPERATING_SYSTEM = depend.getOS()

rootPath = depend.getRootPath()
print(rootPath)

domtree = xml.dom.minidom.parse(
    rootPath + '/src/Qrala_Config.xml')

qrala = domtree.documentElement

# Icons
# Qrala.png
bg_img = Image.open(
    rootPath + '/Images/Qrala_1024x1024px.png')
contact_16px = Image.open(
    rootPath + "/Images/Tab_icons/contact.png").resize((16, 16))
wifi_16px = Image.open(
    rootPath + "/Images/Tab_icons/wifi.png").resize((16, 16))
setting_16px = Image.open(
    rootPath + "/Images/Tab_icons/setting.png").resize((16, 16))


def onOpen():
    # if else    #wenn kein qr code
    file_path = filedialog.askopenfilename()
    splitIn = cv2.QRCodeDetector()
    data, _, _ = splitIn.detectAndDecode(
        cv2.imread(file_path))  # path einbauen
    print("QRCode:\t", data)  # data is the inputtext
    inputText.delete(1.0, END)
    inputText.insert(1.0, data)


def onSave():
    # qr=get_QR()
    print(filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                       filetypes=(("Python files", "*.png;*.jpg;*.svg"), ("All files", "*.*"))))


# Clear Function
def clearText():
    inputText.delete(1.0, END)


def get_From_XML(str):
    # read XML
    tagname = qrala.getElementsByTagName(str)
    return tagname[0].firstChild.data


def changeOnHover(button, colorOnHover, colorOnLeave):

    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def removePlaceholder(event, current_entry):
    current_entry.configure(state=NORMAL)
    current_entry.delete(0, END)

# Grab the text from the textbox into the code
def get_QR():        # WIFI:S:password;T:WPA;P:ssid;; #formart
    qr = qrcode.make(inputText.get(1.0, 3.0))  # , error='H'
    qr.show()

    # qr = qr.png
    # qr = Image.open(qr)
    # qr_code = qr.resize((200, 200))
    # qr_label = Label(win, image=qr_code, bg=BG_COLOR)
    # qr_label.place(x=380, y=40, relwidth=1, relheight=1)
    return qr




# returns list for mac


def get_WIFI_QR(note, new_bg_img):
    wifi_QR = Frame(note)
    wifi_QR.configure(background=BG_COLOR)

    # GUI
    label_In = tk.Label(wifi_QR, bg=BG_COLOR, font=FONT_2, fg="black",
                        text=get_From_XML('QR_Inhalt'))
    label_In.grid(column=0,
                  row=2,
                  padx=20,
                  pady=8)

    # Check for OS
    if OPERATING_SYSTEM == "darwin":
        # MAC OS
        print("\nOS:\t", "Mac OS\n")

    elif OPERATING_SYSTEM == "win64":
        # Windows 64-bit
        print("\nOS:\t", "Windows\n")

    # Label
    label_In = tk.Label(wifi_QR, bg=BG_COLOR, font=FONT_2, fg="black",
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
    wifi_name.bind("<Button-1>", lambda event: removePlaceholder(event, wifi_name))

    wifi_password = Entry(wifi_QR, width=30)
    wifi_password.grid(column=0,
                        row=2,
                        padx=20,
                        pady=8)
    wifi_password.insert(0, 'Password')
    wifi_password.configure(state=DISABLED)
    wifi_password.bind("<Button-1>", lambda event: removePlaceholder(event, wifi_password))

    # Button zum QR-Code Generieren
    get_QR_button = tk.Button(wifi_QR, text=get_From_XML('Generate_Code'), highlightbackground=BG_COLOR, padx=4,
                              pady=2, font=FONT_1, command=get_QR)
    get_QR_button.grid(column=0,
                       row=4,
                       padx=10,
                       pady=18)
    changeOnHover(get_QR_button, "white", secColor)

    # Background Img
    img_label = Label(wifi_QR, image=new_bg_img, bg=BG_COLOR)
    img_label.place(x=680, y=306)

    return wifi_QR


def getCustomQR(note, new_bg_img):
    customQR = Frame(note)
    customQR.configure(background=BG_COLOR)

    # Label
    label_In = tk.Label(customQR, bg=BG_COLOR, font=FONT_2, fg="black",
                        text=get_From_XML('QR_Inhalt'))
    label_In.grid(column=0,
                  row=2,
                  padx=20,
                  pady=8)

    # Textbox
    global inputText
    inputText = Text(customQR, height=20, width=60, bg=secColor, font=FONT_2)
    inputText.grid(column=0,
                   row=3,
                   padx=20, sticky="nesw")

    # Button zum QR-Code Generieren
    getQrButton = tk.Button(customQR, text=get_From_XML('Generate_Code'), highlightbackground=BG_COLOR, padx=4,
                            pady=2, font=FONT_1, command=get_QR)
    changeOnHover(getQrButton, "white", secColor)
    getQrButton.grid(column=0,
                     row=4,
                     padx=10,
                     pady=18)

    # Background Img
    img_label = Label(customQR, image=new_bg_img, bg=BG_COLOR)
    img_label.place(x=680, y=306)

    return customQR



def getContactQR(note, new_bg_img):
    contact_QR = Frame(note)
    contact_QR.configure(background=BG_COLOR)

    # Background Img
    img_label = Label(contact_QR, image=new_bg_img, bg=BG_COLOR)
    img_label.place(x=680, y=306)

    # Label
    label_In = tk.Label(contact_QR, bg=BG_COLOR, font=FONT_2, fg="black",
                        text='Enter your contact information for the VCard')
    label_In.grid(column=0,
                  row=1,
                  padx=20,
                  pady=8)

    showed_name = Entry(contact_QR, width=30)
    showed_name.grid(column=0,
                        row=2,
                        padx=20,
                        pady=8)
    showed_name.insert(0, 'Showed Name')
    showed_name.configure(state=DISABLED)
    showed_name.bind("<Button-1>", lambda event: removePlaceholder(event, showed_name))

    last_name = Entry(contact_QR, width=30)
    last_name.grid(column=0,
                        row=3,
                        padx=20,
                        pady=8)
    last_name.insert(0, 'Last Name')
    last_name.configure(state=DISABLED)
    last_name.bind("<Button-1>", lambda event: removePlaceholder(event, last_name))

    first_name = Entry(contact_QR, width=30)
    first_name.grid(column=1,
                        row=3,
                        padx=20,
                        pady=8)
    first_name.insert(0, 'First Name')
    first_name.configure(state=DISABLED)
    first_name.bind("<Button-1>", lambda event: removePlaceholder(event, first_name))

    # Tel Number Entry
    tel_number = Entry(contact_QR, width=30)
    tel_number.grid(column=0,
                        row=4,
                        padx=20,
                        pady=8)
    tel_number.insert(0, 'Tel. Number')
    tel_number.configure(state=DISABLED)
    tel_number.bind("<Button-1>", lambda event: removePlaceholder(event, tel_number))

    # Email Entry
    email = Entry(contact_QR, width=30)
    email.grid(column=1,
                        row=4,
                        padx=20,
                        pady=8)
    email.insert(0, 'Email')
    email.configure(state=DISABLED)
    email.bind("<Button-1>", lambda event: removePlaceholder(event, email))

    # organization Entry
    organization = Entry(contact_QR, width=30)
    organization.grid(column=0,
                        row=5,
                        padx=20,
                        pady=8)
    organization.insert(0, 'Organization')
    organization.configure(state=DISABLED)
    organization.bind("<Button-1>", lambda event: removePlaceholder(event, organization))

    # address Entry
    address = Entry(contact_QR, width=30)
    address.grid(column=1,
                        row=5,
                        padx=20,
                        pady=8)
    address.insert(0, 'Address')
    address.configure(state=DISABLED)
    address.bind("<Button-1>", lambda event: removePlaceholder(event, address))

    # city Entry
    city = Entry(contact_QR, width=30)
    city.grid(column=0,
                        row=6,
                        padx=20,
                        pady=8)
    city.insert(0, 'City')
    city.configure(state=DISABLED)
    city.bind("<Button-1>", lambda event: removePlaceholder(event, city))

    # country Entry
    country = Entry(contact_QR, width=30)
    country.grid(column=1,
                        row=6,
                        padx=20,
                        pady=8)
    country.insert(0, 'Country')
    country.configure(state=DISABLED)
    country.bind("<Button-1>", lambda event: removePlaceholder(event, country))

    # postalcode Entry
    postalcode = Entry(contact_QR, width=30)
    postalcode.grid(column=0,
                        row=7,
                        padx=20,
                        pady=8)
    postalcode.insert(0, 'Postalcode')
    postalcode.configure(state=DISABLED)
    postalcode.bind("<Button-1>", lambda event: removePlaceholder(event, postalcode))


    return contact_QR



def get_Settings(note, new_bg_img):
    settings = Frame(note)
    settings.configure(background=BG_COLOR)

    # Background Img
    img_label = Label(settings, image=new_bg_img, bg=BG_COLOR)
    img_label.place(x=680, y=306)

    langLabel = ttk.Label(settings, text="Language:")
    langLabel.configure(background=BG_COLOR, font=FONT_1, padding=10)
    langLabel.grid(column=0, row=2)

    chooseLang = ttk.Combobox(settings,
                              values=["Deutsch",
                                      "English"])

    chooseLang.configure(background=BG_COLOR, font=FONT_1,
                         takefocus=NONE, justify=CENTER)
    chooseLang.grid(column=1, row=2)
    chooseLang.current(1)

    pprint(dict(chooseLang))

    return settings


# Main
def main():
    win = Tk()
    win.iconbitmap(rootPath + "/Images/Qrala_Icon_2.icns")

    print(rootPath + "/Images/Qrala_Icon.icns")
    win.title("Qrala")
    win.geometry("960x562")

    # Menubar
    menubar = Menu(win)
    win.configure(background=BG_COLOR, menu=menubar)

    # File Menu
    filemenu = Menu(menubar)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New File", command=clearText)
    filemenu.add_command(label="Open", command=onOpen)
    filemenu.add_separator()
    filemenu.add_command(label="Save File", command=onSave)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=win.quit)


    new_bg_img = ImageTk.PhotoImage(bg_img.resize((200, 200)))

    contact_Icon = ImageTk.PhotoImage(contact_16px)
    wifi_Icon = ImageTk.PhotoImage(wifi_16px)
    setting_Icon = ImageTk.PhotoImage(setting_16px)

    # Notebook
    note = ttk.Notebook(win)
    note.pack(fill="both", expand=1)

    customQR = getCustomQR(note, new_bg_img)
    note.add(customQR, text="Custom")

    wifiQR = get_WIFI_QR(note, new_bg_img)
    note.add(wifiQR, text="WIFI", image=wifi_Icon, compound="left")

    contactQR = getContactQR(note, new_bg_img)
    note.add(contactQR, text="Contact", image=contact_Icon, compound="left")

    settings = get_Settings(note, new_bg_img)
    note.add(settings,  text="Settings", image=setting_Icon, compound="left")

    note.configure()

    win.mainloop()

main()

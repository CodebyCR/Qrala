#################################################################################
#   Copyright of Christoph Rohde, 2022                                          #
#                                                                               #
#   Qrala Version: 0.9 ,              # #  # # # # # #   # #                    #
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




#TKinter
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter
from tkinter.font import BOLD

#XML
import xml.dom.minidom

#plist
import plistlib

import pyqrcode  # max. 4296 Zeichen
from PIL import Image, ImageTk

import cv2
import subprocess

from pprint import pprint
from sys import platform as _platform

bgColor = "#696969"
secColor = "#b5b5b5"
font1 = ("Helvetica", 14)  # ("Century Gothic", 14, BOLD)
font2 = ("Helvetica", 16)

domtree = xml.dom.minidom.parse('/Users/christoph_rohde/Documents/02) Development/Python/Qrala/src/Qrala_Config.xml')
qrala = domtree.documentElement


def get_From_XML(str):
    # read XML
    tagname = qrala.getElementsByTagName(str)
    return tagname[0].firstChild.data


def changeOnHover(button, colorOnHover, colorOnLeave):

    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


def onOpen():
    # if else    #wenn kein qr code
    file_path = filedialog.askopenfilename()
    splitIn = cv2.QRCodeDetector()
    data, _, _ = splitIn.detectAndDecode(
        cv2.imread(file_path))  # path einbauen
    print("QRCode:\t", data)  # data is the inputtext
    inputtxt.delete(1.0, END)
    inputtxt.insert(1.0, data)


def onSave():
    # qr=get_QR()
    print(filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                       filetypes=(("Python files", "*.png;*.jpg;*.svg"), ("All files", "*.*"))))


# Create Clear Function
def clear_Txt():
    inputtxt.delete(1.0, END)


# Grab the text from the textbox into the code
def get_QR():        # WIFI:S:password;T:WPA;P:ssid;; #formart
    qr = pyqrcode.create(inputtxt.get(1.0, 3.0), error='H')
    qr.show()

    # qr = qr.png
    # qr = Image.open(qr)
    # qr_code = qr.resize((200, 200))
    # qr_label = Label(win, image=qr_code, bg=bgColor)
    # qr_label.place(x=380, y=40, relwidth=1, relheight=1)
    return qr


def ausgabe():
    print(lbox.curselection())
    aktuell_ausgewaehlt = lbox.curselection()

# returns list for mac


def get_networks():
    scan_cmd = subprocess.Popen(
        ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport', '-s'],    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    scan_out, scan_err = scan_cmd.communicate()
    scan_out_data = []
    scan_out_lines = str(scan_out).split("\\n")[1:-1]
    for each_line in scan_out_lines:
        split_line = [e for e in each_line.split(" ") if e != ""]
        scan_out_data.append(split_line)
    return scan_out_data


def get_wifi_info():
    process = subprocess.Popen(
        ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()

    wifi_info = {}
    for line in out.decode("utf-8").split("\n"):
        if ": " in line:
            key, val = line.split(": ")
            key = key.replace(" ", "")
            val = val.strip()

            wifi_info[key] = val

    return wifi_info

# Frames

def get_WIFI_QR(note, new_bg_img):
    wifi_QR = Frame(note)
    wifi_QR.configure(background=bgColor)

    # GUI
    label_In = tk.Label(wifi_QR, bg=bgColor, font=font2, fg="black",
                        text=get_From_XML('QR_Inhalt'))
    label_In.grid(column=0,
                  row=2,
                  padx=20,
                  pady=8)

    # Check for OS
    if _platform == "darwin":
        # MAC OS
        print("\nOS:\t", "Mac OS\n")
        # proc = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport', '-s', '-x'], stdout=subprocess.PIPE)
        # #ssid_data = plistlib.load(proc.stdout)
        # pprint(plistlib.loads(proc, fmt=plistlib.FMT_BINARY,  dict_type=dict))

    elif _platform == "win64":
        #     #Windows 64-bit
        print("\nOS:\t", "Windows\n")
        #     nw = subprocess.check_output(['netsh','wlan','show','network'])
        #     ssid_data =nw.decode('ascii')
        #     print(ssid_data)
        #     results = ssid_data.replace("\r","")
        #     ls = results.split("\n")
        #     ls = ls[4:]
        #     ssids = []
        #     x = 0

        #     while x < len(ls):
        #         if x % 5 == 0:
        #             ssids.append(ls[x])
        #         x += 1
        #     print(ssids)

    global lbox
    lbox = tk.Listbox(wifi_QR, height=14, width=60,
                      bg=secColor, font=font2, border=4)
    lbox.grid(column=0,
              row=3,
              padx=20, sticky="nesw")

    # for network in ssids:
    #     lbox.insert("end", network)

    # schaltf1 = tk.Button(self, text="Aktion durchführen", command= ausgabe)
    # schaltf1.pack()

    # Button zum QR-Code Generieren
    get_QR_button = tk.Button(wifi_QR, text=get_From_XML('Generate_Code'), highlightbackground=bgColor, padx=4,
                              pady=2, font=font1, command=get_QR)
    get_QR_button.grid(column=0,
                       row=4,
                       padx=10,
                       pady=18)
    changeOnHover(get_QR_button, "green", "red")

    # Background Img
    img_label = Label(wifi_QR, image=new_bg_img, bg=bgColor)
    img_label.place(x=680, y=306)

    return wifi_QR


def get_Own_QR(note, new_bg_img):
    own_QR = Frame(note)
    own_QR.configure(background=bgColor)

    # Label
    label_In = tk.Label(own_QR, bg=bgColor, font=font2, fg="black",
                        text=get_From_XML('QR_Inhalt'))
    label_In.grid(column=0,
                  row=2,
                  padx=20,
                  pady=8)

    # Textbox
    global inputtxt
    inputtxt = Text(own_QR, height=20, width=60, bg=secColor, font=font2)
    inputtxt.grid(column=0,
                  row=3,
                  padx=20, sticky="nesw")

    # Button zum QR-Code Generieren
    get_QR_button = tk.Button(own_QR, text=get_From_XML('Generate_Code'), highlightbackground=bgColor, padx=4,
                              pady=2, font=font1, command=get_QR)
    changeOnHover(get_QR_button, "green", "red")
    get_QR_button.grid(column=0,
                       row=4,
                       padx=10,
                       pady=18)

    # Background Img
    img_label = Label(own_QR, image=new_bg_img, bg=bgColor)
    img_label.place(x=680, y=306)

    return own_QR


def get_Contact_QR(note, new_bg_img):
    contact_QR = Frame(note)
    contact_QR.configure(background=bgColor)

    # Background Img
    img_label = Label(contact_QR, image=new_bg_img, bg=bgColor)
    img_label.place(x=680, y=306)

    return contact_QR


def get_Settings(note, new_bg_img):
    settings = Frame(note)
    settings.configure(background=bgColor)

    # Background Img
    img_label = Label(settings, image=new_bg_img, bg=bgColor)
    img_label.place(x=680, y=306)

    langLabel = ttk.Label(settings, text="Language:")
    langLabel.configure(background=bgColor, font=font1, padding=10)
    langLabel.grid(column=0, row=2)

    chooseLang = ttk.Combobox(settings,
                              values=["Deutsch",
                                      "English"])

    chooseLang.configure(background=bgColor, font=font1,
                         takefocus=NONE, justify=CENTER)
    chooseLang.grid(column=1, row=2)
    chooseLang.current(1)

    pprint(dict(chooseLang))

    return settings


# Main
win = Tk()
win.iconbitmap(
    "/Users/christoph_rohde/Documents/02) Development/Python/Qrala/Qrala_Icon/Qrala_Icon_2.icns")
win.title("Qrala")
win.geometry("960x562")


# Menubar
menubar = Menu(win)
win.configure(background=bgColor, menu=menubar)


# File Menu
filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New File", command=clear_Txt)
filemenu.add_command(label="Open", command=onOpen)
filemenu.add_separator()
filemenu.add_command(label="Save File", command=onSave)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.quit)


# Qrala.png
bg_img = Image.open(
    '/Users/christoph_rohde/Documents/02) Development/Python/Qrala/Qrala_Icon/Qrala_1024x1024px.png')
new_bg_img = ImageTk.PhotoImage(bg_img.resize((200, 200)))


# Icons
contact_Icon = ImageTk.PhotoImage(Image.open(
    "/Users/christoph_rohde/Documents/02) Development/Python/Qrala/Qrala_Icon/Tab_icons/contact.png").resize((16, 16)))
wifi_Icon = ImageTk.PhotoImage(Image.open(
    "/Users/christoph_rohde/Documents/02) Development/Python/Qrala/Qrala_Icon/Tab_icons/wifi.png").resize((16, 16)))
setting_Icon = ImageTk.PhotoImage(Image.open(
    "/Users/christoph_rohde/Documents/02) Development/Python/Qrala/Qrala_Icon/Tab_icons/setting.png").resize((16, 16)))

# Notebook

note = ttk.Notebook(win)
note.pack(fill="both", expand=1)

own_QR = get_Own_QR(note, new_bg_img)
note.add(own_QR, text="Custom")

wifi_QR = get_WIFI_QR(note, new_bg_img)
note.add(wifi_QR,  text="WIFI", image=wifi_Icon, compound="left")

contact_QR = get_Contact_QR(note, new_bg_img)
note.add(contact_QR, text="Contact", image=contact_Icon, compound="left")

settings = get_Settings(note, new_bg_img)
note.add(settings,  text="Settings", image=setting_Icon, compound="left")
note.configure()



win.mainloop()


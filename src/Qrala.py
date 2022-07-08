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

# Import Modules
import VCard.VCardView as vcard
import WIFI.WIFI_View as wifi
import SystemDependency as sys_dep
import ConstantStyle as cs

# TKinter
from tkinter import filedialog, Text, Tk, Menu
from tkinter.constants import NORMAL, END, NONE, CENTER
from tkinter.ttk import Frame, Label, Button, Combobox, Notebook

# XML
import xml.dom.minidom

#
import cv2

# max. 4296 Zeichen
import qrcode
from PIL import Image, ImageTk

from pprint import pprint

BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2


OPERATING_SYSTEM = sys_dep.getOS()

rootPath = sys_dep.getRootPath()
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






def getCustomQR(note, new_bg_img):
    customQR = Frame(note)
    # customQR.configure(background=BACKGROUND)

    # Label
    label_In = Label(customQR,
                     background=BACKGROUND,
                     font=FONT_2,
                     foreground="black",
                     text=get_From_XML('QR_Inhalt'))
    label_In.grid(column=0,
                  row=2,
                  padx=20,
                  pady=8)

    # Textbox
    global inputText
    inputText = Text(customQR, height=20, width=60, bg=SECONDARY, font=FONT_2)
    inputText.grid(column=0,
                   row=3,
                   padx=20, sticky="nesw")

    # Button zum QR-Code Generieren
    getQrButton = Button(customQR,
                         text=get_From_XML('Generate_Code'),
                         # highlightbackground=BG_COLOR,
                         # padx=4,
                         # pady=2,
                         # font=FONT_1,
                         command=get_QR)
    cs.changeOnHover(getQrButton, "white", SECONDARY)
    getQrButton.grid(column=0,
                     row=4,
                     padx=10,
                     pady=18)

    # Background Img
    img_label = Label(customQR, image=new_bg_img, background=BACKGROUND)
    img_label.place(x=680, y=306)

    return customQR







def get_Settings(note, new_bg_img):
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


# Main
def main():
    win = Tk()
    win.iconbitmap(rootPath + "/Images/Qrala_Icon_2.icns")

    print(rootPath + "/Images/Qrala_Icon.icns")
    win.title("Qrala")
    win.geometry("960x562")

    # Menubar
    menubar = Menu(win)
    win.configure(background=BACKGROUND, menu=menubar)

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
    note = Notebook(win)
    note.pack(fill="both", expand=1)

    customQR = getCustomQR(note, new_bg_img)
    note.add(customQR, text="Custom")

    wifiQR = wifi.getFrame(note, new_bg_img)
    note.add(wifiQR, text="WIFI", image=wifi_Icon, compound="left")

    contactQR = vcard.getFrame(note, new_bg_img)
    note.add(contactQR, text="Contact", image=contact_Icon, compound="left")

    settings = get_Settings(note, new_bg_img)
    note.add(settings,  text="Settings", image=setting_Icon, compound="left")

    note.configure()

    win.mainloop()

main()

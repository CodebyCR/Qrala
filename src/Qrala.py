#################################################################################
#   Copyright of Christoph Rohde, 2022                                          #
#                                                                               #
#   Qrala Version: 0.9.6,             # #  # # # # # #   # #                    #
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
import Custom.CustomView as custom
import VCard.VCardView as vcard
import WIFI.WIFI_View as wifi
import Settings as setting
import SystemDependency as sys_dep
import ConstantStyle as cs

# tkinter
from tkinter import Tk, Menu
from tkinter.ttk import Notebook
from PIL import Image, ImageTk

# max. 4296 symbols

BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2


OPERATING_SYSTEM = sys_dep.getOS()

rootPath = sys_dep.getRootPath()



# Icons
bg_img = Image.open(
    rootPath + '/Images/Qrala_1024x1024px.png')
qrala_icon =  bg_img.resize((200, 200))
contact_16px = Image.open(
    rootPath + "/Images/Tab_icons/contact.png").resize((16, 16))
wifi_16px = Image.open(
    rootPath + "/Images/Tab_icons/wifi.png").resize((16, 16))
setting_16px = Image.open(
    rootPath + "/Images/Tab_icons/setting.png").resize((16, 16))


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

    # Qrala Menu
    qrala_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Qrala", menu=qrala_menu)
    qrala_menu.add_command(label="Preferences", command=custom.onOpen)
    qrala_menu.add_separator()
    qrala_menu.add_command(label="Exit", command=win.quit)

    # File Menu
    file_menu = Menu(menubar)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New File", command=custom.clearText)
    file_menu.add_command(label="Open", command=custom.onOpen)
    file_menu.add_separator()
    file_menu.add_command(label="Save File", command=custom.onSave)

    new_bg_img = ImageTk.PhotoImage(qrala_icon)
    contact_Icon = ImageTk.PhotoImage(contact_16px)
    wifi_Icon = ImageTk.PhotoImage(wifi_16px)
    setting_Icon = ImageTk.PhotoImage(setting_16px)

    # Notebook
    note = Notebook(win)
    note.pack(fill="both", expand=1)

    customQR = custom.getFrame(note, new_bg_img)
    note.add(customQR, text="Custom")

    wifiQR = wifi.getFrame(note, new_bg_img)
    note.add(wifiQR, text="WIFI", image=wifi_Icon, compound="left")

    contactQR = vcard.getFrame(note, new_bg_img)
    note.add(contactQR, text="Contact", image=contact_Icon, compound="left")

    settings = setting.get_frame(note, new_bg_img)
    note.add(settings,  text="Settings", image=setting_Icon, compound="left")

    note.configure()

    win.mainloop()

main()

#################################################################################
#   Copyright of Christoph Rohde, 2022                                          #
#                                                                               #
#   Qrala Version: 1.0.0,             # #  # # # # # #   # #                    #
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

import qrcode

import Custom.CustomView as custom
import VCard.VCardView as vcard
import WIFI.WIFI_View as wifi
from src import Settings as setting
from src import About
import SystemDependency as sys_dep
import ConstantStyle as cs
import src.Translations as translation
import cv2

# tkinter
from tkinter import Tk, Menu, filedialog
from tkinter.ttk import Notebook, Frame, Label, Button
from PIL import Image, ImageTk

from src.XML_Parser import XML_Parser

# max. 4296 symbols
current_qr_image = []

BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2

OPERATING_SYSTEM = sys_dep.get_os()

rootPath = sys_dep.get_root_path()

# Icons
image_path = sys_dep.get_image_path()
tab_icon_path = image_path.joinpath("Tab_icons")

bg_image_path = image_path.joinpath("Qrala_1024x1024px.png")
bg_img = Image.open(bg_image_path)
qrala_icon = bg_img.resize((200, 200))

contact_path = tab_icon_path.joinpath("contact.png")
contact_16px = Image.open(contact_path).resize((16, 16))

wifi_path = tab_icon_path.joinpath("wifi.png")
wifi_16px = Image.open(wifi_path).resize((16, 16))

setting_path = tab_icon_path.joinpath("setting.png")
setting_16px = Image.open(setting_path).resize((16, 16))


def create_qr(text: str) -> Image:
    # Get QR Code customization
    xml_parser = XML_Parser('Settings.xml')
    filling_color = xml_parser.get_tag_text("fill_color")
    background_color = xml_parser.get_tag_text("background_color")

    qr = qrcode.QRCode(
        #     # ERROR_CORRECT_H: Up to 30% of errors can be corrected
        #     error_correction=qrcode.constants.ERROR_CORRECT_H,
        error_correction=setting.get_correctness(),
        # Control the number of pixels contained in each small grid in the QR code
        box_size=2,
        border=3,
        #     # version value is an integer from 1 to 40, which controls the size of the QR code
        #     (the minimum value is 1, which is a 12*12 matrix)
        #     # If you want the program to automatically determine, set the value to None and use the fit parameter
        #     version=5,
    )

    qr.add_data(text)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color=filling_color, back_color=background_color)

    # qr = qr.png

    return qr_image


def set_qr_code_image(qr_text: str) -> Image:
    qr_image = create_qr(qr_text)
    qr_image_copy = qr_image.copy()

    qr_tk_image = qr_image_copy.resize((200, 200), Image.ANTIALIAS)
    # TODO: save as temporary file -> save a placeholder image

    qr_tk_image = ImageTk.PhotoImage(qr_tk_image)
    qr_code.configure(image=qr_tk_image)
    qr_code.image = qr_tk_image

    return qr_image


def generate_qr_text() -> str:
    qr_text = ""
    current_tab = note.index("current")

    if current_tab == 0:
        qr_text = custom.get_custom_text()

    elif current_tab == 1:
        qr_text = wifi.get_wifi_text()

    elif current_tab == 2:
        qr_text = vcard.get_vcard_text()

    return qr_text


def generate_qr_code():
    generated_qr_text = generate_qr_text()
    qr_image = set_qr_code_image(generated_qr_text)
    current_qr_image.insert(0, qr_image)


def generate_wifi_text():
    wifi_text = wifi.generate_wifi_qr()
    qr_image = set_qr_code_image(wifi_text)
    current_qr_image.insert(0, qr_image)


def on_save():
    file = filedialog.asksaveasfile(
        mode='w',
        initialdir="/",
        title="Save as",
        initialfile='My_QR_Code',
        filetypes=[('*.png', 'png'),
                   ('*.jpg', 'jpg')],
        defaultextension=".png"
    )

    #
    # my_file.write(current_qr_image)
    # my_file.close()

    if file:
        qr_image: Image = current_qr_image[0]

        qr_image.save(file.name)
        # else:
        #     qr_image.save(file.name + ".svg")

        qr_image.save(file)
        # file.close()


def open_file():
    # if else    #wenn kein qr code
    file_path = filedialog.askopenfilename()
    split_info = cv2.QRCodeDetector()
    temp = cv2.imread(file_path)
    result_text, _, _ = split_info.detectAndDecode(temp)
    print("QRCode:\t", result_text)

    # Show the text in custom tab
    note.select(0)
    custom.set_loaded_text(result_text)

    # Show loaded QR code in Qrala
    loaded_image = Image.open(file_path)
    loaded_image = loaded_image.resize((200, 200), Image.ANTIALIAS)
    qr_tk_image = ImageTk.PhotoImage(loaded_image)
    qr_code.configure(image=qr_tk_image)
    qr_code.image = qr_tk_image


def main() -> None:
    win = Tk()

    # Dock Icon
    if OPERATING_SYSTEM == "Mac OS":
        dock_image = Image.open("../Images/Qrala_Icon.icns")

    elif OPERATING_SYSTEM == "Windows":
        dock_image = Image.open("../Images/Qrala_Icon.ico")

    win.iconphoto(False, ImageTk.PhotoImage(dock_image))
    title_icon_path = image_path.joinpath("Qrala_Icon_2.icns")
    win.iconbitmap(title_icon_path)

    win.title("Qrala")
    win.geometry("960x562")
    win.resizable(False, False)

    # Menubar
    menubar = Menu(win)
    win.configure(background=BACKGROUND, menu=menubar)

    # Qrala Menu
    qrala_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Qrala", menu=qrala_menu)
    qrala_menu.add_command(label="Settings", command=setting.get_settings)
    qrala_menu.add_command(label="About", command=About.get_about)
    qrala_menu.add_separator()
    qrala_menu.add_command(label="Exit", command=win.quit)

    # File Menu
    file_menu = Menu(menubar)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New File", command=custom.clear_text_entry)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_separator()
    file_menu.add_command(label="Save As..", command=on_save)

    new_bg_img = ImageTk.PhotoImage(qrala_icon)
    contact_icon = ImageTk.PhotoImage(contact_16px)
    wifi_icon = ImageTk.PhotoImage(wifi_16px)

    # Notebook
    global note
    note = Notebook(win)
    note.pack(fill="both", expand=True)

    custom_qr: Frame = custom.getFrame(note)
    note.add(custom_qr, text="Custom")

    wifi_qr: Frame = wifi.get_frame(note)
    note.add(wifi_qr, text="WIFI", image=wifi_icon, compound="left")

    contact_qr: Frame = vcard.getFrame(note)
    note.add(contact_qr, text="VCard", image=contact_icon, compound="left")

    # note.configure()
    print("selected note: ", note.index("current"))

    # Background Img
    img_label = Label(win, image=new_bg_img)
    img_label.place(x=680, y=330)

    # Generated QR Code
    global qr_code
    qr_code = Label(win)
    qr_code.place(x=680, y=80)

    # Button to generate a QR-Code
    getQrButton = Button(win,
                         text=translation.get("Generate_Code"),
                         command=generate_qr_code)
    # cs.changeOnHover(getQrButton, "white", SECONDARY)
    getQrButton.place(x=470, y=480)

    # Button to generate wifi QR-Codes
    try_current_wifi = Button(wifi_qr,
                              text="Try current WIFI",
                              # font=FONT_1,
                              command=generate_wifi_text)

    if OPERATING_SYSTEM == "Mac OS":
        try_current_wifi.place(x=260, y=444)
    elif OPERATING_SYSTEM == "Windows":
        try_current_wifi.place(x=260, y=455)

    # cs.changeOnHover(try_current_wifi, "white", SECONDARY)

    win.mainloop()


if __name__ == "__main__":
    main()
    print("Qrala is closed")
    exit()

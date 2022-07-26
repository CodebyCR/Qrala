from tkinter import Text, filedialog
from tkinter.constants import END
from tkinter.ttk import Frame, Label, Button
import src.ConstantStyle as cs
import src.Translations as translation
import qrcode
import cv2

# Colors
BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY

# Fonts
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2


def onOpen():
    # if else    #wenn kein qr code
    file_path = filedialog.askopenfilename()
    splitIn = cv2.QRCodeDetector()
    temp = cv2.imread(file_path)
    result_text, _, _ = splitIn.detectAndDecode(temp)
    print("QRCode:\t", result_text)
    custom_text.delete(1.0, END)
    custom_text.insert(1.0, result_text)


def onSave():
    # qr=get_QR()
    print(filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                       filetypes=(("Python files", "*.png;*.jpg;*.svg"), ("All files", "*.*"))))


# Clear Function
def clearText():
    custom_text.delete(1.0, END)


# Grab the text from the textbox into the code
def get_QR():
    qr = qrcode.QRCode(
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        # Control the number of pixels contained in each small grid in the QR code
        box_size = 2,
        border = 3,
    )

    text = custom_text.get(1.0, END)
    qr.add_data(text)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color=cs.FILL_COLOR, back_color=cs.BACK_COLOR)

    qr_image.show()

    # qr = qr.png
    # qr = Image.open(qr)
    # qr_code = qr.resize((200, 200))
    # qr_label = Label(win, image=qr_code, bg=BG_COLOR)
    # qr_label.place(x=380, y=40, relwidth=1, relheight=1)
    return qr_image

def getFrame(note, new_bg_img):
    customQR = Frame(note)
    # customQR.configure(background=BACKGROUND)

    # Label
    label_In = Label(customQR,
                     background=BACKGROUND,
                     font=FONT_2,
                     foreground="black",
                     text=translation.get("QR_Inhalt")
                     )
    label_In.grid(column=0,
                  row=2,
                  padx=20,
                  pady=8)

    # Textbox
    global custom_text
    custom_text = Text(customQR, height=20, width=60, bg=SECONDARY, font=FONT_2)
    custom_text.grid(column=0,
                   row=3,
                   padx=20, sticky="nesw")

    # Button zum QR-Code Generieren
    getQrButton = Button(customQR,
                         text=translation.get("Generate_Code"),
                         # highlightbackground=BG_COLOR,
                         # padx=4,
                         # pady=2,
                         # font=FONT_1,
                         command=get_QR)
    # cs.changeOnHover(getQrButton, "white", SECONDARY)
    getQrButton.grid(column=0,
                     row=4,
                     padx=10,
                     pady=18)

    # Background Img
    img_label = Label(customQR, image=new_bg_img, background=BACKGROUND)
    img_label.place(x=680, y=306)

    return customQR
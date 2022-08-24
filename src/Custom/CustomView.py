from tkinter import Text, filedialog, Image
from tkinter.constants import END
from tkinter.ttk import Frame, Label
import src.ConstantStyle as cs
import src.Translations as translation

import cv2

# Colors
BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY

# Fonts
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2


# def onOpen():
#     # if else    #wenn kein qr code
#     file_path = filedialog.askopenfilename()
#     splitIn = cv2.QRCodeDetector()
#     temp = cv2.imread(file_path)
#     result_text, _, _ = splitIn.detectAndDecode(temp)
#     print("QRCode:\t", result_text)
#     custom_text.delete(1.0, END)
#     custom_text.insert(1.0, result_text)
#
#     loaded_image = Image.open(file_path)
#     qr_tk_image = ImageTk.PhotoImage(qr_tk_image)
#     qr_code.configure(image=qr_tk_image)


def set_loaded_text(text):
    custom_text.delete(1.0, END)
    custom_text.insert(1.0, text)


# Clear Function
# def clear_text_entry(entry: Entry) -> None:
#     entry.delete(1.0, END)

def clear_text_entry() -> None:
    custom_text.delete(1.0, END)


# Grab the text from the textbox into the code
def get_custom_text():
    text = custom_text.get(1.0, END)
    return text


def getFrame(note):
    customQR = Frame(note, width=600)

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
    custom_text = Text(customQR, height=16, width=50, font=FONT_2)
    custom_text.grid(column=0,
                     row=3,
                     padx=20, sticky="nesw")

    return customQR

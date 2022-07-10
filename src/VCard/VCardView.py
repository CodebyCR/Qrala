from tkinter.constants import DISABLED, NORMAL, END
from tkinter.ttk import Entry, Frame, Label, Button
from src.VCard import VCardModel as model
import src.ConstantStyle as cs
import src.Translations as translation

# Colors
BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY

# Fonts
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2



def create_Entry(frame, current_column, current_row, placeholder_text):
    entry_name = Entry(frame, width=30)
    entry_name.insert(0, placeholder_text)
    entry_name.grid(column=current_column,
                    row=current_row,
                    padx=20,
                    pady=8)
    return entry_name

def removePlaceholder(event, current_entry):
    current_entry.configure(state=NORMAL)
    current_entry.delete(0, END)


def get_text(entry, placeholder_text):
    input = entry.get()
    input = input.strip()

    if input == "" or input == placeholder_text:
        input = None

    return input

def create_tuple():
    postcode_str = get_text(postcode, "Postalcode")

def getFrame(note, new_bg_img):
    vcard_frame = Frame(note)

    # Background Img
    img_label = Label(vcard_frame, image=new_bg_img, background=BACKGROUND)
    img_label.place(x=680, y=306)

    # Label
    label_In = Label(vcard_frame, background=BACKGROUND, font=FONT_2, foreground="black",
                        text='Enter your contact information for the VCard')
    label_In.grid(column=0,
                  row=1,
                  padx=20,
                  pady=8)


    # Shown name
    shown_name = create_Entry(vcard_frame, 0, 2, "Shown Name")
    shown_name.configure(state=DISABLED)
    shown_name.bind("<Button-1>", lambda event: removePlaceholder(event, shown_name))

    # Last name
    last_name = create_Entry(vcard_frame, 0, 3, "Last Name")
    last_name.configure(state=DISABLED)
    last_name.bind("<Button-1>", lambda event: removePlaceholder(event, last_name))

    # First name
    first_name = create_Entry(vcard_frame, 1, 3, "First Name")
    first_name.configure(state=DISABLED)
    first_name.bind("<Button-1>", lambda event: removePlaceholder(event, first_name))

    # Telephone number
    telephone_number = create_Entry(vcard_frame, 0, 4, "Tel. Number")
    telephone_number.configure(state=DISABLED)
    telephone_number.bind("<Button-1>", lambda event: removePlaceholder(event, telephone_number))

    # Email
    email = create_Entry(vcard_frame, 1, 4, "Email")
    email.configure(state=DISABLED)
    email.bind("<Button-1>", lambda event: removePlaceholder(event, email))

    # Organization
    organization = create_Entry(vcard_frame, 0, 5, "Organization")
    organization.configure(state=DISABLED)
    organization.bind("<Button-1>", lambda event: removePlaceholder(event, organization))

    # Address
    address = create_Entry(vcard_frame, 1, 5, "Address")
    address.configure(state=DISABLED)
    address.bind("<Button-1>", lambda event: removePlaceholder(event, address))

    # City
    city = create_Entry(vcard_frame, 0, 6, "City")
    city.configure(state=DISABLED)
    city.bind("<Button-1>", lambda event: removePlaceholder(event, city))

    # Country
    country = create_Entry(vcard_frame, 1, 6, "Country")
    country.configure(state=DISABLED)
    country.bind("<Button-1>", lambda event: removePlaceholder(event, country))

    # Postcode
    global postcode
    postcode = create_Entry(vcard_frame, 0, 7, "Postalcode")
    postcode.configure(state=DISABLED)
    postcode.bind("<Button-1>", lambda event: removePlaceholder(event, postcode))


    get_QR_button = Button(vcard_frame,
                           text=translation.get("Generate_Code"),
                           command=model.create_vcard_qr)



    get_QR_button.grid(column=1,
                       row=7,
                       padx=10,
                       pady=18)
    cs.changeOnHover(get_QR_button, "white", SECONDARY)

    return vcard_frame

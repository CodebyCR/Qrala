from tkinter.constants import DISABLED, NORMAL, END
from tkinter.ttk import Entry, Frame, Label
from src.VCard import VCardModel as model
import src.ConstantStyle as cs


# Colors
BACKGROUND = cs.BACKGROUND
SECONDARY = cs.SECONDARY

# Fonts
FONT_1 = cs.FONT_1
FONT_2 = cs.FONT_2

# Const Placeholder
SHOWN_NAME = "Shown Name"
LAST_NAME = "Last Name"
FIRST_NAME = "First Name"
TEL_NUMBER = "Tel. Number"
EMAIL = "Email"
ORGANIZATION = "Organization"
ADDRESS = "Address"
CITY = "City"
COUNTRY = "Country"
POSTALCODE = "Postalcode"
BIRTHDAY = "Birthday (mm.dd.yyyy)"
WEBSITE = "http://www.website.com/"

entry_List = []


def create_Entry(frame: any, current_column: any, current_row: any, placeholder_text: any) -> Entry:
    entry_name = Entry(frame, width=30)
    entry_name.insert(0, placeholder_text)
    entry_name.grid(column=current_column,
                    row=current_row,
                    padx=20,
                    pady=8)
    entry_List.append(entry_name)
    return entry_name


def removePlaceholder(event: any, current_entry: Entry) -> None:
    current_entry.configure(state=NORMAL)
    current_entry.delete(0, END)


def get_dict() -> dict:
    entry_dict = {SHOWN_NAME: entry_List[0].get(),
                  LAST_NAME: entry_List[1].get(),
                  FIRST_NAME: entry_List[2].get(),
                  TEL_NUMBER: entry_List[3].get(),
                  EMAIL: entry_List[4].get(),
                  ORGANIZATION: entry_List[5].get(),
                  ADDRESS: entry_List[6].get(),
                  CITY: entry_List[7].get(),
                  COUNTRY: entry_List[8].get(),
                  POSTALCODE: entry_List[9].get(),
                  BIRTHDAY: entry_List[10].get(),
                  WEBSITE: entry_List[11].get()}

    print(entry_dict)

    return entry_dict


# def create_vcard_text():
#     entry_dict = get_dict()
#
#     # vCard_v3 = """
#     # BEGIN:VCARD
#     # VERSION:3.0
#     # FN:Christoph Rohde
#     # N:Rohde;Christoph
#     # BDAY:--01.02
#     # ORG;TYPE=work:Sim
#     # ADR;WORK:;;Weinberg 48;Wuppertal;;42109
#     # TEL;WORK;VOICE:015785407998
#     # URL:http://www.website.com/
#     # EMAIL;
#     # iich@live.de
#     # END:VCARD"""
#     #
#     # vcard_text = str(vCard_v3)
#
#     model.create_vcard_qr(entry_dict)


def get_vcard_text() -> str:
    entry_dict = get_dict()
    vcard_txt = model.create_vcard_text(entry_dict)
    return vcard_txt


def getFrame(note: any) -> Frame:
    vcard_frame = Frame(note)

    # Label
    label_In = Label(vcard_frame, background=BACKGROUND, font=FONT_2, foreground="black",
                     text='Enter your contact information for the VCard')
    label_In.grid(column=0,
                  row=1,
                  padx=20,
                  pady=8)

    # Shown name
    global shown_name
    shown_name = create_Entry(vcard_frame, 0, 2, SHOWN_NAME)
    shown_name.configure(state=DISABLED)
    shown_name.bind("<Button-1>", lambda event: removePlaceholder(event, shown_name))

    # Last name
    global last_name
    last_name = create_Entry(vcard_frame, 0, 3, LAST_NAME)
    last_name.configure(state=DISABLED)
    last_name.bind("<Button-1>", lambda event: removePlaceholder(event, last_name))

    # First name
    global first_name
    first_name = create_Entry(vcard_frame, 1, 3, FIRST_NAME)
    first_name.configure(state=DISABLED)
    first_name.bind("<Button-1>", lambda event: removePlaceholder(event, first_name))

    # Telephone number
    global telephone_number
    telephone_number = create_Entry(vcard_frame, 0, 4, TEL_NUMBER)
    telephone_number.configure(state=DISABLED)
    telephone_number.bind("<Button-1>", lambda event: removePlaceholder(event, telephone_number))

    # Email
    global email
    email = create_Entry(vcard_frame, 1, 4, EMAIL)
    email.configure(state=DISABLED)
    email.bind("<Button-1>", lambda event: removePlaceholder(event, email))

    # Organization
    global organization
    organization = create_Entry(vcard_frame, 0, 5, ORGANIZATION)
    organization.configure(state=DISABLED)
    organization.bind("<Button-1>", lambda event: removePlaceholder(event, organization))

    # Address
    global address
    address = create_Entry(vcard_frame, 1, 5, ADDRESS)
    address.configure(state=DISABLED)
    address.bind("<Button-1>", lambda event: removePlaceholder(event, address))

    # City
    global city
    city = create_Entry(vcard_frame, 0, 6, CITY)
    city.configure(state=DISABLED)
    city.bind("<Button-1>", lambda event: removePlaceholder(event, city))

    # Country
    global country
    country = create_Entry(vcard_frame, 1, 6, COUNTRY)
    country.configure(state=DISABLED)
    country.bind("<Button-1>", lambda event: removePlaceholder(event, country))

    # Postcode
    global postcode
    postcode = create_Entry(vcard_frame, 0, 7, POSTALCODE)
    postcode.configure(state=DISABLED)
    postcode.bind("<Button-1>", lambda event: removePlaceholder(event, postcode))

    # Birthday
    global birthday
    birthday = create_Entry(vcard_frame, 1, 7, BIRTHDAY)
    birthday.configure(state=DISABLED)
    birthday.bind("<Button-1>", lambda event: removePlaceholder(event, birthday))

    # Website
    global website
    website = create_Entry(vcard_frame, 0, 8, WEBSITE)
    website.configure(state=DISABLED)
    website.bind("<Button-1>", lambda event: removePlaceholder(event, website))

    return vcard_frame

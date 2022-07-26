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

def create_Entry(frame, current_column, current_row, placeholder_text):
    entry_name = Entry(frame, width=30)
    entry_name.insert(0, placeholder_text)
    entry_name.grid(column=current_column,
                    row=current_row,
                    padx=20,
                    pady=8)
    entry_List.append(entry_name)
    return entry_name

def removePlaceholder(event, current_entry):
    current_entry.configure(state=NORMAL)
    current_entry.delete(0, END)




def create_text():

    entry_dic = {}

    entry_dic[SHOWN_NAME] = entry_List[0].get()
    entry_dic[LAST_NAME] = entry_List[1].get()
    entry_dic[FIRST_NAME] = entry_List[2].get()
    entry_dic[TEL_NUMBER] = entry_List[3].get()
    entry_dic[EMAIL] = entry_List[4].get()
    entry_dic[ORGANIZATION] = entry_List[5].get()
    entry_dic[ADDRESS] = entry_List[6].get()
    entry_dic[CITY] = entry_List[7].get()
    entry_dic[COUNTRY] = entry_List[8].get()
    entry_dic[POSTALCODE] = entry_List[9].get()
    entry_dic[BIRTHDAY] = entry_List[10].get()
    entry_dic[WEBSITE] = entry_List[11].get()

    print(entry_dic)
    
    return entry_dic
    
def create_vcard_text():
    entry_dict = create_text()

    # vCard_v3 = f"""
    # BEGIN:VCARD
    # VERSION:3.0
    # FN:{entry_dict[SHOWN_NAME]}
    # N:{entry_dict[LAST_NAME]};{entry_dict[FIRST_NAME]}
    # BDAY:--0203
    # ORG;TYPE=work:{entry_dict[ORGANIZATION]}
    # ADR;WORK:;;{entry_dict[ADDRESS]};{entry_dict[CITY]};;{entry_dict[POSTALCODE]}
    # TEL;WORK;VOICE:{entry_dict[TEL_NUMBER]}
    # TEL;TYPE=CELL:+49 178 12345678
    # TEL;WORK;FAX:+49 7531 123456
    # URL:http://www.website.com/
    # EMAIL;INTERNET:{entry_dict[EMAIL]}
    # END:VCARD
    # """

    vCard_v3 = """
    BEGIN:VCARD
    VERSION:3.0
    FN:Christoph Rohde
    N:Rohde;Christoph
    BDAY:--01.02
    ORG;TYPE=work:Sim
    ADR;WORK:;;Weinberg 48;Wuppertal;;42109
    TEL;WORK;VOICE:015785407998
    URL:http://www.website.com/
    EMAIL;
    iich@live.de
    END:VCARD"""

    # vCard_v3 = f"""
    # BEGIN:VCARD
    # VERSION:3.0
    # FN:{entry_dict[SHOWN_NAME]}
    # N:{entry_dict[LAST_NAME]};{entry_dict[FIRST_NAME]}
    # BDAY:--01.02
    # ORG;TYPE=work:{entry_dict[ORGANIZATION]}
    # ADR;WORK:;;{entry_dict[ADDRESS]};{entry_dict[CITY]};;{entry_dict[POSTALCODE]}
    # TEL;WORK;VOICE:{entry_dict[TEL_NUMBER]}
    # URL:http://www.website.com/
    # EMAIL;
    # {entry_dict[EMAIL]}
    # END:VCARD
    # """


    vcard_text = str(vCard_v3)

    model.create_vcard_qr(entry_dict)

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

    get_QR_button = Button(vcard_frame,
                           text=translation.get("Generate_Code"),
                           command=create_vcard_text)



    get_QR_button.grid(column=1,
                       row=8,
                       padx=10,
                       pady=18)
    # cs.changeOnHover(get_QR_button, "white", SECONDARY)


    return vcard_frame

from tkinter.constants import DISABLED, NORMAL, END
from tkinter.ttk import Entry, Frame, Label

# Colors
BACKGROUND = "#696969"
SECONDARY = "#b5b5b5"

# Fonts
FONT_1 = ("Helvetica", 14)
FONT_2 = ("Helvetica", 16)

def removePlaceholder(event, current_entry):
    current_entry.configure(state=NORMAL)
    current_entry.delete(0, END)

def getFrame(note, new_bg_img):
    vcard_frame = Frame(note)
    # vcard_frame.configure( background=BACKGROUND)

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

    showed_name = Entry(vcard_frame, width=30)
    showed_name.grid(column=0,
                        row=2,
                        padx=20,
                        pady=8)
    showed_name.insert(0, 'Showed Name')
    showed_name.configure(state=DISABLED)
    showed_name.bind("<Button-1>", lambda event: removePlaceholder(event, showed_name))

    last_name = Entry(vcard_frame, width=30)
    last_name.grid(column=0,
                        row=3,
                        padx=20,
                        pady=8)
    last_name.insert(0, 'Last Name')
    last_name.configure(state=DISABLED)
    last_name.bind("<Button-1>", lambda event: removePlaceholder(event, last_name))

    first_name = Entry(vcard_frame, width=30)
    first_name.grid(column=1,
                        row=3,
                        padx=20,
                        pady=8)
    first_name.insert(0, 'First Name')
    first_name.configure(state=DISABLED)
    first_name.bind("<Button-1>", lambda event: removePlaceholder(event, first_name))

    # Tel Number Entry
    tel_number = Entry(vcard_frame, width=30)
    tel_number.grid(column=0,
                        row=4,
                        padx=20,
                        pady=8)
    tel_number.insert(0, 'Tel. Number')
    tel_number.configure(state=DISABLED)
    tel_number.bind("<Button-1>", lambda event: removePlaceholder(event, tel_number))

    # Email Entry
    email = Entry(vcard_frame, width=30)
    email.grid(column=1,
                        row=4,
                        padx=20,
                        pady=8)
    email.insert(0, 'Email')
    email.configure(state=DISABLED)
    email.bind("<Button-1>", lambda event: removePlaceholder(event, email))

    # organization Entry
    organization = Entry(vcard_frame, width=30)
    organization.grid(column=0,
                        row=5,
                        padx=20,
                        pady=8)
    organization.insert(0, 'Organization')
    organization.configure(state=DISABLED)
    organization.bind("<Button-1>", lambda event: removePlaceholder(event, organization))

    # address Entry
    address = Entry(vcard_frame, width=30)
    address.grid(column=1,
                        row=5,
                        padx=20,
                        pady=8)
    address.insert(0, 'Address')
    address.configure(state=DISABLED)
    address.bind("<Button-1>", lambda event: removePlaceholder(event, address))

    # city Entry
    city = Entry(vcard_frame, width=30)
    city.grid(column=0,
                        row=6,
                        padx=20,
                        pady=8)
    city.insert(0, 'City')
    city.configure(state=DISABLED)
    city.bind("<Button-1>", lambda event: removePlaceholder(event, city))

    # country Entry
    country = Entry(vcard_frame, width=30)
    country.grid(column=1,
                        row=6,
                        padx=20,
                        pady=8)
    country.insert(0, 'Country')
    country.configure(state=DISABLED)
    country.bind("<Button-1>", lambda event: removePlaceholder(event, country))

    # postalcode Entry
    postalcode = Entry(vcard_frame, width=30)
    postalcode.grid(column=0,
                        row=7,
                        padx=20,
                        pady=8)
    postalcode.insert(0, 'Postalcode')
    postalcode.configure(state=DISABLED)
    postalcode.bind("<Button-1>", lambda event: removePlaceholder(event, postalcode))


    return vcard_frame
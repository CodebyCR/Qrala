
import qrcode

# vCard_v3 = """
# BEGIN:VCARD
# VERSION:3.0
# FN:Christoph Rohde
# N:Rohde;Christoph
# BDAY:--01.02
# ORG;TYPE=work:Sim
# ADR;WORK:;;Weinberg 48;Wuppertal;;42109
# TEL;WORK;VOICE:015785407998
# URL:http://www.website.com/
# EMAIL;
# iich@live.de
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

# vCard_v3 = """
# BEGIN:VCARD
# VERSION:3.0
# FN:Christoph Rohde
# N:Rohde;Christoph
# BDAY:--01.02
# ORG;TYPE=work:Sim
# ADR;WORK:;;Weinberg 48;Wuppertal;;42109
# TEL;WORK;VOICE:015785407998
# URL:http://www.website.com/
# EMAIL;
# iich@live.de
# END:VCARD"""

# vCard_v3 = """
# BEGIN:VCARD
# VERSION:3.0
# FN:Christoph Rohde
# N:Rohde;Christoph
# BDAY:--01.02
# ORG;TYPE=work:Sim
# ADR;WORK:;;Weinberg 48;Wuppertal;;42109
# TEL;WORK;VOICE:01575407998
# URL:http://www.website.com/
# EMAIL;
# iich@live.de
# END:VCARD
# """


vCard_v4 = """
BEGIN:VCARD
VERSION:4.0
N:Gump;Forrest;;Mr.;
FN:Sheri Nom
ORG:Sheri Nom Co.
TITLE:Ultimate Warrior
PHOTO;MEDIATYPE#image/gif:http://www.sherinnom.com/dir_photos/my_photo.gif
TEL;TYPE#work,voice;VALUE#uri:tel:+1-111-555-1212
TEL;TYPE#home,voice;VALUE#uri:tel:+1-404-555-1212
ADR;TYPE#WORK;PREF#1;LABEL#"Normality\nBaytown\, LA 50514\nUnited States of America":;;100 Waters Edge;Baytown;LA;50514;United States of America
ADR;TYPE#HOME;LABEL#"42 Plantation St.\nBaytown\, LA 30314\nUnited States of America":;;42 Plantation St.;Baytown;LA;30314;United States of America
EMAIL:sherinnom@example.com
REV:20080424T195243Z
x-qq:21588891
END:VCARD
"""

vcard_text = ""
vcard_text += "BEGIN:VCARD\n"
vcard_text += "VERSION:4.0"


def create_vcard_qr(entry_dict):

    vCard_v3 = f"""
    BEGIN:VCARD
    VERSION:3.0
    FN:{entry_dict["Shown Name"]}
    N:{entry_dict["Last Name"]};{entry_dict["First Name"]}
    BDAY:--01.02
    ORG;TYPE=work:{entry_dict["Organization"]}
    ADR;WORK:;;{entry_dict["Address"]};{entry_dict["City"]};;{entry_dict["Postalcode"]}
    TEL;WORK;VOICE:{entry_dict["Tel. Number"]}
    URL:http://www.website.com/
    EMAIL;
    {entry_dict["Email"]}
    END:VCARD
    """

    vcard_txt = str(vCard_v3)

    qr = qrcode.QRCode(
        # version value is an integer from 1 to 40, which controls the size of the QR code (the minimum value is 1, which is a 12*12 matrix)
        # If you want the program to automatically determine, set the value to None and use the fit parameter
        version=5,

        # ERROR_CORRECT_H: About 30% or less errors can be corrected
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        # Control the number of pixels contained in each small grid in the QR code
        box_size=2,
        border=3,
    )
    print("this is the current string: ", vcard_txt)
    # Fill vCard data into qr
    qr.add_data(vcard_txt)

    qr.make(fit=True)
    qr_image = qr.make_image()

    qr_image.show()
    # Generate picture
    return qr_image
    # image.thumbnail((500, 500))
    # # Save the picture to the specified path file
    # image.show("QR.png")


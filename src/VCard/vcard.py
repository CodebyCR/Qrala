
# create VCard QR Code
#from vobject import vCard
import qrcode

# vCard content

vCard_v3 = """
BEGIN:VCARD
VERSION:3.0
FN:Vorname Nachname
N:Nachname;Vorname
BDAY:--0203
ORG;TYPE=work:Viagenie
ADR;WORK:;;Straße Hausnummer;Ort;;Postleitzahl
TEL;WORK;VOICE:+49 7531 12345
TEL;TYPE=CELL:+49 178 12345678
TEL;WORK;FAX:+49 7531 123456
URL:http://www.website.com/
EMAIL;INTERNET:email.address@website.com
END:VCARD
"""

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

def create_vcard_qr(vcard_str):
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

    # Fill vCard data into qr
    qr.add_data(vCard_v4)

    qr.make(fit=True)

    # Generate picture
    return qr.make_image()
    # image.thumbnail((500, 500))
    # # Save the picture to the specified path file
    # image.show("QR.png")


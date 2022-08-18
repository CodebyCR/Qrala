
# TODO: for the future:
# vCard_v4 = """
# BEGIN:VCARD
# VERSION:4.0
# N:Gump;Forrest;;Mr.;
# FN:Sheri Nom
# ORG:Sheri Nom Co.
# TITLE:Ultimate Warrior
# PHOTO;MEDIATYPE#image/gif:http://www.sherinnom.com/dir_photos/my_photo.gif
# TEL;TYPE#work,voice;VALUE#uri:tel:+1-111-555-1212
# TEL;TYPE#home,voice;VALUE#uri:tel:+1-404-555-1212
# ADR;TYPE#WORK;PREF#1;LABEL#"Normality\nBaytown\, LA 50514\nUnited States of America":;;100 Waters Edge;Baytown;LA;50514;United States of America
# ADR;TYPE#HOME;LABEL#"42 Plantation St.\nBaytown\, LA 30314\nUnited States of America":;;42 Plantation St.;Baytown;LA;30314;United States of America
# EMAIL:sherinnom@example.com
# REV:20080424T195243Z
# x-qq:21588891
# END:VCARD
# """

def create_vcard_text(entry_dict: dict) -> str:
    vcard_txt = '''
    BEGIN:VCARD
    VERSION:3.0'''
    vcard_txt += f"FN:{entry_dict['Shown Name']}\n"
    vcard_txt += f"N:{entry_dict['Last Name']};{entry_dict['First Name']}\n"
    vcard_txt += f"BDAY:--01.02\n"
    vcard_txt += f"ORG;TYPE=work:{entry_dict['Organization']}\n"
    vcard_txt += f"ADR;WORK:;;{entry_dict['Address']};{entry_dict['City']};;{entry_dict['Postalcode']}\n"
    vcard_txt += f"TEL;WORK;VOICE:{entry_dict['Tel. Number']}\n"
    vcard_txt += f"URL:http://www.website.com/\n"
    vcard_txt += f"EMAIL;\n"
    vcard_txt += f"{entry_dict['Email']}\n"
    vcard_txt += "END:VCARD"

    print("this is the current string: ", vcard_txt)
    return vcard_txt





# def create_vcard_qr(text: str) -> PilImage:
#     qr = qrcode.QRCode(
#         # version value is an integer from 1 to 40, which controls the size of the QR code (the minimum value is 1, which is a 12*12 matrix)
#         # If you want the program to automatically determine, set the value to None and use the fit parameter
#         version=5,
#
#         # ERROR_CORRECT_H: About 30% or less errors can be corrected
#         error_correction=qrcode.constants.ERROR_CORRECT_H,
#
#         # Control the number of pixels contained in each small grid in the QR code
#         box_size=2,
#         border=3,
#     )
#
#     # Fill vCard data into qr
#     qr.add_data(vcard_txt)
#
#     qr.make(fit=True)
#     qr_image = qr.make_image(fill_color=cs.FILL_COLOR, back_color=cs.BACK_COLOR)
#
#     qr_image.show()
#     # Generate picture
#     return qr_image
#     # image.thumbnail((500, 500))
#     # # Save the picture to the specified path file
#     # image.show("QR.png")

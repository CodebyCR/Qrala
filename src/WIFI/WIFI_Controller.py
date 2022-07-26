import subprocess
import src.SystemDependency as sys_dep
#from wifi_qrcode_generator import wifi_qrcode
import qrcode
import src.ConstantStyle as cs

# Mac command to get WI-FI Password
# /System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I | awk -F: '/ SSID/{print $2}'
# security find-generic-password -wa SSID

OPERATING_SYSTEM = sys_dep.getOS()

# Check for OS
if OPERATING_SYSTEM == "darwin":
    # MAC OS
    print("\nOS:\t", "Mac OS\n")

elif OPERATING_SYSTEM == "win64":
    # Windows 64-bit
    print("\nOS:\t", "Windows\n")


def get_current_ssid():
    # get SSID from Terminal
    get_current_SSID_Command = "/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I | awk -F: '/ SSID/{print $2}'"
    ssid = subprocess.check_output(get_current_SSID_Command, shell=True)

    # Clean up SSID
    ssid = str(ssid).replace("b' ", "")
    ssid = ssid.replace("\\n'", "")
    print(f"SSID: {ssid}")

    return ssid


def get_current_password(ssid):
    # get password for the current SSID from Terminal
    get_SSID_password_Command = f"security find-generic-password -wa {ssid}"
    password = subprocess.check_output(get_SSID_password_Command, shell=True)

    # Clean up password
    password = str(password).replace("b'", "")
    password = password.replace("\\n'", "")
    print(f"Password: {password}")

    return password


# working on macOS
def create_wifi_qr(ssid, password):
    #works
    # Use wifi_qrcode() to create a QR image
    # qr_image = wifi_qrcode(ssid,
    #                        False,
    #                        "WPA",
    #                        password)

    # wifi text
    wifi_text = "WIFI:T:WPA;S:"
    wifi_text += ssid
    wifi_text += f""";P:"""
    wifi_text += password
    wifi_text += f""";H:false;;"""


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
    qr.add_data(wifi_text)

    qr.make(fit=True)

    qr_image = qr.make_image(fill_color=cs.FILL_COLOR, back_color=cs.BACK_COLOR)
    qr_image.show()

    return qr_image


def try_current_wifi():
    try:
        ssid = get_current_ssid()
        password = get_current_password(ssid)

        create_wifi_qr(ssid, password)

    except:
        print("No wifi connection")

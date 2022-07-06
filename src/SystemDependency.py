import wifi_qrcode_generator as qr
import os
import subprocess
from sys import platform as _platform


def getOS():
    if _platform == "darwin":
        return "Mac OS"
    elif _platform == "win64":
        return "Windows"


def getRootPath():
    if _platform == "darwin":
        return os.path.dirname(os.getcwd())
    elif _platform == "win64":
        return os.path.dirname(os.getcwd())


# working on mac
# Import module
def createWIFI_QR(note, new_bg_img):
    # get SSID from termianl
    get_current_SSID_Command = "/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I | awk -F: '/ SSID/{print $2}'"

    ssid = subprocess.check_output(get_current_SSID_Command, shell=True)

    # Clean up SSID
    ssid = str(ssid).replace("b' ", "")
    ssid = ssid.replace("\\n'", "")
    print(f"SSID: {ssid}")

    # get password for the current SSID from termianl
    get_SSID_password_Command = f"security find-generic-password -wa {ssid}"
    password = subprocess.check_output(get_SSID_password_Command, shell=True)

    # Clean up password
    password = str(password).replace("b'", "")
    password = password.replace("\\n'", "")
    print(f"Password: {password}")


    # # Use wifi_qrcode() to create a QR image
    wifiQR = qr.wifi_qrcode(ssid,
                            False,
                            "WPA",
                            password)
    wifiQR.show()


# Mac command to get WIFI Password
# /System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I | awk -F: '/ SSID/{print $2}'
# security find-generic-password -wa MagentaWLAN-ZKSP

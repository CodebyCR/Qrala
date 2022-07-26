import subprocess
import src.SystemDependency as sys_dep
from wifi_qrcode_generator import wifi_qrcode

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
    # Use wifi_qrcode() to create a QR image
    qr_image = wifi_qrcode(ssid,
                           False,
                           "WPA",
                           password)
    qr_image.show()

    return qr_image


def try_current_wifi():
    try:
        ssid = get_current_ssid()
        password = get_current_password(ssid)

        create_wifi_qr(ssid, password)

    except:
        print("No wifi connection")

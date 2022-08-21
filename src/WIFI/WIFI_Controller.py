import subprocess
from typing import Optional

import src.SystemDependency as sys_dep

# Mac command to get WI-FI Password
# /System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I | awk -F: '/ SSID/{print $2}'
# security find-generic-password -wa SSID

OPERATING_SYSTEM = sys_dep.get_os()

# Check for OS
print(f"\nOS:\t {OPERATING_SYSTEM}\n")


def get_current_ssid() -> str:
    # get SSID from Terminal
    ssid_command = ""
    ssid = ""

    if OPERATING_SYSTEM == "Mac OS":
        ssid_command = "/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport" \
                       " -I | awk -F: '/ SSID/{print $2}'"
        ssid = subprocess.check_output(ssid_command, shell=True)

        # Clean up SSID
        ssid = str(ssid).replace("b' ", "")
        ssid = ssid.replace("\\n'", "")

    elif OPERATING_SYSTEM == "Windows":
        ssid_command = "Netsh WLAN show interfaces"
        temp_ssid = subprocess.check_output(ssid_command, shell=True)
        ssid_information: list = str(temp_ssid).split(":")

        ssid = str(ssid_information[12]).split("\\r\\n")[0]
        ssid = ssid.strip()

    print(f"SSID: {ssid}")

    return ssid


def get_current_password(ssid) -> str:
    password = ""

    print(f"operating system: {OPERATING_SYSTEM}")
    if OPERATING_SYSTEM == "Mac OS":
        # get password for the current SSID from Terminal
        password_command = f"security find-generic-password -wa {ssid}"
        password = subprocess.check_output(password_command, shell=True)

        # Clean up password
        password = str(password).replace("b'", "")
        password = password.replace("\\n'", "")
        print(f"Password: {password}")

    elif OPERATING_SYSTEM == "Windows":
        # get password for the current SSID from CMD
        password_command = f"Netsh wlan show profile name={ssid} key=clear"
        password = subprocess.check_output(password_command, shell=True)

        # Clean up password
        password = str(password).split(":")[21].split("\\r\\n")[0]
        password = password.strip()

    print(f"Password: {password}")
    return password


# working on macOS
def create_wifi_text(ssid: any, password: any) -> str:
    # wi-fi text
    wifi_text = "WIFI:T:WPA;S:"
    wifi_text += ssid
    wifi_text += ";P:"
    wifi_text += password
    wifi_text += ";H:false;;"

    return wifi_text


def try_current_wifi() -> tuple[str, str, str]:
    ssid = get_current_ssid()

    password = get_current_password(ssid)

    wifi_text = create_wifi_text(ssid, password)

    wifi_tuple = (ssid, password, wifi_text)
    return wifi_tuple

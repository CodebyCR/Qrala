import subprocess

import src.SystemDependency as sys_dep

# Mac command to get WI-FI Password
# /System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I | awk -F: '/ SSID/{print $2}'
# security find-generic-password -wa SSID

OPERATING_SYSTEM = sys_dep.get_os()

# Check for OS
if OPERATING_SYSTEM == "darwin":
    # MAC OS
    print("\nOS:\t", "Mac OS\n")

elif OPERATING_SYSTEM == "win64":
    # Windows 64-bit
    print("\nOS:\t", "Windows\n")


def get_current_ssid() -> str:
    # get SSID from Terminal
    ssid_command = "/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport" \
                   " -I | awk -F: '/ SSID/{print $2}'"
    ssid = subprocess.check_output(ssid_command, shell=True)

    # Clean up SSID
    ssid = str(ssid).replace("b' ", "")
    ssid = ssid.replace("\\n'", "")
    print(f"SSID: {ssid}")

    return ssid


def get_current_password(ssid) -> str:
    # get password for the current SSID from Terminal
    password_command = f"security find-generic-password -wa {ssid}"
    password = subprocess.check_output(password_command, shell=True)

    # Clean up password
    password = str(password).replace("b'", "")
    password = password.replace("\\n'", "")
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
    try:
        ssid = get_current_ssid()
        password = get_current_password(ssid)

        wifi_text = create_wifi_text(ssid, password)
        # TODO: maybe optional strings

    except:
        print("No wifi connection")

    wifi_tuple = (ssid, password, wifi_text)
    return wifi_tuple

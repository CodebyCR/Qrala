import wifi_qrcode_generator as qr
import os

import subprocess
from sys import platform as _platform


def get_networks():
    scan_cmd = subprocess.Popen(
        ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport', '-s'],    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    scan_out, scan_err = scan_cmd.communicate()
    scan_out_data = []
    scan_out_lines = str(scan_out).split("\\n")[1:-1]

    for each_line in scan_out_lines:
        split_line = [e for e in each_line.split(" ") if e != ""]
        scan_out_data.append(split_line)

    return scan_out_data


def get_wifi_info():
    process = subprocess.Popen(
        ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()

    wifi_info = {}
    for line in out.decode("utf-8").split("\n"):
        if ": " in line:
            key, val = line.split(": ")
            key = key.replace(" ", "")
            val = val.strip()

            wifi_info[key] = val

    return wifi_info


def get_current_network():
    process = subprocess.Popen(
        ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()

    for line in out.decode("utf-8").split("\n"):
        if ": " in line:
            key, val = line.split(": ")
            key = key.replace(" ", "")
            val = val.strip()

            if key == "SSID":
                return val


def getRootPath():
    if _platform == "darwin":
        return os.getcwd()
    elif _platform == "win64":
        return os.path.dirname(os.getcwd())


def getOS():
    if _platform == "darwin":
        return "Mac OS"
    elif _platform == "win64":
        return "Windows"


# working on mac

# Import module

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

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

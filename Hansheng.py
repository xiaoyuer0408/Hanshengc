import sys
import subprocess
import platform
import webbrowser
import shutil
import os
import time
from mitmproxy import ctx, http

PROXY_ADDRESS = "127.0.0.1:8080"
URL_TO_OPEN = "https://t.me/Rsmyhtl"
CREATOR_NAME = "========================   Tg:@Rsmyhtl  ========================"
CREATOR_LINK = "@Rsmyhtl"

def set_system_proxy():
    proxy_settings = [
        ("ProxyServer", PROXY_ADDRESS),
        ("ProxyEnable", "1"),
    ]
    for setting, value in proxy_settings:
        subprocess.run(
            [
                "reg",
                "add",
                r"HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings",
                "/v",
                setting,
                "/d",
                value,
                "/f",
            ],
            capture_output=True,
        )

def unset_system_proxy():
    proxy_settings = ["ProxyServer", "ProxyEnable"]
    for setting in proxy_settings:
        subprocess.run(
            [
                "reg",
                "delete",
                r"HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings",
                "/v",
                setting,
                "/f",
            ],
            capture_output=True,
        )

def request(flow: http.HTTPFlow) -> None:
    if "evlfdev.com/canyouseeme.php" in flow.request.pretty_url:
        flow.request.host = "jiazaiqi.000webhostapp.com"
        flow.request.path = "/canyouseeme.php"
    elif "evlfdev.com/check.php" in flow.request.pretty_url:
        flow.request.method = "GET"
        flow.request.host = "jiazaiqi.000webhostapp.com"
        flow.request.path = "/check.php"
        ctx.log.info(" You are successfully logged in.")
        ctx.log.info("Press CTRL+C to close the loader.")

def print_centered_message(message):
    terminal_width = shutil.get_terminal_size().columns
    padding = max((terminal_width - len(message)) // 2, 0)
    print(f"{' ' * padding}{message}{' ' * padding}")

def main():
    set_system_proxy()

    print_centered_message("PHP server by @Rsmyhtl")
    print_centered_message(f"By: {CREATOR_NAME} - {CREATOR_LINK}")

    print(" _____   _   _   _  __    __  _   _   _____ ")
    print("/  ___/ | | | | | | \\ \\  / / | | | | | ____|")
    print("| |___  | |_| | | |  \\ \\/ /  | | | | | |__   ")
    print("\\___  \\ |  _  | | |   \\  /   | | | | |  __| ")
    print(" ___| | | | | | | |   / /    | |_| | | |___ ")
    print("/_____/ |_| |_| |_|  /_/     \\_____/ |_____|")
    print(" Tg:@Rsmyhtl ")
    print("                                                                           ")
    print("                    For customization, please contact Tg:@Rsmyhtl!")

    devnull = open(os.devnull, 'w')
    command = ['mitmdump', '-s', __file__, '--no-anticache'] + sys.argv[1:]
    mitm_process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True
    )

    try:
        for line in mitm_process.stdout:
            if "🔒 Logged in Successfully 🔒 : Access Granted!" in line:
                print(line.strip())
            if "Wrap-up: CTRL+C to Finish..." in line:
                print(line.strip())

        mitm_process.wait()
        mitm_process.communicate()  # Wait for the mitmdump process to complete

    finally:
        mitm_process.terminate()
        time.sleep(1)

        unset_system_proxy()

        webbrowser.open(URL_TO_OPEN)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

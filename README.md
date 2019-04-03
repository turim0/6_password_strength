# Password complexity

Password complexity
Script takes password and gives it a rating from 1 to 10. 1 is a very weak password, 10 is very cool

The base of the most common passwords can be downloaded [here](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt)

# Example
``` bash
user:~$ python3 password_strength.py
Warning: use password blacklist file to check your password
Usage: python password_strength.py + path to your file
Password: (your password)
Password strength: 4
user:~$ python3 password_strength.py /home/blacklist.txt 
Password: (your password)
Password strength: 8

```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)


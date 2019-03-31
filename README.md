# Сложность пароля
Скрипт, который просит ввести пароль и выдаёт ему оценку от 1 до 10. 1 – очень слабый пароль, 10 – очень крутой

Базу самых встречающихся паролей можно скачать [здесь](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt)

# Пример
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
# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

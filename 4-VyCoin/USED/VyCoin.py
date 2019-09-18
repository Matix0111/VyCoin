import time
import configparser
import msvcrt as m
import win32api
from threading import Thread

store = None

def check():
    time.sleep(2)
    if store != None:
        return
    print("\nContinuing")

parser = configparser.ConfigParser()

print("-=-=-=-=-=- WELCOME! -=-=-=-=-=-")

user = input("Are you a new user? ")

if user == "No" or user == "no":
    login_username = input("Please enter your username: ")
    login_password = input("Please enter your password: ")

    with open('Accounts.txt') as f:
        account_make = f.readlines()
    for lines in account_make:
        if login_password and login_username in lines:
            print("Login Successful")
            time.sleep(1)
            game = input("New game(ng/NG) or continue(c/C)? ")

            if game == "ng" or game == "Ng" or game == "nG" or game == "NG":
                parser['VYCOINS'] = {
                    'VyCoins': '0',
                    'Balance': '0'
                }

                with open('./config.ini', 'w') as f:
                    parser.write(f)

                print("Config created!")

                time.sleep(1)

                parser.read('config.ini')
                parser.get('VYCOINS', 'vycoins')
                placeholder = int(parser.get('VYCOINS', 'vycoins'))
                while True:
                    time.sleep(2)
                    placeholder = placeholder + 1
                    parser.set('VYCOINS', 'vycoins', str(placeholder))
                    with open('config.ini', 'w') as configfile:
                        parser.write(configfile)
                    print('VyCoins: ' + str(placeholder))

            elif game == "c" or game == "C":
                parser.read('config.ini')
                parser.get('VYCOINS', 'vycoins')
                placeholder = int(parser.get('VYCOINS', 'vycoins'))
                while True:
                    placeholder = placeholder + 1
                    parser.set('VYCOINS', 'vycoins', str(placeholder))
                    with open('config.ini', 'w') as configfile:
                        parser.write(configfile)
                    print('VyCoins: ' + str(placeholder))
                    Thread(target = check).start()
                    store = input("Store? ")
                    if store == 'Yes' or store == 'yes':
                        choice = input("Convert ")
                        if choice == "convert" or choice == "Convert":
                            VyCoin_C = 8142
                            multiply = int(parser.get('VYCOINS', 'vycoins'))
                            print("Converting! ")
                            time.sleep(5)
                            result = VyCoin_C * multiply
                            parser.get('VYCOINS', 'balance')
                            parser.set('VYCOINS', 'balance', str(result))
                            parser.set('VYCOINS', 'vycoins', '0')
                            placeholder = 0
                            with open('config.ini', 'w') as configfile:
                                parser.write(configfile)
                            print("You've earned $" + str(result) + "!")

elif user == "Yes" or user == "yes":
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    password_check = input("Please re-enter your password: ")

    if password != password_check:
        print("Passwords do not match!")
    elif password == password_check:
        account_make = open('Accounts.txt', 'a')
        account_make.write('USER: ' + username + ' | PASS: ' + password)
        account_make.close()
        print("Account created successfully!")

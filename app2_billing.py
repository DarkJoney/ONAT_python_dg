import datetime
from random import randint
reg_acc = []
reg_data = {}
billing_data = []


def ac_rev(phonen):
    if "money" in reg_data[phonen]:
        print("Amount of avaliable money: " + str(reg_data[phonen]["money"]))
    else:
        print("The user didn't put any money on his account before")
    if "payam" in reg_data[phonen]:
        print("Latest payment was at " + str(reg_data[phonen]["data"]) + ", total num of payments: " + str(reg_data[phonen]["payam"]))
    else:
        print("The user didn't put any money on his account before")


def ac_rep(phonen):
    print("Data for: " + phonen)
    if "money" in reg_data[phonen]:
        print("Amount of avaliable money for calls " + str(reg_data[phonen]["money"]-4*reg_data[phonen]["numcall"]))


def call_data(phonen):
    print("Data for: " + phonen)
    if "reccall" in reg_data[phonen]:
        print("Last incoming call: " + str(reg_data[phonen]["reccall"]) + " at " + str(reg_data[phonen]["lastrecdata"]))
    else:
        print("no calls avaliable")
    if "lastcall" in reg_data[phonen]:
        print("Last outcoming  call: " + str(reg_data[phonen]["lastcall"]) + " at " + str(reg_data[phonen]["lastcalldata"]))
    else:
        print("no calls avaliable")

def sub_data(usr_num):
    print("Data for: " + usr_num)
    print(reg_data[usr_num])
    #for x in reg_data[usr_num].values:
    #       print(x)


def sub_reg():
    print("Input your phone number: ")
    phonen = input()
    if phonen not in reg_acc:
        reg_acc.append(phonen)
        print(phonen + " is added")
        print("Let's input an additional information. ")
        print("Input name:")
        name = input()
        print("Input surname:")
        surname = input()

        reg_data[phonen] = {
            "name": name,
            "surname": surname,
            "numcall": 0
        }
        print(reg_data[phonen]["name"] + " is registered  in system")
    else:
        print("He is already registered in the system")



def add_money(phonen):

    print("Enter amount of money:")
    money2add = int(input())
    if "money" in reg_data[phonen]:
        reg_data[phonen]["money"] = reg_data[phonen]["money"] + money2add
        reg_data[phonen]["data"] = datetime.datetime.now()

        reg_data[phonen]["payam"] = reg_data[phonen]["payam"] + 1
    else:
        reg_data[phonen]["money"] = money2add
        reg_data[phonen]["payam"] = 1
        reg_data[phonen]["data"] = datetime.datetime.now()


def make_call(phonen):
    reg_data[phonen]["numcall"] = int(reg_data[phonen]["numcall"]) + int(1)
    number = "0" + str(randint(630000000, 990000000))
    reg_data[phonen]["lastcall"] = number
    reg_data[phonen]["lastcalldata"] = datetime.datetime.now()
    print(phonen + " makes call to " + number)


def rec_call(phonen):

    number = "0" + str(randint(630000000, 990000000))
    reg_data[phonen]["reccall"] = number
    reg_data[phonen]["lastrecdata"] = datetime.datetime.now()
    print(phonen + " gets call from " + number)

while True:
    print("WELCOME TO SUBSCRIBER BILLING SYSTEM! What you would like to do?")
    print("Main Functions:")
    print("1 - subscriber registration")
    print("2 - view subscriber data")
    print("3 - account review")
    print("4 - view data on calls")
    print("5 - account replenishment")
    print("Additional Functions:")
    print("7 - add money to debit")
    print("8 - make a call")
    print("9 - receive call")
    userInput = input()
    if userInput is str("1"):
        sub_reg()
    elif userInput is str("2"):
        print("Enter phone number: ")
        num = input()
        sub_data(num)
    elif userInput is str("3"):
        print("Enter phone number: ")
        num = input()
        ac_rev(num)
    elif userInput is str("4"):
        print("Enter phone number: ")
        num = input()
        call_data(num)
    elif userInput is str("5"):
        print("Enter phone number: ")
        num = input()
        ac_rep(num)

    elif userInput is str("7"):
        print("Enter phone number: ")
        num = input()
        add_money(num)
    elif userInput is str("8"):
        print("Enter phone number: ")
        num = input()
        make_call(num)
    elif userInput is str("9"):
        print("Enter phone number: ")
        num = input()
        rec_call(num)





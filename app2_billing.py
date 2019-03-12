import datetime
from random import randint
reg_acc = []
reg_data = {}
billing_data = []


def acc_stat():
    pass

def data_calls():
    pass

def ac_rev(phonen):
    if "money" in reg_data[phonen]:



def ac_rep():
    pass


def call_data():
    pass


def sub_data(usr_num):
    print("Data for: " + usr_num)
    print(reg_data[usr_num])
    #for x in reg_data[usr_num].values:
    #       print(x)


def sub_reg():
    print("Input your phone number: ")
    phonen = input()
    reg_acc.append(phonen)
    print(phonen + "is added")
    print("Let's input an additional information. ")
    print("Input name:")
    name = input()
    print("Input surname:")
    surname = input()

    reg_data[phonen] = {
        "name": name,
        "surname": surname
    }
    print(reg_data[phonen]["name"] + " is registered  in system")


def add_money(phonen):

    print("Enter amount of money:")
    money2add = int(input())
    if "money" in reg_data[phonen]:
        reg_data[phonen]["money"] = reg_data[phonen["money"]] + money2add
        reg_data[phonen]["data"] = datetime.datetime.now()
        if "payAM" in reg_data[phonen]:
            reg_data[phonen]["payam"] = reg_data[phonen["payam"]] + 1
    else:
        reg_data[phonen]["money"] = money2add
        reg_data[phonen]["payam"] = 1
        reg_data[phonen]["data"] = datetime.datetime.now()


def make_call(phonen):

    number = "0" + str(randint(630000000, 990000000))
    reg_data[phonen]["lastcall"] = number
    print(reg_data[phonen]+" makes call to " + number)

def rec_call(phonen):

    number = "0" + str(randint(630000000, 990000000))
    reg_data[phonen]["reccall"] = number
    print(reg_data[phonen] + " gets call from " + number)

while True:
    print("WELCOME TO SUBSCRIBER BILLING SYSTEM! What you would like to do?")
    print("Main Functions:")
    print("1 - subscriber registration")
    print("2 - view subscriber data")
    print("3 - account review")
    print("4 - view data on calls")
    print("5 - account replenishment")
    print("6 - status of the account")
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
        call_data()
    elif userInput is str("5"):
        ac_rep()
    elif userInput is str("6"):
        acc_stat()
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





"""it is the subscriber account system """
MTS = {}
list_number = ["0956500044", "095226288", "0952425399", "0956435699", "0666419388"]


def create_account(dict_abonents, phonenumber, name, surname, amountofmoney=0):
    """create account for new abonent"""
    # print("function is create_account")
    # print(phonenumber,name,surname)
    dict_abonents[phonenumber] = {
        "name": name,
        "surname": surname
    }


def put_money_score(a=0):
    pass


def print_info(dict_abonents, phone_number):
    print(dict_abonents[phone_number]["name"])


def call(phone_number):
    pass


def print_phone_numbers(list_phones):
    i = 0
    for number in list_phones:
        i += 1
        print("{} - +38{}".format(i, number))


if __name__ == "__main__":
    print("please choose phone number")
    print_phone_numbers(list_number)

    i_number = int(input())

    if i_number > 0 and i_number <= len(list_number):
        print("OK!,thanks for our answer,please enter your name")
        name = input("please enter your name: ")
        surname = input("please enter your surname: ")
        create_account(MTS, list_number[i_number - 1], name, surname)
        print_info(MTS, list_number[i_number - 1])



    else:
        print("sorry,number is not correct")




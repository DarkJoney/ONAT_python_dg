import random

person_counter = 0
current_person = 0
user_mode_input = ""
is_waiting = True
is_testing = False
person_list = []
correct_answers = []
vopros_num = 0
wrong_answer = []
while True:

    admin_name = "Vorobienko Petr Petrovich"
    while is_waiting is True:
        print("Hello, " + admin_name)
        print("Please register person for testing: ")
        person_list.append(input())
        #append drugie soprovojdenie
        print(person_list[person_counter] + " is registered")

        is_waiting = False
        is_testing = True

    while is_testing is True:

        a = random.randint(1, 10)
        b = random.randint(1, 10)
        testVal = random.randint(1, 4)
        signs = ["*","/","+","-"]

        print("What's the result of" + " " + str(a) + signs[testVal] + str(b) + "?")
        userOtvet = input()
        vopros_num = vopros_num +1
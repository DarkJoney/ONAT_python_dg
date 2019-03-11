import random

person_counter = 0
current_person = 0
user_mode_input = ""
is_waiting = True
is_testing = False
is_results = False
person_list = []
correct_answers = []
ratios_list = []
ca_counter = 0
wa_counter = 0
vopros_num = 1
wrong_answer = []


def runTest():
    global vopros_num
    global ca_counter
    global wa_counter
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    testVal = random.randint(0, 3)
    signs = ["*", "/", "+", "-"]

    if vopros_num <= 3:
        print("Task #" + str(vopros_num) + " from 4")
        print("What's the result of" + " " + str(a) + signs[testVal] + str(b) + "?")
        taskResult = eval(str(a) + signs[testVal] + str(b))
        userOtvet = input()
        if userOtvet == str(taskResult):
            print("Correct!")
            ca_counter = ca_counter + 1
        else:
            print("Wrong!")
            wa_counter = wa_counter + 1
        vopros_num = vopros_num + 1

    if vopros_num == 4:
        correct_answers.append(ca_counter)
        wrong_answer.append(wa_counter)
        print("Correct answers: " + str(ca_counter))
        print("Wrong answers: " + str(wa_counter))

        print("Do you want to continue? Y/N")


while True:
    name = input()
    while is_waiting is True:
        quest_num = 0
        ca_counter = 0
        wa_counter = 0
        print("Hello, " + name)


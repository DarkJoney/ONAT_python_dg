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
ques_num = 1
wrong_answer = []


def calc_ratio():
    for x in range(len(person_list)):
        ratios_list.append((correct_answers[x]/4)*100)


def print_res():
    print("#    NAME    C/W             ratio")

    list_marker = 1
    for out, out1 in zip(person_list, zip(correct_answers, wrong_answer)):
        print(list_marker, '\t', out, '\t', out1, '\t', '\t', ratios_list[list_marker-1])
        list_marker = list_marker + 1
    temp_largest = 0
    for x in range(len(correct_answers)):
        if correct_answers[x] >= correct_answers[x - 1]:
            temp_largest = x
    print("Best scored person is: " + str(person_list[temp_largest]) + " with score:" + str(correct_answers[temp_largest]))


admin_name = "Vorobienko Petr Petrovich"
print("Hello, " + admin_name)
while True:


    while is_waiting is True:
        ques_num = 0
        ca_counter = 0
        wa_counter = 0
        print("Please register person for testing: ")
        name = input()
        if name not in person_list:
            person_list.append(name)
        else:
            print("He is already in the list")
            break

        print(person_counter)
        print(person_list[person_counter] + " is registered")
        is_results = False
        is_waiting = False
        is_testing = True

    while is_testing is True:

        a = random.randint(1, 10)
        b = random.randint(1, 10)
        testVal = random.randint(0, 3)
        signs = ["*", "/", "+", "-"]

        if ques_num <= 3:
            print("Task #" + str(ques_num) + " from 4")
            print("What's the result of" + " " + str(a) + signs[testVal] + str(b) + "?")
            taskResult = eval(str(a) + signs[testVal] + str(b))
            userInput = input()
            if userInput == str(taskResult):
                print("Correct!")
                ca_counter = ca_counter + 1
            else:
                print("Wrong!")
                wa_counter = wa_counter + 1
            ques_num = ques_num + 1

        if ques_num == 4:
            correct_answers.append(ca_counter)
            wrong_answer.append(wa_counter)
            print("Correct answers: " + str(ca_counter))
            print("Wrong answers: " + str(wa_counter))

            print("Do you want to continue? Y/N")
            inputcheck = input()
            if inputcheck == str("Y"):
                is_testing = False
                is_waiting = True
                is_results = False
                current_person = current_person + 1
                person_counter = person_counter + 1
            elif inputcheck == str("N"):
                is_testing = False
                is_waiting = False
                is_results = True

            # else:
            # is_testing = False
            # is_waiting = False
            #  is_results = True
            #  current_person = current_person + 1
            #  person_counter = person_counter + 1
            #  print("Press Enter to view results")

        if is_results is True:
            calc_ratio()
            print_res()


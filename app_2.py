import random

person_counter = 0
current_person = 0
user_mode_input = ""
is_waiting = True
is_testing = False
is_results = False
person_list = []
correct_answers = []
ca_counter = 0
wa_counter = 0
vopros_num = 1
wrong_answer = []
while True:

    admin_name = "Vorobienko Petr Petrovich"
    while is_waiting is True:
        print("Hello, " + admin_name)

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
        signs = ["*","/","+","-"]

        if vopros_num <= 3:
            print("Task #" + str(vopros_num) + " from 4")
            print("What's the result of" + " " + str(a) + signs[testVal] + str(b) + "?")
            taskResult = eval(str(a) +  signs[testVal] + str(b))
            userOtvet = input()
            if userOtvet == str(taskResult):
                print("pizdato")
                ca_counter = ca_counter+1
            else:
                print ("pizdec")
                wa_counter = wa_counter+1
            vopros_num = vopros_num +1

        if vopros_num == 4:
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

            #else:
               # is_testing = False
               # is_waiting = False
              #  is_results = True
              #  current_person = current_person + 1
              #  person_counter = person_counter + 1
              #  print("Press Enter to view results")

        if is_results is True:
            print("debug")
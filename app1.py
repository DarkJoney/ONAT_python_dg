import random

persons = []
correct = []
wrong = []
isTest = True


def show_results():
    print("*********************************************")
    print("Results of " + str(len(persons)) + " person")
    print("Name" + '\t' + "Correct and wrong")
    for data1, data2 in zip(persons, zip(correct, wrong)):
        print(data1, '\t', data2)


def test(test):
    while True and test is True:
        vopros_num = 1
        ca_counter = 0
        wa_counter = 0
        isTesting = False
        print("Enter your name:")
        user_name =  input()
        if user_name not in persons:
            persons.append(user_name)
        else:
            print("Already registered")
            break
        isTesting = True

        while isTesting is True:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            test = random.randint(0, 3)
            signs = ["*", "/", "+", "-"]
            if vopros_num <= 4:
                print("Task #" + str(vopros_num) + " from 4")
                print("What's the result of" + " " + str(a) + signs[test] + str(b) + "?")
                taskResult = eval(str(a) + signs[test] + str(b))
                userOtvet = input()
                if userOtvet == str(taskResult):
                    print("Correct!")
                    ca_counter = ca_counter + 1
                else:
                    print("Wrong!")
                    wa_counter = wa_counter + 1
                vopros_num = vopros_num + 1
            if vopros_num >= 5:
                wrong.append(wa_counter)
                correct.append(ca_counter)

                print("Finish!")

                isTest = False
                show_results()
                break


while True:
    print("")
    print("Session started")
    if isTest is True:
        test(isTest)



def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input()) #5
    total = 0
    while total!=num:
        print(total, '!')
        total  += 1


def test():
    print("Let's test your programming knowledge")
    print("Why do we use methods?")
    print("1.To repeat a statement multiple times")
    print("2.Todecompose a program into several small subroutimes")
    print("3.To determine the execution time of a program")
    print("4.To interrupt the execution of a program")
    q = int(input())
    while q!=2:
        print("Plase,try again")
        q = int(input())
    else:
        print("Completed, have a nice day")


def end():
    print('Congratulations, have a nice day!')


greet('DODO', '2021')
remind_name()
guess_age()
count()
test()
end()
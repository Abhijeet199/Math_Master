import msvcrt
import os
import random
import time
import termcolor
import textwrap

title = termcolor.colored('-*/+' * 7, 'yellow') \
        + termcolor.colored(' Math master ') \
        + termcolor.colored('+\*-' * 7, 'yellow')


def menu():
    os.system('cls')
    global p, wrong_attempt
    p = wrong_attempt = 0
    print(title)
    print('\n1> Easy')
    print('2> Medium')
    print('3> Hard')
    print('4> Exit')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
        clear_and_print_title('Easy')
        ask_for_continue(30)
        easy()
    elif choice == 2:
        clear_and_print_title('Medium')
        ask_for_continue(27)
        medium()
    elif choice == 3:
        clear_and_print_title('Hard')
        ask_for_continue(25)
        hard()
    elif choice == 4:
        exit(0)
    else:
        print('Invalid Choice')
        time.sleep(2)
        menu()


def clear_and_print_title(level):
    os.system('cls')
    print(title)
    print('\n{} Challenges are loading...'.format(level))
    time.sleep(2)
    os.system('cls')
    print(title, '\n')


def ask_for_continue(q):
    note = 'Note: In this challenge, there are {} questions and the difficulty of challenge will increases ' \
           'gradually. A wrong attempt counter will count your wrong attempts if you attempt 3 ' \
           'wrong attempts, then your game will over so be careful.'.format(q)
    wrapper = textwrap.TextWrapper(width=68)
    word_list = wrapper.wrap(text=note)
    for element in word_list:
        print(element)
    print('\n\nPress any key to continue...')
    flush_input()
    msvcrt.getch()


def easy():
    for i in range(1, 32):
        os.system('cls')
        print(title)
        val1, val2, op = return_values_and_operators_and_set_level_for_easy(i)
        result = '{:.2f}'.format(eval('{} {} {}'.format(val1, op, val2)))
        if i > 12:
            op = change_multiplication_symbol('Easy', op)
        val1, val2 = set_bracket_on_negative_values('Easy', val1, val2)
        print('\nSolve this: {} {} {} = ?'.format(val1, op, val2))
        get_and_check_ans(result)
        option()


def medium():
    for i in range(1, 29):
        os.system('cls')
        print(title)
        val1, val2, val3, op1, op2 = return_values_and_operators_and_set_level_for_medium(i)
        result = '{:.2f}'.format(eval('{} {} {} {} {}'.format(val1, op1, val2, op2, val3)))
        if i > 10:
            op1, op2 = change_multiplication_symbol('Medium', op1, op2)
        val1, val2, val3 = set_bracket_on_negative_values('Medium', val1, val2, val3)
        print('\nSolve this: {} {} {} {} {} = ?'.format(val1, op1, val2, op2, val3))
        get_and_check_ans(result)
        option()


def hard():
    for i in range(1, 27):
        os.system('cls')
        print(title)
        val1, val2, val3, val4, op1, op2, op3 = return_values_and_operators_and_set_level_for_hard(i)
        val1, val2, val3, val4 = set_bracket_on_negative_values('Hard', val1, val2, val3, val4)
        choice = random.randint(1, 3)
        print('\nSolve this: ', end='')
        if choice == 1:
            result = choice1(val1, op1, val2, op2, val3, op3, val4)
        elif choice == 2:
            result = choice2(val1, op1, val2, op2, val3, op3, val4)
        else:
            result = choice3(val1, op1, val2, op2, val3, op3, val4)
        get_and_check_ans(result)
        option()


def choice1(val1, op1, val2, op2, val3, op3, val4):
    choice = random.randint(1, 4)
    if choice == 1:
        if op2 != '*':
            result = '{:.2f}'.format(eval('({} {} {}) {} {} {} {}'.format(val1, op1, val2, op2, val3, op3, val4)))
            op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
            print('( {} {} {} ) {} {} {} {}'.format(val1, op1, val2, op2, val3, op3, val4))
            return result
        else:
            choice = random.randint(1, 2)
            if choice == 1:
                result = '{:.2f}'.format(eval('({} {} {}) {} {} {} {}'.format(val1, op1, val2, op2, val3, op3, val4)))
                op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
                print('( {} {} {} ) {} {} {} {}'.format(val1, op1, val2, op2, val3, op3, val4))
                return result
            else:
                result = '{:.2f}'.format(eval('(({} {} {}) {} {}) {} {}'.format(val1, op1, val2, op2, val3, op3, val4)))
                op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
                print('( {} {} {} ) {} {} {}'.format(val1, op1, val2, val3, op3, val4))
                return result
    elif choice == 2:
        if op1 != '*' and op3 != '*':
            result = '{:.2f}'.format(eval('{} {} ({} {} {}) {} {}'.format(val1, op1, val2, op2, val3, op3, val4)))
            op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
            print('{} {} ( {} {} {} ) {} {}'.format(val1, op1, val2, op2, val3, op3, val4))
            return result
        else:
            if op1 == '*' and op3 == '*':
                choice = random.randint(1, 4)
                if choice == 1:
                    result = '{:.2f}'.format(eval('{} {} ({} {} {}) {} {}'.format(val1, op1, val2, op2, val3, op3,
                                                                                  val4)))
                    op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
                    print('{} {} ( {} {} {} ) {} {}'.format(val1, op1, val2, op2, val3, op3, val4))
                    return result
                elif choice == 2:
                    result = '{:.2f}'.format(eval('({} {} ({} {} {}) {} {})'.format(val1, op1, val2, op2, val3, op3,
                                                                                    val4)))
                    op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
                    print('{} ( {} {} {} ) {}'.format(val1, val2, op2, val3, val4))
                    return result
                elif choice == 3:
                    result = '{:.2f}'.format(eval('({} {} ({} {} {})) {} {}'.format(val1, op1, val2, op2, val3, op3,
                                                                                    val4)))
                    op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
                    print('{} ( {} {} {} ) {} {}'.format(val1, val2, op2, val3, op3, val4))
                    return result
                else:
                    result = '{:.2f}'.format(eval('{} {} (({} {} {}) {} {})'.format(val1, op1, val2, op2, val3, op3,
                                                                                    val4)))
                    op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
                    print('{} {} ( {} {} {} ){}'.format(val1, op1, val2, op2, val3, val4))
                    return result
    elif choice == 3:
        if op2 != '*':
            result = '{:.2f}'.format(eval('{} {} {} {} ({} {} {})'.format(val1, op1, val2, op2, val3, op3, val4)))
            op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
            print('{} {} {} {} ( {} {} {} )'.format(val1, op1, val2, op2, val3, op3, val4))
            return result
        else:
            choice = random.randint(1, 2)
            if choice == 1:
                result = '{:.2f}'.format(eval('{} {} {} {} ({} {} {})'.format(val1, op1, val2, op2, val3, op3, val4)))
                op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
                print('{} {} {} {} ( {} {} {} )'.format(val1, op1, val2, op2, val3, op3, val4))
                return result
            else:
                result = '{:.2f}'.format(eval('{} {} ({} {} ({} {} {}))'.format(val1, op1, val2, op2, val3, op3, val4)))
                op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
                print('{} {} {} ( {} {} {} )'.format(val1, op1, val2, val3, op3, val4))
                return result
    else:
        if op2 != '*':
            result = '{:.2f}'.format(eval('({} {} {}) {} ({} {} {})'.format(val1, op1, val2, op2, val3, op3, val4)))
            op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
            print('( {} {} {} ) {} ( {} {} {} )'.format(val1, op1, val2, op2, val3, op3, val4))
            return result
        else:
            choice = random.randint(1, 2)
            if choice == 1:
                result = '{:.2f}'.format(eval('({} {} {}) {} ({} {} {})'.format(val1, op1, val2, op2, val3, op3, val4)))
                op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
                print('( {} {} {} ) {} ( {} {} {} )'.format(val1, op1, val2, op2, val3, op3, val4))
                return result
            else:
                result = '{:.2f}'.format(eval('({} {} {}) {} ({} {} {})'.format(val1, op1, val2, op2, val3, op3, val4)))
                op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
                print('( {} {} {} ) ( {} {} {} )'.format(val1, op1, val2, op2, val3, op3, val4))
                return result


def choice2(val1, op1, val2, op2, val3, op3, val4):
    choice = random.randint(1, 3)
    if choice == 1:
        result = '{:.2f}'.format(eval('(({} {} {}) {} {}) {} {}'.format(val1, op1, val2, op2, val3, op3, val4)))
        op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
        print('{ ' + '( {} {} {} ) {} {}'.format(val1, op1, val2, op2, val3) + ' } ' + '{} {}'.format(op3, val4))
    elif choice == 2:
        result = '{:.2f}'.format(eval('({} {} ({} {} {})) {} {}'.format(val1, op1, val2, op2, val3, op3, val4)))
        op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
        print('{ ' + '{} {} ( {} {} {} )'.format(val1, op1, val2, op2, val3) + ' } ' + '{} {}'.format(op3, val4))
    else:
        result = '{:.2f}'.format(eval('({} {} {} {} {}) {} {}'.format(val1, op1, val2, op2, val3, op3, val4)))
        op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
        print('( {} {} {} {} {} ) {} {}'.format(val1, op1, val2, op2, val3, op3, val4))
    return result


def choice3(val1, op1, val2, op2, val3, op3, val4):
    choice = random.randint(1, 3)
    if choice == 1:
        result = '{:.2f}'.format(eval('{} {} (({} {} {}) {} {})'.format(val1, op1, val2, op2, val3, op3, val4)))
        op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
        print('{} {}'.format(val1, op1) + ' { ' + '( {} {} {} ) {} {}'.format(val2, op2, val3, op3, val4) + ' }')
    elif choice == 2:
        result = '{:.2f}'.format(eval('{} {} {} {} ({} {} {})'.format(val1, op1, val2, op2, val3, op3, val4)))
        op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
        print('{} {}'.format(val1, op1) + ' { ' + '{} {} ( {} {} {} )'.format(val2, op2, val3, op3, val4) + ' }')
    else:
        result = '{:.2f}'.format(eval('{} {} ({} {} {} {} {})'.format(val1, op1, val2, op2, val3, op3, val4)))
        op1, op2, op3 = change_multiplication_symbol('Hard', op1, op2, op3)
        print('{} {} ( {} {} {} {} {} )'.format(val1, op1, val2, op2, val3, op3, val4))
    return result


def return_values_and_operators_and_set_level_for_easy(j):
    if j <= 4:
        print('\n                           Question: {:=02d}/30'.format(j))
        val1, val2 = (random.randint(-20, -1) if random.randint(1, 4) == 1 else random.randint(0, 20) for _ in range(2))
        op = '+'
        return val1, val2, op
    elif j <= 8:
        print('\n                           Question: {:=02d}/30'.format(j))
        val1 = random.randint(-20, -1) if random.randint(1, 4) == 1 else random.randint(0, 20)
        val2 = random.randint(-10, -1) if random.randint(1, 4) == 1 else random.randint(0, 10)
        op = '-'
        val1, val2 = randomly_exchange_values(val1, val2)
        return val1, val2, op
    elif j <= 12:
        print('\n                           Question: {:=02d}/30'.format(j))
        val1, val2 = (random.randint(-25, -6) if random.randint(1, 3) == 1 else random.randint(6, 25) for _ in range(2))
        op = operator(['+', '-'])
        return val1, val2, op
    elif j <= 16:
        print('\n                           Question: {:=02d}/30'.format(j))
        val1 = random.randint(-20, -1) if random.randint(1, 4) == 1 else random.randint(0, 20)
        val2 = random.randint(-10, -1) if random.randint(1, 4) == 1 else random.randint(0, 10)
        op = '*'
        val1, val2 = randomly_exchange_values(val1, val2)
        return val1, val2, op
    elif j <= 20:
        print('\n                           Question: {:=02d}/30'.format(j))
        val1 = random.randint(0, 20)
        val2 = random.randint(0, 10)
        op = '/'
        return val1, val2, op
    elif j <= 24:
        print('\n                           Question: {:=02d}/30'.format(j))
        val1, val2 = (random.randint(-25, -6) if random.randint(1, 3) == 1 else random.randint(6, 25) for _ in range(2))
        op = operator(['*', '/'])
        return val1, val2, op
    elif j <= 30:
        print('\n                           Question: {:=02d}/30'.format(j))
        val1, val2 = (random.randint(-30, -6) if random.randint(1, 2) == 1 else random.randint(6, 30) for _ in range(2))
        op = operator(['*', '/', '-', '+'])
        return val1, val2, op
    else:
        finish_challenge('Easy')


def return_values_and_operators_and_set_level_for_medium(j):
    if j <= 5:
        print('\n                           Question: {:=02d}/27'.format(j))
        val1, val2, val3 = (random.randint(-20, -1) if random.randint(1, 3) == 1 else random.randint(0, 20) for _ in
                            range(3))
        op1, op2 = '+', '+'
        return val1, val2, val3, op1, op2
    elif p <= 10:
        print('\n                           Question: {:=02d}/27'.format(j))
        val1, val2, val3 = (random.randint(-25, -6) if random.randint(1, 3) == 1 else random.randint(6, 25) for _ in
                            range(3))
        op1, op2 = (operator(['+', '-']) for _ in range(2))
        return val1, val2, val3, op1, op2
    elif j <= 15:
        print('\n                           Question: {:=02d}/27'.format(j))
        val1, val2, val3 = (random.randint(-30, -10) if random.randint(1, 3) == 1 else random.randint(10, 30) for _ in
                            range(3))
        op1, op2 = (operator(['+', '-', '*']) for _ in range(2))
        return val1, val2, val3, op1, op2
    elif j <= 20:
        print('\n                           Question: {:=02d}/27'.format(j))
        val1, val2, val3 = (random.randint(-35, -15) if random.randint(1, 3) == 1 else random.randint(15, 35) for _ in
                            range(3))
        op1, op2 = (operator(['+', '-', '*', '/']) for _ in range(2))
        return val1, val2, val3, op1, op2
    elif j <= 27:
        print('\n                           Question: {:=02d}/27'.format(j))
        val1, val2, val3 = (random.randint(-50, -20) if random.randint(1, 2) == 1 else random.randint(20, 50) for _ in
                            range(3))
        op1, op2 = (operator(['+', '-', '*', '/']) for _ in range(2))
        return val1, val2, val3, op1, op2
    else:
        finish_challenge('Medium')


def return_values_and_operators_and_set_level_for_hard(j):
    if j <= 5:
        print('\n                           Question: {:=02d}/25'.format(j))
        val1, val2, val3, val4 = (random.randint(-20, -1) if random.randint(1, 2) == 1 else random.randint(0, 20)
                                  for _ in range(4))
        op1, op2, op3 = (operator(['+', '-', '*', '/']) for _ in range(3))
        return val1, val2, val3, val4, op1, op2, op3
    elif p <= 10:
        print('\n                           Question: {:=02d}/25'.format(j))
        val1, val2, val3, val4 = (random.randint(-40, -1) if random.randint(1, 2) == 1 else random.randint(0, 40)
                                  for _ in range(4))
        op1, op2, op3 = (operator(['+', '-', '*', '/']) for _ in range(3))
        return val1, val2, val3, val4, op1, op2, op3
    elif j <= 15:
        print('\n                           Question: {:=02d}/25'.format(j))
        val1, val2, val3, val4 = (random.randint(-60, -20) if random.randint(1, 2) == 1 else random.randint(20, 60)
                                  for _ in range(4))
        op1, op2, op3 = (operator(['+', '-', '*', '/']) for _ in range(3))
        return val1, val2, val3, val4, op1, op2, op3
    elif j <= 20:
        print('\n                           Question: {:=02d}/25'.format(j))
        val1, val2, val3, val4 = (random.randint(-80, -40) if random.randint(1, 2) == 1 else random.randint(40, 80)
                                  for _ in range(4))
        op1, op2, op3 = (operator(['+', '-', '*', '/']) for _ in range(3))
        return val1, val2, val3, val4, op1, op2, op3
    elif j <= 25:
        print('\n                           Question: {:=02d}/25'.format(j))
        val1, val2, val3, val4 = (random.randint(-100, -50) if random.randint(1, 2) == 1 else random.randint(50, 100)
                                  for _ in range(4))
        op1, op2, op3 = (operator(['+', '-', '*', '/']) for _ in range(3))
        return val1, val2, val3, val4, op1, op2, op3
    else:
        finish_challenge('Hard')


def operator(opr):
    op = random.choice(opr)
    return op


def randomly_exchange_values(val1, val2):
    ch = random.randint(0, 1)
    if ch == 1:
        return val1, val2
    return val2, val1


def change_multiplication_symbol(level, op1, op2='', op3=''):
    if level == 'Easy':
        if op1 == '*':
            op1 = 'x'
        return op1

    if level == 'Medium':
        if op1 == '*':
            op1 = 'x'
        if op2 == '*':
            op2 = 'x'
        return op1, op2

    if level == 'Hard':
        if op1 == '*':
            op1 = 'x'
        if op2 == '*':
            op2 = 'x'
        if op3 == '*':
            op3 = 'x'
        return op1, op2, op3


def set_bracket_on_negative_values(level, val1, val2, val3=0, val4=0):
    if level == 'Easy':
        if val1 < 0:
            val1 = '({})'.format(val1)
        if val2 < 0:
            val2 = '({})'.format(val2)
        return val1, val2

    if level == 'Medium':
        if val1 < 0:
            val1 = '({})'.format(val1)
        if val2 < 0:
            val2 = '({})'.format(val2)
        if val3 < 0:
            val3 = '({})'.format(val3)
        return val1, val2, val3

    if level == 'Hard':
        if val1 < 0:
            val1 = '({})'.format(val1)
        if val2 < 0:
            val2 = '({})'.format(val2)
        if val3 < 0:
            val3 = '({})'.format(val3)
        if val4 < 0:
            val4 = '({})'.format(val4)
        return val1, val2, val3, val4


def get_and_check_ans(result_):
    global p, wrong_attempt
    ans = float('{:.2f}'.format(eval(input('\nEnter you answer: '))))
    result_ = float(result_)
    if result_ == ans:
        print(termcolor.colored('\nCongrats! you are right.', 'green'))
        print('\nPoint: {}'.format(p) + termcolor.colored(' + 10', 'green') + ' -> ', end='')
        p += 10
        print(p)
    else:
        wrong_attempt += 1
        print(termcolor.colored("\nWrong answer!", 'red'))
        print("right answer is {}".format(result_))
        check_wrong_attempt(wrong_attempt, 3)
        if p > 0:
            print('\nPoint: {}'.format(p) + termcolor.colored(' - 5', 'red') + ' -> ', end='')
            p -= 5
            print(p)
        else:
            print('Point: {:=03d}'.format(p))
    wrong_att(wrong_attempt)


def wrong_att(wrong):
    color = ['green', 'yellow', 'red']
    if wrong != 2:
        termcolor.cprint('Wrong Attempts: {}/3'.format(wrong), color[wrong])
    else:
        termcolor.cprint('Wrong Attempts: {}/3'.format(wrong), color[wrong], attrs=['blink'])


def check_wrong_attempt(w_a, max_):
    global p
    if w_a == max_:
        if p > 0:
            p -= 5
        print(termcolor.colored('\n\n                              Game Over!', 'red'))
        termcolor.cprint('                          Wrong Attempts: {}/{}'.format(w_a, max_), 'red')
        print('                              Point: {:=03d}'.format(p))
        option_for_game_over_or_finishing_the_challenges()
    print("Don't feel bad! try again!")


def finish_challenge(challenge):
    os.system('cls')
    print(title)
    termcolor.cprint('\n\n       Congratulations! You have completed all {} challenges.'.format(challenge), 'green')
    print('                        ', end='')
    wrong_att(wrong_attempt)
    print('                            Point: {:=03d}'.format(p))
    option_for_game_over_or_finishing_the_challenges()


def option_for_game_over_or_finishing_the_challenges():
    time.sleep(4)
    print('\nPress any key to go to menu...')
    flush_input()
    msvcrt.getch()
    menu()


def option():
    flush_input()
    print()
    print("Press any key to continue or 'm' for menu...")
    pressed_key = msvcrt.getch()
    if ord(pressed_key) == 109:
        menu()


def flush_input():
    while msvcrt.kbhit():
        msvcrt.getch()


menu()

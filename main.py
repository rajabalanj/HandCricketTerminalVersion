import random


def ball(balls, wickets=0):
    com_total = 0
    print("you're going to bowl now")
    for i in range(0, balls):
        print(f"cpu : {com_total} - {wickets} \n overs : {i // 6}.{i % 6}")
        user = int(input("Enter number \n"))
        if 0 < user <= 6:
            print("You've chosed", user, "\n")
        else:
            print('Enter number from 1 to 6')
            balls -= 1
            continue
        computer = random.randint(1, 6)
        print("Computer chose", computer, "\n")
        if computer == user:
            print("out :-)")
            wickets += 1
            if wickets == balls/6 or wickets == 10:
                break
        else:
            com_total = com_total + computer
            print("computer's total is now", com_total)
    target = com_total + 1
    print("computer's score is:", com_total)
    print('target:', target)
    user_total = 0
    wickets = 0
    print("you're going to bat now")
    for i in range(0, balls):
        print(f"user : {user_total} - {wickets} \n overs : {i // 6}.{i % 6}")
        user = int(input("Enter number \n"))
        if 0 < user <= 6:
            print("You've inputed", user, "\n")
        else:
            print('Enter number from 1 to 6')
            balls -= 1
            continue
        computer = random.randint(1, 6)
        print("Computer chose", computer, "\n")
        if computer == user:
            print("out :-(")
            wickets += 1
            if wickets == balls/6 or wickets == 10:
                break
        else:
            user_total = user_total + user
            remaining = target - user_total
            print(f'you need {remaining} more runs to win in {balls - i -1} balls')
            print("your score is now:", user_total)
            if remaining <= 0:
                print('you won')
                break
    if com_total > user_total:
        print('computer won')
    elif user_total == com_total:
        print('tie')


def bat(balls, wickets=0):
    user_total = 0
    print("you're going to bat now")
    for i in range(0, balls):
        print(f"user : {user_total} - {wickets} \n overs : {i // 6}.{i % 6}")
        user = int(input("Enter number \n"))
        if 0 < user <= 6:
            print("You've inputed", user, "\n")
        else:
            print('Enter number from 1 to 6')
            balls -= 1
            continue
        computer = random.randint(1, 6)
        print("Computer chose", computer, "\n")
        if computer == user:
            print("out :-(")
            wickets += 1
            if wickets == balls/6 or wickets == 10:
                break
        else:
            user_total = user_total + user
            print("Your total is now", user_total)
    print("Your score is:", user_total)
    target = user_total + 1
    print('target:', target)
    com_total = 0
    wickets = 0
    print("you're going to bowl now")
    for i in range(0, balls):
        print(f"cpu : {com_total} - {wickets} \n overs : {i // 6}.{i % 6}")
        user = int(input("Enter number \n"))
        if 0 < user <= 6:
            print("You've inputed", user, "\n")
        else:
            print('Enter number from 1 to 6')
            balls -= 1
            continue
        computer = random.randint(1, 6)
        print("Computer chose", computer, "\n")
        if computer == user:
            print("out :-)")
            wickets += 1
            if wickets == balls/6 or wickets == 10:
                break
        else:
            com_total = com_total + computer
            remaining = target - com_total
            print(f'computer need {remaining} more runs to win in {balls - i - 1} balls')
            print("computer's total is now", com_total)
            if remaining <= 0:
                print('computer won')
                break
    if user_total > com_total:
        print('you win')
    elif user_total == com_total:
        print('tie')


def main():
    overs = int(input("How many overs would you like to play?\n"))
    print("The game is set for", overs, "overs")
    balls = overs * 6
    toss_input = input('choose odd or even')
    user_input = int(input('enter a number'))
    computer_input = random.randint(1, 6)
    print('computer choose', computer_input)
    odd_or_even = (user_input + computer_input) % 2
    if odd_or_even == 1:
        odd_or_even = 'odd'
    else:
        odd_or_even = 'even'
    if toss_input == odd_or_even:
        bat_or_ball = input('you won the toss choose bat or ball:')
        if bat_or_ball == 'bat':
            bat(balls)
        elif bat_or_ball == 'ball':
            ball(balls)
    else:
        bat_or_ball = random.randint(1, 2)
        if bat_or_ball == 1:
            print('Computer won the toss and elected to bat first')
            ball(balls)
        else:
            print('Computer won the toss and elected to bowl first')
            bat(balls)


main()

while True:
    play_again = input('Do you want to play again ? : ')
    if play_again == 'yes':
        main()
    else:
        break


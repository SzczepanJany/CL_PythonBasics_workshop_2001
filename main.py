from random import randint, choice
import re
DICES = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]

def throws_and_dices(is_user, type_of_throw= "D1"):
    '''
    Function is determinating which dice was choose
    '''
    while True and is_user:
        type_of_throw = input("Enter type of throw: ")
        x = re.compile("(D10(0)?|D3|D4|D6|D8|D12|D20)")
        if x.fullmatch(type_of_throw):
            break
        else:
            print("Enter correct form!")
    throw = re.split('D',type_of_throw)
    result = randint(1,int(throw[1]))
    return (result)

def calculate_score(points, is_user):
    '''
    Function is calulating score
    '''
    tmp_points = 0
    tmp_points += throws_and_dices(is_user, choice(DICES))
    tmp_points += throws_and_dices(is_user, choice(DICES))
    if tmp_points == 7:
        points = int(points/7)
    elif tmp_points == 11:
        points = points * 11
    else:
        points += tmp_points
    return points



user_points = 0
computer_points = 0

print("Enter Yours pick of dices (one by one)")
user_points += throws_and_dices(True)
user_points += throws_and_dices(True)
computer_points += throws_and_dices(False, choice(DICES))
computer_points += throws_and_dices(False, choice(DICES))
winner = ''

while user_points < 2001 or computer_points < 2001:
    print(f"Current score, user: {user_points}, coputer: {computer_points}")
    user_points = calculate_score(user_points,True)
    if user_points >= 2001:
        winner = "user"
        break
    computer_points = calculate_score(computer_points,False)
    if computer_points >= 2001:
        winner = "computer"
        break
print(f"Current score, user: {user_points}, computer: {computer_points}")
print(f"And the winner is: {winner}!!")

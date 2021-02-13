from flask import Flask, request
from random import randint,choice

app = Flask(__name__)
DICES = ["3", "4", "6", "8", "10", "12", "20", "100"]
def calculate_score(points, is_user, dice1 = 3, dice2 = 3):
    tmp_points = 0
    if is_user:
        pass    
    else:
        dice1=int(choice(DICES))
        dice2=int(choice(DICES))
    tmp_points += randint(1,dice1)
    tmp_points += randint(1,dice2)
    if tmp_points == 7:
        points = int(points/7)
    elif tmp_points == 11:
        points = points * 11
    else:
        points += tmp_points
    return points



@app.route('/', methods=['GET','POST'])
def game():
    if request.method == 'GET':
        page = f'''
        <form action="/" method="POST">
        <H1> Lets play a game. Pick Your dices and throw them! </H1>
        <table>
            <thead>
            <tr>
            <th>First Dice</th>
            <th>Second Dice</th>
            </tr>
            </thead>
            <tbody>
            <td>
            <input type="radio" id="dice1" name="dice1" value="3">
            <label for="3">D3</label><br>
            <input type="radio" id="dice1" name="dice1" value="4">
            <label for="4">D4</label><br>
            <input type="radio" id="dice1" name="dice1" value="6">
            <label for="6">D6</label><br>
            <input type="radio" id="dice1" name="dice1" value="8" checked>
            <label for="8">D8</label><br>
            <input type="radio" id="dice1" name="dice1" value="10">
            <label for="10">D10</label><br>
            <input type="radio" id="dice1" name="dice1" value="12">
            <label for="12">D12</label><br>
            <input type="radio" id="dice1" name="dice1" value="20">
            <label for="20">D20</label><br>
            <input type="radio" id="dice1" name="dice1" value="100">
            <label for="100">D100</label><br>                
            </td>
            <td>
            <input type="radio" id="dice2" name="dice2" value="3">
            <label for="3">D3</label><br>
            <input type="radio" id="dice2" name="dice2" value="4">
            <label for="4">D4</label><br>
            <input type="radio" id="dice2" name="dice2" value="6">
            <label for="6">D6</label><br>
            <input type="radio" id="dice2" name="dice2" value="8" checked>
            <label for="8">D8</label><br>
            <input type="radio" id="dice2" name="dice2" value="10">
            <label for="10">D10</label><br>
            <input type="radio" id="dice2" name="dice2" value="12">
            <label for="12">D12</label><br>
            <input type="radio" id="dice2" name="dice2" value="20">
            <label for="20">D20</label><br>
            <input type="radio" id="dice2" name="dice2" value="100">
            <label for="100">D100</label><br>
            </td>
            </tr>
            </tbody>
            </table>   
        <input type=hidden id="computer_points" name="computer_points" value=0><br><br>        
        <input type=hidden id="user_points" name="user_points" value=0><br><br>        
        <button name="Throw_button" type="submit">Throw!</button>
               
        '''
    if request.method == 'POST':
        user_points = request.form["user_points"]
        computer_points = request.form["computer_points"]
        dice_1 = request.form["dice1"]
        dice_2 = request.form["dice2"]
        computer_points = calculate_score(int(computer_points),False)
        user_points = calculate_score(int(user_points),True,int(dice_1), int(dice_2))
        if user_points < 2001 and computer_points < 2001:
            page = f'''
            <form action="/" method="POST">
            <H1> Current score, user: {user_points}, computer: {computer_points}. Pick Your dices and throw them! </H1>
            <table>
            <thead>
            <tr>
            <th>First Dice</th>
            <th>Second Dice</th>
            </tr>
            </thead>
            <tbody>
            <td>
            <input type="radio" id="dice1" name="dice1" value="3">
            <label for="3">D3</label><br>
            <input type="radio" id="dice1" name="dice1" value="4">
            <label for="4">D4</label><br>
            <input type="radio" id="dice1" name="dice1" value="6">
            <label for="6">D6</label><br>
            <input type="radio" id="dice1" name="dice1" value="8" checked>
            <label for="8">D8</label><br>
            <input type="radio" id="dice1" name="dice1" value="10">
            <label for="10">D10</label><br>
            <input type="radio" id="dice1" name="dice1" value="12">
            <label for="12">D12</label><br>
            <input type="radio" id="dice1" name="dice1" value="20">
            <label for="20">D20</label><br>
            <input type="radio" id="dice1" name="dice1" value="100">
            <label for="100">D100</label><br>                
            </td>
            <td>
            <input type="radio" id="dice2" name="dice2" value="3">
            <label for="3">D3</label><br>
            <input type="radio" id="dice2" name="dice2" value="4">
            <label for="4">D4</label><br>
            <input type="radio" id="dice2" name="dice2" value="6">
            <label for="6">D6</label><br>
            <input type="radio" id="dice2" name="dice2" value="8" checked>
            <label for="8">D8</label><br>
            <input type="radio" id="dice2" name="dice2" value="10">
            <label for="10">D10</label><br>
            <input type="radio" id="dice2" name="dice2" value="12">
            <label for="12">D12</label><br>
            <input type="radio" id="dice2" name="dice2" value="20">
            <label for="20">D20</label><br>
            <input type="radio" id="dice2" name="dice2" value="100">
            <label for="100">D100</label><br>
            </td>
            </tr>
            </tbody>
            </table>    
            <input type=hidden id="computer_points" name="computer_points" value={computer_points}><br><br>        
            <input type=hidden id="user_points" name="user_points" value={user_points}><br><br>        
            <button name="Throw_button" type="submit">Throw!</button>

            
            '''
        else:
            if user_points >= 2001:
                winner = "user"
            elif computer_points >= 2001:
                winner = "computer"
            page=f'''
            <form action="/" method="GET">
            <H3>Current score, user: {user_points}, computer: {computer_points}"</H3>
            <H1>And the winner is: {winner}!!</H1>
            <br><br>
            <button name="play_again" type="submit">Play again!</button>
            '''

    return page
if __name__ == '__main__':
    app.run(debug=False)


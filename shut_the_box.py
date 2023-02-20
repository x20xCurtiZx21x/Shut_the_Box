'''
Author: Chase Curtis
email: curtischase6@gmail.com
Email any questions
'''

#shut_the_box.py 

import random

from encoder import Encoder

def menu():

    count = 0

    record_list = records()

    print('====Welcome to Shut the Box====')

    while count == 0:

        print('')

        print('1) Single Player')

        print('2) Multiplayer')

        print('3) Check Stats')

        print('4) New Player')

        print('5) Prestige')

        print('6) Exit')

        try:

            option = int(input('Enter an option: '))

        except:

            option = 0

        print('')

        if option == 1:

            name = input('Enter your username: ')

            if check_player(name, record_list):

                try:

                    print('')

                    bet = input("Enter player's bet(Specified amount or type 'max'. 'max' = 100,000): ")

                    if bet == 'max' or bet == 'MAX':

                        bet = 100000

                    difficulty = set_difficulty()

                    if int(bet) <= 100000:

                        if check_bet(int(bet), name, record_list):

                            mult = multiplier(int(bet)) + max_bonus(name, record_list, int(bet))

                            bot_score = bot(difficulty)

                            p1_score = start()

                            print(f'{name}: {p1_score}')

                            print(f'Bot: {bot_score}')

                            if p1_score < bot_score or p1_score == 0:

                                print('')

                                print('You win!')

                                if mult > 0:

                                    xp = 50 * mult * difficulty

                                else:

                                    xp = 50 * difficulty

                                winning_bet = int(bet)

                                if p1_score == 0:

                                    xp += 500

                                    bonus = int(bet) / 2

                                    winning_bet += int(bonus)

                                win_stats(name, xp, record_list, winning_bet)

                            else:

                                print('')

                                print('You Lose!')

                                lose(name, record_list, int(bet))

                        else:

                            print('Invalid bet amount')

                except:

                    print('Invalid bet amount')

            else:

                print('')

                print("Player doesn't exist")

        elif option == 2:

            try:

                player_amt = int(input('Enter amount of players: '))

                if player_amt > 1:

                    player_list = []

                    for num in range(player_amt):

                        player = input(f'Enter player {num+1}: ')

                        if check_player(player, record_list):

                            try:
                            
                                bet = input("Enter player's bet(Specified amount or type 'max'. 'max' = 100,000): ")

                                if bet == 'max' or bet == 'MAX':

                                    bet = 100000

                                if int(bet) <= 100000:

                                    if check_bet(int(bet), player, record_list):

                                        mult = multiplier(int(bet)) + max_bonus(player, record_list, int(bet))

                                        if mult > 0:

                                            player_list.append([player, int(bet), mult])

                                        else:

                                            player_list.append([player, int(bet), 1])

                                    else:

                                        print('Invalid bet amount')

                                else:

                                    print('Invalid bet amount')

                            except:

                                print('Invalid bet amount')

                    if len(player_list) == player_amt:

                        winnings = 0

                        for item in player_list:

                            temp = int(item[1])

                            winnings += temp

                        player_results = []

                        for player in player_list:

                            print('')

                            print(f"{player[0]}'s turn!")

                            result = start()

                            player_results.append(result)

                        winner = min_value(player_results)

                        for num in range(len(player_list)):

                            print(f'{player_list[num][0]}: {player_results[num]}')

                        print('')

                        print(f'{player_list[winner][0]} wins!')

                        for num in range(len(player_list)):

                            if player_list[num][0] == player_list[winner][0]:

                                xp = 0

                                if int(player_list[winner][2]) == 0:

                                    xp = 500

                                    bonus = winnings / 2

                                    winnings += bonus

                                win_stats(player_list[winner][0], (player_amt*100*player_list[winner][2]) + xp, record_list, winnings)

                            else:

                                lose(player_list[num][0], record_list, player_list[num][1])

                    else:

                        print("Sorry, there wasn't enough players")

                else:

                    print('Sorry, that is not a valid player amount!')

            except:

                print('Sorry, that is not a valid player amount!')

        elif option == 3:

            name = input('Enter your username: ')

            if check_player(name, record_list):

                money = player_money(name, record_list)

                level = player_level(name, record_list)

                xp = player_xp(name, record_list)

                prestige = player_prestige(name, record_list)

                temp = Encoder(name, int(xp), int(level), int(money), prestige)

                code = temp.encode()

                print('')

                print(f'username: {name}')

                print(f'Money: ${money}')

                print(f'Level: {level}')

                print(f'xp: {xp}/{1000*level}')

                if prestige > 0:

                    print(f'Prestige: {prestige}')

                print(f'Player Code: {code}')

            else:

                print("Sorry, that player doesn't exist")

        elif option == 4:

            new_player(record_list)

        elif option == 5:

            name = input('Enter your username: ')

            if check_player(name, record_list):

                prestige_up(name, record_list)

            else:

                print("Sorry, player doesn't exist")

        elif option == 6:

            count = 1

            print('Goodbye!')

            exit(record_list)

        else:

            print("Sorry, that's not an option")

def max_bonus(name, record_list, bet):

    for item in record_list:

        if name == item[2]:

            temp = item

    if bet == int(temp[3]):

        return 2

    return 0

def multiplier(bet):

    mult = 0

    if bet > 100:

        mult = bet/100

    return int(mult)

def min_value(player_results):

    length = len(player_results)

    for index in range(length):

        if player_results[index] == min(player_results):

            return index

def check_bet(bet, name, record_list):

    for item in record_list:

        if name == item[2]:

            temp = item

    if 0 < bet <= int(temp[3]):

        return True
    
    return False

def bot(mode):

    if mode == 0.5:

        return random.randint(20, 30)

    elif mode == 1:

        return random.randint(10, 20)

    elif mode == 2:

        return random.randint(0, 15)

    else:

        return 0

def records():

    try:

        records = open('records.txt', 'r')

        record_list = []

        for line in records:

            record_list.append(line.split())

        records.close()

    except:

        record_list = []

    return record_list

def player_level(name, record_list):

    for item in record_list:

        if name == item[2]:

            temp = item

    return int(temp[1])

def player_xp(name, record_list):

    for item in record_list:

        if name == item[2]:

            temp = item

    return int(temp[0])

def player_money(name, record_list):

    for item in record_list:

        if name == item[2]:

            temp = item

    return int(temp[3])

def new_player(record_list):

    try:

        choice = input('Create New Player or Input a Code?(New/Code): ')

        if choice.upper() == 'NEW':

            name = input("Enter a username(NO SPACES OR '#'): ")

            if check_player(name, record_list):

                print('This Player already exists!')

            else:

                record_list.append([0, 1, name, 100, 0])

                print(f'New player added: {name}')

        elif choice.upper() == 'CODE':

            code = input('Enter your code: ')

            returning = Encoder()

            returning.decode(code)

            if check_player(returning._name, record_list):

                for item in record_list:

                        if returning._name == item[2]:

                            temp = item

                if (int(temp[1]) > 5) and (int(temp[0]) != 0) and (int(temp[3]) != 100) and (int(temp[3]) > 100) and (returning._level > int(temp[1])) and (returning._prestige >= int(temp[4])):

                    record_list.remove(temp)

                    record_list.append([returning._xp, returning._level, returning._name, returning._money, returning._prestige])

                    print(f'{returning._name} was updated!')

                else:
                
                    print('This Player already exists!')

            else:

                record_list.append([returning._xp, returning._level, returning._name, returning._money, returning._prestige])

                print(f'Player was found: {returning._name}')

    except:

        print('Invalid Input')

def prestige_up(name, record_list):

    for item in record_list:

        if name == item[2]:

            temp = item

    if (int(temp[3]) >= 10000*(int(temp[4]) + 1)) and int(temp[1]) >= 100:

        record_list.remove(temp)

        record_list.append([0, 1, name, 100, int(temp[4]) + 1])

        print(f'{name} has gone up in prestige!')

    else:

        print(f'Sorry, you need to have ${(int(temp[4]) + 1)*10000} and need to be level 100 to prestige!')

def player_prestige(name, record_list):

    for item in record_list:

        if name == item[2]:

            temp = item

    return int(temp[4])

def check_player(name, record_list):

    for item in record_list:

        if name == item[2]:

            return True

    return False

def lose(name, record_list, bet):

    for item in record_list:

        if name == item[2]:

            temp = item

    money = int(temp[3])

    temp[3] = money - bet

    if temp[3] <= 0:

        print(f'{name} has been reset')

        record_list.remove(temp)

        record_list.append([0, 1, name, 100, int(temp[4])])

def level_up(name, current_xp, level):

    level_xp = level*1000
    
    if current_xp >= level_xp:

        level += 1

        current_xp -= level_xp

        return level_up(name, current_xp, level)

    else:

        stats = [current_xp, level]

        return stats

def win_stats(name, xp, record_list, bet):

    for item in record_list:

        if name == item[2]:

            temp = item

    record_list.remove(temp)

    amount = int(temp[0])

    temp[0] = amount + int(xp)

    if temp[0] >= (int(temp[1])*1000):

        stats = level_up(name, int(temp[0]), int(temp[1]))

        print(f'{name} leveled up!')

        temp[0] = int(stats[0])

        temp[1] = int(stats[1])

    money = int(temp[3]) + bet

    temp[3] = money

    record_list.append(temp)

def exit(record_list):

    record = open('records.txt', 'w')

    for item in record_list:

        record.write(f'{item[0]} {item[1]} {item[2]} {item[3]} {item[4]}\n')

    record.close()

def new_game():

    options = []

    for num in range(10):

        options.append(num)

    options.remove(0)

    return options

def valid_moves(num_list, roll):

    count = 0

    for i in num_list:

        if i == roll:

            count += 1

        for j in num_list:

            if (i + j == roll) and i != j:

                count += 1

            for k in num_list:

                if (i + j + k == roll) and k != i and k != j and i != j:

                    count += 1

    if count > 0:

        return True
    
    else: 

        return False

def helper(user_input):

    try:

        new_input = []

        temp = user_input.split(',')

        for item in temp:

            new_input.append(int(item))

        return new_input

    except:

        print('')

        print('Invalid Input, Try Again!')

        return False

def d12():

    roll = d6() + d6()

    return roll

def d6():

    roll = random.randint(1,6)

    return roll

def add(user_nums, num):

    if num < 0:

        return 0

    else:

        return user_nums[num] + add(user_nums, num - 1)

def check_move(user_nums, roll, num_list):

    count = 0

    for i in user_nums:

        for j in num_list:

            if i == j:

                count += 1

    if count == len(user_nums):

        index = len(user_nums) - 1

        if add(user_nums, index) == roll:

            return True

        else:

            return False

    else:

        return False

def remove(user_nums, num_list):

    for num in user_nums:

        num_list.remove(num)

    return num_list

def num_check(num_list):

    check_list = []

    for i in num_list:

        for j in range(7,10):

            if i == j:

                return False

    return True

def start():

    count = 0

    num_list = new_game()

    while count == 0:

        turn_count = 0

        if len(num_list) > 0:

            if num_check(num_list):

                roll = d6()

            else:

                roll = d12()

            print('')

            print(f'Here is your roll: {roll}')

            if valid_moves(num_list, roll):

                while turn_count == 0:

                    print('')

                    print('Numbers Left:')

                    for num in num_list:

                        print(num)

                    user_input = input('Enter a number(If more than 1 number, seperate with a comma with no space): ')

                    input_check = helper(user_input)

                    if input_check == False:

                        print('')

                        print(f'Here is your roll: {roll}')

                    else:

                        if check_move(input_check, roll, num_list):

                            for num in input_check:

                                num_list.remove(num)

                            turn_count = 1

                        else:

                            print('')

                            print('Invalid Input, Try Again!')

                            print('')

                            print(f'Here is your roll: {roll}')

            else:

                print('')

                print('No Valid Moves!')

                print('')

                score = 0

                for num in num_list:

                    score += num

                print(f'Your Score: {score}')

                count = 1

        else:

            print('')

            print('You Shut the Box!')

            score = 0

            count = 1

    return score

def set_difficulty():

    try:

        print('')

        userinput = input("Enter a difficulty(Easy/Medium/Hard/Impossible): ")

        if userinput.lower() == "easy":

            return 0.5

        elif userinput.lower() == "medium":

            return 1

        elif userinput.lower() == "hard":

            return 2

        elif userinput.lower() == "impossible":

            return 3

        else:

            return 0.5

    except:

        return 0.5

menu()
#Filename: Blackjack.py
#Author: Campbell Bain
#Date: 31/05/2021
#Description: This is a game of blackjack where you try and gain as much money as possible without going bankrupt.



import random
import time
import json

#Setting up a save file for the money, losses, wins, bankrupts and the amount of debt you have.
json_attack = json.load(open('jason_derulo.json', 'r'))
money = json_attack['Money']
losses = json_attack['Losses']
wins = json_attack['Wins']
bankrupts = json_attack['Bankrupts']
debt = json_attack['Debt']

ace = 11
card_list = [ace, 2, 3, 4, 5, 6 , 7, 8, 9, 10, 10, 10, 10]
player_deck = [0]
house_deck = [0]
running = True
game = True
house_deck.append(random.choice(card_list))
house_deck.append(random.choice(card_list))
player_bust = False
stand = False
house_bust = False

#Writes the json save file with newer variables 
def jason_derulo():
    global money
    global wins
    global losses
    jason_dump = {
        'Money': money,
        'Wins': wins,
        'Losses': losses,
        'Bankrupts': bankrupts,
        "Debt": debt
    }
    with open('jason_derulo.json', 'w') as derulo_dump:
        json.dump(jason_dump, derulo_dump, indent = 4, sort_keys = True)
jason_derulo()

#Draws a random card to put into the deck. Uses which_deck to decide which deck to draw to.
def draw(which_deck):
    global ace
    global player_deck
    global house_deck
    picked_card = random.choice(card_list)
    if picked_card == ace and sum(which_deck) > 10:
        ace = 1
    else:
        ace = 11
    which_deck.append(picked_card)

 #Has all the game over scenarios and adds losses or wins.
def game_over():
    global game
    global wins
    global losses
    global house_deck
    global money
    time.sleep(1)
    print("The houses deck was ", sum(house_deck))
    time.sleep(1)
    game = False
    if sum(house_deck) == sum(player_deck) and player_bust != True and house_bust != True:
        print("You tied")
        time.sleep(1)
        print("Losses: ", losses, "Wins ", wins)
        return
    elif player_bust == True:
        losses += 1
        print("You busted xD")
        time.sleep(1)
        money -= bet
        print("Losses: ", losses, "Wins ", wins)
        return
    elif house_bust == True and player_bust != True:
        wins += 1
        print("The bot busted xD")
        time.sleep(1)
        money += bet
        print("Losses: ", losses, "Wins ", wins)
        return
    elif sum(house_deck) > sum(player_deck):
        losses += 1
        print("Why didn't you hit????")
        time.sleep(1)
        money -= bet
        print("Losses: ", losses, "Wins ", wins)
        return
    elif sum(player_deck) > sum(house_deck):
        wins += 1
        print("You beat the bot!")
        time.sleep(1)
        money += bet
        print("Losses: ", losses, "Wins ", wins)
        return

#Checks for busts
def bust_check():
    global game
    if game == True:
        if sum(player_deck) > 21:
            global player_bust
            player_bust = True
            game_over()
        if sum(house_deck) > 21:
            global house_bust
            house_bust = True


while running == True:
    player_bust = False
    stand = False
    house_bust = False
    game = True
    player_deck = [0]
    house_deck = [0]
    draw(player_deck)
    draw(player_deck)
    draw(house_deck)
    draw(house_deck)
    #To check if you are bankrupt and if so makes you in debt.
    if money == 0 or money < 0:
        money = 20
        time.sleep(1)
        print("You are bankrupt. You get $20 but you owe me...")
        debt += 20
        bankrupts += 1
        jason_derulo()
        time.sleep(1)
    #Asks if you want to pay back your debt.
    if money > debt and debt > 0:
        time.sleep(1)
        debt_collection = input("Do you want to pay back your debt? yes/no >>")
        if debt_collection == "yes":
            money -= debt
    time.sleep(1)
    #Asks for how much money you want to bet.
    print("your money: ", money)
    bet = input("How much money do you want to bet? >> ")
    bet = int(bet)
    while bet > money or bet < 0:
        bet = int(input("No. Try again >> "))
    print("Player deck", sum(player_deck))
    print("House card", house_deck[1])
    while game == True:
        choice = input("Hit or Stand? h/s: ")
        time.sleep(.5)
        if choice == "h" and player_bust != True:
            draw(player_deck)
            time.sleep(.5)
            print("You hit, your total is ", sum(player_deck))
            bust_check()
        else:
            time.sleep(.5)
            print("You stand")
            stand = True
        while sum(house_deck) < 17 and sum(house_deck) < sum(player_deck):
            draw(house_deck)
            bust_check()
        bust_check()
        if stand == True:
            game_over()
    jason_derulo()
    time.sleep(1)
    continue_playing = input("Do you wish to play again? y/n: ")
    if continue_playing == "n":
        running = False
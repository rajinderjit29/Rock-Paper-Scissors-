from ast import Break
from random import randint
import time 
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0, 2)]
player = False
while player == False:
    player = input('Please enter Rock, Paper, Scissors')
    if player == computer:
        print("tie")
    elif player == "Rock":
        if computer == "Paper":
            print("Computer wins")
        else:
            print("Player wins")
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer wins")
        else:
            print("Player wins")
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer wins")
        else:
            print("Player wins")
    else:
        print("Invalid input please enter Rock Paper Scissors")
    chance = input('Do you want to continue? yes or no')
    if chance == 'Yes':
        player = False
        computer = t[randint(0, 2)]
    elif chance == 'No':
        player = True 
        print("Have a great day. Byee")
        break
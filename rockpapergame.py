"""
work of project :

1- input from user (rock, paper, scissor)
2- computer choice (computer will choose raandomly not conditionally)
3- result print

cases:
A- rock 
rock- rock = tie
rock- paper = paper win
rock- scissor = rock wine

B- paper 
paper- paper = tie 
paper- rock = paper win 
paper- scissor = scissor win

C- scissor 
scissor- scissor = tie
scissor- rock = rock win
scissor- paper = scissor win

"""


import random
item_list = ["rock", "paper", "scisson"]

user_choice = input("enter your move = rock, paper, scissor = ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("both choose same: = match tie")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("paper covers rock = computer")

    else :
        print("rock smashes scissor = you win")

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("scissor cuts paper, computer win")
    else :
        print("paper covers rock, you win")   

elif user_choice == "scissor":
    if comp_choice == "paper":
        print("scissor cuts paper, computer win")
    else :
        print("rock smashes scissor, computer win")             

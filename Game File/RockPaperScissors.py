#imports duh
import random, os, sys

#Var for game
cpuscore = 0
userscore = 0
totalgames = int(input("How many games of Rock Paper Scissors!\n How many games would you like to play?"))
userchoice = ""
cpuchoice = ""
userwin = False
draw = False
choice = ""
clear =  lambda: os.system("cls")


# random number chooser using importyyy random

for x in range(0, totalgames):
    randomnum = random.randint(1,3)
    if randomnum == 1:
        cpuchoice = "rock"
    elif randomnum == 2:
        cpuchoice = "paper"
    elif randomnum == 3:
        cpuchoice == "scissors"


#user input choices

    userchoice = input("Select Rock, Paper, or Scissors\n")


#all user vs. cpu choices. win/lose
    if userchoice == "rock" and cpuchoice == "scissors":
        print("You selected",userchoice,"and the computer selected",cpuchoice,"You won this round!")
        userscore += 1
    elif userchoice == "rock" and cpuchoice == "paper":
        print("You selected",userchoice,"and the computer selected",cpuchoice,"You lost this round!")
        cpuscore += 1
    if userchoice == "paper" and cpuchoice == "rock":
        print("You selected",userchoice,"and the computer selected",cpuchoice,"You won this round!")
        userscore += 1
    elif userchoice == "paper" and cpuchoice == "scissors":
        print("You selected",userchoice,"and the computer selected",cpuchoice,". You lost this round!")
        cpuscore += 1
    if userchoice == "scissors" and cpuchoice == "paper":
        print("You selected",userchoice,"and the computer selected",cpuchoice,"You won this round!")
        userscore += 1
    elif userchoice == "scissors" and cpuchoice == "rock":
        print("You selected",userchoice,"and the computer selected",cpuchoice,"You lost this round!")
        cpuscore += 1

# who wins v. lose based on score

if userscore > cpuscore:
    userwin = True
elif userscore == cpuscore:
    draw = True

# User win and lose final

if userwin == True:
    print("Congratulations, you won!\nYour score:",userscore,"\nComputer's score:",cpuscore)
elif draw == True:
    print("You drew!\nYour score:",userscore,"\nComputer's score:",cpuscore)
elif userwin == False:
    print("I'm sorry, but you lost.\nYour score:",userscore,"\nComputer's score:",cpuscore)


#os and sys you will be able to restart the game

choice = str(input("Would you like to play again? y/n\n"))
if choice == "y":
    clear()
    os.system("RockPaperScissors.py")


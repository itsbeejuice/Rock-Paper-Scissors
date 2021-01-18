from random import choice, randint

t=["Rock","Paper","Scissors"]

win=0
loss=0
tie=0

player=False
while player==False:
    computer=choice(t)
    player=input("Rock, Paper, Scissors? ")
    if player==computer:
        print('Tieeee!')
        tie+=1
    elif player.lower()=="rock":
        if computer=="Paper":
            print("You lose! good day sir")
            loss+=1
        else:
            print("You win! Conrats!")
            win+=1
    elif player.lower()=="scissors":
        if computer=="Rock":
            print("You lose! good day<3")
            loss+=1
    elif player.lower()=="paper":
        if computer=="Scissors":
            print("You lose! good bye!")
            loss+=1
        else:
            print("You win!")
            win+=1
    else:
        print("Not a valid play, please try again")
    print("Wins=",win,"Losses=",loss,"Ties=",tie)
    player=False

#the tutorial(s) I have followed https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/ and https://theyuvas.com/rock-paper-scissors-in-python/ 

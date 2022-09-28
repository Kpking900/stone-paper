import random
score=0
while True:
    a=random.randint(1,3)
    if a==1:
       a="rock"
    if a==2:
       a="paper"
    if a==3:
       a="scissor"

    b=input("Your turn : ")

    if a==b:
       print("Draw")
    elif b=="rock":
       if a=="paper":
           print("you lose",a)
       else:
           print("You won")
           score=score+10
           print("score :",score)
    elif b=="paper":
       if a=="scissor":
          print("you lose",a)
       else:
           print("You won")
           score=score+10
           print("score :",score)
    elif b=="scissor":
       if a=="rock":
           print("you lose",a)
       else:
           print("You won")
           score=score+10
           print("score :",score)
    elif b=='exit':
        print("Game over")
        break

total_score=score
print("Total score : ", total_score)

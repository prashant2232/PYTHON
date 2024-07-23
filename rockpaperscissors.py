import random
def check(user,comp):
    if(comp==user):
        return 0
    if(comp==0 and user==2):
        return -1
    if(comp==1 and user==0):
        return -1
    if(comp==2 and user==1):
        return -1
    else:
       return 1

print("Welcome to the Amazing Rock, Paper or Scissor Game!!")   
user=int(input("Choose 0 for Rock, 1 for Paper or 2 for Scissor: "))
comp=random.randint(0, 2)
print("Your Choice: ",user)
print("Computer's Choice: ",comp)

score=check(user,comp)
if(score==0):
    print("It's a Draw")
elif(score==-1):
    print("You Lose")
else:
    print("You Won")


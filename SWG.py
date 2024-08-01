import random
def check(comp,choice):
    if comp==choice:
        return 1;
    elif (comp==0 and choice ==1):
        return 0
    elif (comp==1 and choice==2):
        return 0
    elif (comp==2 and choice==1):
        return 0
comp_count=0
user_count=0
choice=0
i=1
while (choice !=4):
    choice = int(input("\n=====Welcome to the snake, water and gun game=====\n=====Choose '0' for Snake '1' for Water and  '2' for gun\ enter 4 to exit=======\n"))
    comp=random.randint(0,2)
    result =check(comp,choice)
    if (result==1):
       print("It's draw")
    elif (result==0):
       comp_count+=1
       print("You lose in the round",i)
    else :
       user_count+=1
       print("You won  in the round",i)
    i+=1
if (comp_count>user_count):
    print("Oops ,You lose !!")
    print("Your score: ",user_count)
    print("Computer Score: ",comp_count)
elif (comp_count<user_count):
    print("Hurrah! ,You Won !!")
    print("Your score: ",user_count)
    print("Computer Score: ",comp_count)
else:
    print("It's draw")

import random
r=random.randint(1,100)
i=int(input("Lets play a game, guess the number that i m thinking about ,, Hint:its between 1 to 100: "))
count=1
while(i!=r):
    if(i<r):
        i=int(input("Higher number please: "))
        count+=1
    else:
        i=int(input("Lower Number please: "))
        count+=1
print(f"Congrats You won after {count} tries!")
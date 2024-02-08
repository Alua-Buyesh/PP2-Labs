from random import randint

def r(x,y):
    if x!= y:
        return False
    return True

y=randint(1,20)
print("Hello! What is your name?")
name= input()
g=0

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
x=int(input())
while not r(x,y):
    g+=1
    if x<y:
        print("Your guess is too low.")

    else:
        print("Your guess is too hight.")
    print("Take a guess.")
    x=int(input())
    

print(f"Good job, {name}! You guessed my number in {g} guesses!")
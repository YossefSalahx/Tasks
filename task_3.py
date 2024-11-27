import random
fruits=["apple", "orange", "banana", "strawberry"]
myrandom=random.choice(fruits)

characters=""
for char in random.sample(myrandom,len(myrandom)):
    characters +=char

print(characters)

tries=5
while tries>0:
    answer=input("enter your answer: ")
    if answer==myrandom:
        print("congrate!")
        break
    else:
        tries -=1
        print(f"try again you have {tries}")

if tries==0:
    print(f"GAME OVER! the correct answer is{myrandom}")
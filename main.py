# AS09
import random
wordlist = ["takes", "known", "kicks", "stark", "boots", "baton", "clear", "crime", "waste", "close", "sword",
            "slave", "fargo", "maybe", "males"]

print(", ".join(wordlist))

word = random.choice(wordlist)

strikes = 0
while strikes < 4:
    guess = input("\nInput guess")
    count = 0
    if guess == word:
        break
    for i in range(len(guess)):
        if guess[i] in word:
            if guess[i] not in guess[i + 1::]:
                count = count + 1
    print("The similarity is:", count)
    strikes = strikes + 1
    print("Strikes:", strikes)

print("The word was:", word)
if strikes < 4:
    print("You win!")
else:
    print("You lose!")

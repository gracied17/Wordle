import random
from words import word_list
from colorama import Fore

answer = random.choice(word_list)
guess = ""
for x in range(6):
    while True:
        guess = input()
        guess = guess.upper()
        if guess in word_list:
            break
    for i in range(0, len(answer)):
        if guess[i] == answer[i]:
            print(Fore.GREEN, guess[i], end="")
        elif guess[i] in answer:
            print(Fore.YELLOW, guess[i], end="")
        else:
            print(Fore.WHITE, guess[i], end="")
    print("\n")
    if guess == answer:
        break
    x += 1
if guess != answer:
    print(Fore.WHITE, "The answer was: " + answer)
else:
    print(Fore.WHITE, "You Win!")

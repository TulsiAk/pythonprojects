import random
from stage import stages
from wordlist import word_list
lives=len(stages)-1

word = random.choice(word_list)
print("Word to guess:", word)

display = ["_"] * len(word)
print(" ".join(display))
step = True
while step:
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        print(stages[lives])
        lives -= 1

    print(" ".join(display))

    if "_" not in display:
        print("Congratulations! You guessed the word.")
        step = False
    elif lives < 0:
        print("Game Over! The word was:", word)
        step = False

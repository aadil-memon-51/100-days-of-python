#day7_1
import random
word_list=["aadil","waiz","hammad","ali"]
word_chosen=random.choice(word_list)
guess=input("Guess a Letter ").lower()
for i in range(len(word_chosen)):
    if guess==word_chosen[i]:
        print("You guessed it right")
    else:
        print("Wrong guess!")

#day7_2
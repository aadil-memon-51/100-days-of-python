import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
rand_pick=random.randint(0,len(names)-1)
print(f"{names[rand_pick]} is going to buy the meal today! ")
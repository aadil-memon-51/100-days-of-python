print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
m_name=name1.lower()
y_name=name2.lower()
combine_name=m_name+y_name
a=0
b=0
a+=combine_name.count("t")
a+=combine_name.count("r")
a+=combine_name.count("u")
a+=combine_name.count("e")
b+=combine_name.count("l")
b+=combine_name.count("o")
b+=combine_name.count("v")
b+=combine_name.count("e")
score=int(f"{a}{b}")
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else: 
    print(f"Your score is {score}.")
print("Welcome to Python Pizza Deliveries! ")
bill=0
size=input("What size pizza do you want? S,M or L ")
if size=="Y":
    bill+=15
    print("Small size pizza price is: $15")

elif size=="M":
    bill += 20
    print("Medium size pizza price is: $20")

elif size=="L":
    bill += 25
    print("Large size pizza price is: $25")

else:
    print("Not such size!")
add_pepperoni=input("Do you want pepperoni? Y or N ")
if add_pepperoni=="Y":
    if size=="S":
        bill+=2
        print("extra amount for pepperoni: $2 for small pizza")
    else:
        bill+=3
        print("extra amount for pepperoni: $3 for medium or large pizza")
extra_cheese=input("Do you want extra cheeze? Y or N ")
if extra_cheese=="Y":
    bill+=1
    print("extra amount for extra cheese: $1")
print(f"your final bill is: ${bill}")

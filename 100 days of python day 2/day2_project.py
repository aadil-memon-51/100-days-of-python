print("Welcome to the tip calculator ")
t_bill=float(input("What was the total bill? $"))
p_tip=float(input("What percentage tip would you like to give? 10,12 or 15?"))/100
peoples=int(input("How many people to split the bill? "))
each_bill=(t_bill+t_bill*p_tip)/peoples
print(f"Each person should pay ${round(each_bill, 2)}")
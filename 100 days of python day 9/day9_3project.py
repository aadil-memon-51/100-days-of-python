from os import system
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction Program")
bidder="yes"
while bidder=="yes":
    bid_name=[input("What is your name?: ")]
    bid=[int(input("What\'s your bid?: $"))]
    bidders={}
    for i in range(len(bid_name)):
        bidders={
            bid_name[i]:bid[i]
        }
    bidder=input("Is there any Other bidders? Type 'yes' or 'no' ")
    if bidder=="yes":
        system("cls")
big_bid=0
winner=""
for b in bidders:
    b_amount=bidders[b]
    if b_amount>big_bid:
        big_bid=b_amount
        winner=b
print(f"The winner is {winner}, with a bid of ${big_bid}.")
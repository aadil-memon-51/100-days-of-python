row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#1st Method
# if position[0]=='1':
#     if position[1]=='1':
#         row1[0]='X'
#     elif position[1]=='2':
#         row2[0]='X'
#     elif position[1]=='3':
#         row3[0]='X'
#     else:
#         print("row doesn't exist!")
# elif position[0]=='2':
#     if position[1]=='1':
#         row1[1]='X'
#     elif position[1]=='2':
#         row2[1]='X'
#     elif position[1]=='3':
#         row3[1]='X'
#     else:
#         print("row doesn't exist!")
# elif position[0]=='3':
#     if position[1]=='1':
#         row1[2]='X'
#     elif position[1]=='2':
#         row2[2]='X'
#     elif position[1]=='3':
#         row3[2]='X'
#     else:
#         print("row doesn't exist!")
# else:
#     print("Wrong position Selected")
#2nd Method
map[int(position[1])-1][int(position[0])-1]='X'
print(f"{row1}\n{row2}\n{row3}")
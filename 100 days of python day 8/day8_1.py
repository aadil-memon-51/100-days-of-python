# def greet():
#     print("hi")
#     print("How are you?")
#     print("My babe! ")
# greet()
# def greet_with_loc(name,loc):
#     print(f"Hi {name} from {loc}")
# greet_with_loc(loc="Sujawal",name="Angela")

#day8_1
import math
def calc(height,width,cover):
    no_of_cans=math.ceil((height*width)/cover)
    print(f"You\'ll need {no_of_cans} cans ")
test_h=int(input("Height of wall: "))
test_w=int(input("Width of wall: "))
coverage=5
calc(width=test_w,cover=coverage,height=test_h)
# DECLARING HEADING OF CAFE
print("-----------------------------------------")
print("    CHIYA SANSAAR                        ")
print("------------------------------------------")

#USER GREETINGS
user_input=input("What's your name?\n :-")
print(f"Welcome,{user_input} in our CHIYA SANSAAR cafe\n")

# STORING IN LIST OF MENU
menu={
    "milk tea": 45,
    "black tea": 30,
    "black coffee": 70,
    "white coffee": 100,
    "bubble tea": 300,
}
total=0
#DISPLAYING MENU
print("---------------------------------------------")
print("         OUR MENU                              ") 
print("----------------------------------------------")
print("\n 1.Milk tea\n 2.Black tea\n 3.Black Coffee\n 4.White Coffee\n 5.Bubble tea\n ")

#USER ORDER PROCESS
user_repeat=int(input("How many times order would you like to place:- "))
for i in range(1,user_repeat+1):
    user_order=input("Enter your order please:- ").lower()
    if user_order in menu:
     new_order=int(input(f"Enter how many cup of {user_order} you like to order:- "))
     total+=new_order*menu[user_order]
    else:
     print(f"WE DON'T HAVE {user_order} IN OUR MENU")

print(f"Thank You,{user_input} for visiting\n")
print(f"Your total payable bill is NPR {total}")


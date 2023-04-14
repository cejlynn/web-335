# ==============================================
# ; Title: johnson_hobbies.py
# ; Author: Caitlynne Johnson
# ; Date: 13 April 2023
# ; Description: Experimenting with Python conditionals and iterators

# =============================================

# create a list of hobbies, using a for loop to iterate the list
hobbies = ["Writing", "Gaming", "Reading", "Baking", "Drawing"]
[print(x) for x in hobbies]


#create a list of days (sunday through saturday) and iterate the list.
#if else statement to display what day it is
days = ["Sunday", "Monday", "Tueday", "Wednesday", "Thursday", "Friday", "Saturday"]
for weekday in days:
    if weekday == "Sunday":
        print("It's your day off, enjoy it!")
    elif weekday == "Monday":
        print("You work today.")
    elif weekday == "Tuesday":
        print("You work today.")
    elif weekday == "Wednesday":
        print("You work today.")
    elif weekday == "Thursday":
        print("You work today.")
    elif weekday == "Friday":
        print("Yay, it's Friday! Too bad you still work today.")
    elif weekday == "Saturday":
        print("It's your day off, enjoy it!")
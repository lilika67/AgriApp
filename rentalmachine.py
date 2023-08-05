#This python codes are for all the group members
print("--------WELCOME TO OUR AGRICULTURAL RENTING MACHINE----------")
print("We have the following machines. Please choose any machine you want:")
print("1. Plow per one hour 1000/h")
print("2. Disc Harrow 1500/h")
print("3. Rotary Tiller 2000/h")
print("4. Cultivator 800/h")
print("5. Subsoiler 1200/h")

machine = int(input("Please choose any type of the machine(enter a number betueen 1 and 5):"))

if starting_hour >= ending_hour:
print("The starting hour must be less than the ending hour")
elif starting_hour > 24 or ending_hour > 24:
    print("Your hours must be within the range of 0-24 because it is a daily program")
    else:
        rental_hours = ending_hour - starting_hour
        if machine == 1:
            amount = rental_hours * 1000
        elif machine == 5:
            amount = rental_hours * 1200
            print("The amount of money you need to pay is", amount)
            elif machine == 2:
                amount = rental_hours * 1500
                elif machine == 3:

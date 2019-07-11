def even():
    a = [x * 10 if x % 2 == 0 else x for x in range(0, 20)]
    print(a)

even()




def age():
    a = int(input("How old are you: "))
    if a < 18:
        print("You are not up to the required age")
    else:
        print("You are up to the required age")
age()


#print("The age of the person")
print("\n")


def tell_age():
    age = int(input("Which year were you born: "))
    if age > 1919:
        ans = 2019 - age
        print("You are", ans)
    else:
        print("You better get serious,dude!,we are not in the ,mood for jokers")

tell_age() 


print("\n\n\t\t The age you is: ")
print("\n")





# Python program to check if the input year is a leap year or not

def leap_year():
    year = int(input("Enter a year: "))
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               print("{0} is a leap year".format(year))
           else:
               print("{0} is not a leap year".format(year))
       else:
           print("{0} is a leap year".format(year))
    else:
       print("{0} is not a leap year".format(year))
   
leap_year()
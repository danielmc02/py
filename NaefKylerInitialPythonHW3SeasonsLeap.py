#Kyler 696969

#Create var storing value of a month via int
Month = input("Enter the number of month you were born:\n")

#parse the input (string) to an int inorder to perform certain comperation operator
intMonth = int(Month)

if type(intMonth) == int and intMonth <= 12:
    # Creating a tuple (Immutable list) to store the months that will
    # be accesed via index of the number entered by the user
    months = ("January", "Febuary", "March", "April", "May", "June", "July",
              "August", "Semptember", "October", "November", "December")
    print("User birthday is the " + str(intMonth) + "th month of the year (" +
          str(months[intMonth - 1] + ")\n"))
    yearBorn = input("What year were you born (4 digit form): ")
    print("You were born in " + str(yearBorn))
    if intMonth in range(4,6):
        print("This means you were born in Spring")
    elif intMonth in range(7,9):
        print("This means you were born in Summer")
    elif intMonth in range(10-12):
        print("This means you were born in Fall")
    else:
        print("This means you were born in Winter")
    intYear = int(yearBorn)
    if intYear % 4 == 0:
        print("You were born on a leap year")
    else:
        print("You were not born on a leap year")
    #idk what she means on #10 by imputed year
else:
    print("Sorry value was not correct, plz try again")
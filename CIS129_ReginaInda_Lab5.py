# declare variables
totalBottles = 0 # will store accumulated bottle values 
counter = 1 # will control loop
todayBottles = 0 # will store number of bottles returned in a day
totalPayout = 0 # will store calculated value of totalBottles .10
keepGoing = 'y' # will run the program again

while keepGoing == 'y':
    totalBottles = 0

    for day in range(1,8):
        todayBottles = int(input(f"Enter number of bottles returned for day #{day}: "))
        totalBottles += todayBottles
        counter = counter + 1

    totalPayout = totalBottles * 0.10


    print(f"The total number of bottles collected is {totalBottles}")
    print(f"The total paid out is $ {totalPayout:.1f}")

# ask if user wants to keep entering data
    keepGoing = input("Do you want to enter another week's worth of data? (Enter y or n): ")

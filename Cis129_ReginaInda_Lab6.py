import math 
def main():
    total = 0 
    # get the total number of hot dogs needed
    total = get_total_hot_dogs()
    # names constants for the package sizes
    DOGS = 10 # hot dogs in a package 
    BUNS = 8 # buns in a package 

    # local variables 
    dogs_left = 0 # left over hot dogs
    buns_left = 0 # left over hot dog buns
    min_dogs = 0 # min packages of hot dogs 
    min_buns = 0 # min packages of buns 

    # calculate the number of left over hot dogs 
    dogs_left = (DOGS - total % DOGS) % DOGS 

    # calulate the min number of packages of hot dogs
    min_dogs = math.ceil(total / BUNS)

    # calculate the number of left over buns
    buns_left = (BUNS - total % BUNS) % BUNS
    
    # calculate min nmber of packages of buns
    min_buns = math.ceil(total / BUNS)

    # output 
    # display the results 
    show_results(dogs_left, min_dogs, buns_left, min_buns)

# get_total_hot_dogs mod. gets number of people
def get_total_hot_dogs():
    # local variables 
    people = 0 # number of peoplt attending 
    hot_dogs_per_person = 0 # hot dogs per person 

    # get number of people attending the cookout 
    people = int(input('Enter the number of people attending the cookout: '))

    # get the number of hot dogs each person will be given 
    hot_dogs_per_person = int(input('Enter the number of hot dogs each person will be given: '))

    # calculate the total number of hot dogs needed 
    total = people * hot_dogs_per_person
    return total

# show_results mod accepts the total number of hot dogs
def show_results(dogs_left, min_dogs, buns_left, min_buns):
    # display the min packages of hot dogs needed
    print('Minimum packages of hot dogs needed:', min_dogs)

    # display the min packages of buns needed
    print('Minimum packages of hot dog buns needed:', min_buns)

    # display number of hot dogs left over 
    print('Hot dogs left over:', dogs_left)

    # display number of hot dog buns left over 
    print('Hot dog buns left over:', buns_left)


main()
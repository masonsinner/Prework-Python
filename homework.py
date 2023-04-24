#Question 1 
def hello_name(user_name):
    """Prints Hello User!"""
    print("Hello " + user_name + "!")

user = input("Please enter your username :) ")

hello_name(user)

#Question 2
def first_odds():
    """Checks if number is odd, adding 1 each time"""
    current_number = 0
    while current_number < 100:
        current_number += 1
        if current_number % 2 == 0:
            continue
        print(current_number)

first_odds()

#Question 3 

def max_num_in_list(a_list):
    """Returns Maximum Number of list"""
    max = a_list[ 0 ]
    for a in a_list:
        if a > max:
            max = a
    return max
print(max_num_in_list([-1,2,4,5,656565]))

#Question 4
def is_leap_year(a_year):
    """Find if a given year is a Leap Year"""
    if((a_year % 400 == 0) or 
       (a_year % 100 != 0) and 
        (a_year % 4 == 0)):
        return True
    else:
        return False

year = input('Enter a year please: ')
leap_year = int(year) #converts year to int

is_leap_year(leap_year)

#Question 5 

def is_consecutive(a_list):
    """Find if a List is consecutive"""
    sorted_list = sorted(a_list)
    is_consecutive = all(
        sorted_list[i] == sorted_list[i - 1]
        + 1 for i in range(1, len(sorted_list))
        )

is_consecutive([1,5,4,3,2])

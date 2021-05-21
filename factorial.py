#!/usr/bin/env python3

# Created by: Jonathan
# Created on: May 21, 2021
# This program asks the user for a whole number. It
# then calculates the factorial of a number
def main():
    # initialize the loop counter and sum
    loop_counter = 0
    factorial_answer = 1

    # get the user number as a string
    user_number_string = input("Enter a positive number: ")
    print("")
    try:
        user_number_int = int(user_number_string)
        print("")
    except ValueError:
        print("Please enter a valid number")

    else:
        # replicates a do..while loop
        # calculates the factorial of the user number using a loop
        while True:
            loop_counter = loop_counter + 1
            factorial_answer = factorial_answer*loop_counter
            print("Tracking {0} times through loop.".format(loop_counter))
            if (loop_counter >= user_number_int):
                break
        if (user_number_int > 0):
            print("")
            print("{}! = {}".format(user_number_int, factorial_answer))
        else:
            print("")
            print("{0} is not a valid number".format(user_number_int))
    finally:
        print("")
        print("Thank you for your input")


if __name__ == "__main__":
    main()

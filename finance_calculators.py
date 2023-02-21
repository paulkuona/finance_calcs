"""
The program with the following code consists of two calculators.
The investment calculator calculates and tells the user how much they will earn in interest
over a given period of time and how much money they will have at the end of that period

The home loan repayment calculator (bond) calculates and tells the user how much they should 
expect to pay every month for a given period to fully repay their home loan.
"""

import math

def get_num(prompt):
    """This function uses a try/except block in a while loop to validate that a user has entered
    a number on which mathematical operations can be applied. The 'try' block casts the input to a float
    and returns the input in a variable num if it can be casted. If not, the except block loops back to the start
    and prompts the user to enter a number only. The get_num function will be used for all number inputs.
    """
    while True:
        num = input(prompt)
        try:
            num = float(num)
            return num
        except:
            print("Invalid entry! Please enter a number as requested.")

# Because the user will be asked to choose between two calculators, this 'while' loop will continue running
# until a valid choice between 'investment' and 'bond' is made
while True:
    
    # Ask user to choose the calculation they want to make
    calculator_choice = input(
    """Choose either 'investment' or 'bond' from the menu below to proceed:

    investment  -   to calculate the amount of interest you'll earn on your investment
    bond        -   to calculate the amount you'll have to pay on a home loan

    Enter your choice here: """
    )

    # Code for the investment calculator is within an 'if' block while the corresponding 'elif' block houses code for the loan
    # repayment calculator.
    # Escape characters (tab and new line) are used throughout the program to make outputs more readable.
    # str.lower() method is used throughout the program to convert user input to lowercase so that whatever case the user inputs can used in conditional statements

    if calculator_choice.lower() == "investment":
        # Getting inputs from using using get_num function
        principal = get_num("\n1.\tHow much are you looking to deposit? $")
        interest_rate = get_num("2.\tWhat's the interest rate you will get per annum?\n\tEnter just the number, excluding the '%' symbol: ")
        time = get_num("3.\tFor how long do you plan on investing?\n\tPlease enter just the number of years: ")

        # The following 'while' loop will run until the user makes a valid choice between 'simple' and 'compound' interest
        while True:
            interest_type = input("4.\tWould you like to calculate simple or compound interest?\n\tEnter 'simple' or 'compound': ")

            if interest_type.lower() == "simple":
                amount = principal * (1 + (interest_rate/100) * time)
                # Interest rate is divided by 100 to convert it to a percentage
                break
            elif interest_type.lower() == "compound":
                amount = principal * math.pow((1 + (interest_rate/100)) , time) 
                break
            else:
                print("\nINVALID CHOICE! Please choose between 'simple' or 'compund'.\nTry again :-)\n")
                continue
            # This 'else' block keeps the program in the loop if anything other than 'simple' or 'compound' is entered by the user
        
        # The formatting used below {variable:,.2f} ensure that the variable is rounded to 2 decimal places, and a comma is added as a thousand separator
        print(f"\nYou will earn ${(amount - principal):,.2f} in interest over the course of {int(time)} years!")
        print(f"That means you will have ${amount:,.2f} after this period!")
        break

    elif calculator_choice.lower() == "bond":
        # Taking user input
        house_value = get_num("\n1.\tWhat is the present value of the house which you intend to buy? $")
        interest_rate = get_num("2.\tAt what interest rate per annum are you getting your home loan?\n\tEnter just the number, excluding the '%' symbol: ")
        repayment_months = get_num("3.\tOver how many months do you wish to have fully repaid your home loan?\n\tEnter just the number of months: ")

        monthly_interest_rate = (interest_rate / 100) / 12
        monthly_repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-repayment_months))
        print(f"\nYou will need to pay ${monthly_repayment:,.2f} every month for {int(repayment_months)} months.")
        print(f"That's a total of ${monthly_repayment * repayment_months:,.2f} you will pay over time.")
        break
    else:
        print("\nINVALID CHOICE! Please choose between 'investment' or 'bond'.\nLet's start over :-)\n")
        continue
# Program responds to user based on input age
"""Technically negative whole numbers can be input but this will default to
age being less than first age condition, this can be potentially corrected 
in future development of code"""

# Request age input and store as integer
while True:
    try:
        age = int(input("Please enter your age (as a whole/integer number): "))
        if age <0:
            print("Please enter a non-negative value for age")
            continue
    except ValueError:
        print("Value input not recognised as an integer, please try again")
        continue
    else:
        break

# Set maximum age as 100
max_age = 100

# Set variables for age values that will be used as conditions to check against
age_condition1 = 13
age_condition2 = 21
age_condition3 = 40
age_condition4 = 65

# Set variables to store output statements to be used when certain conditions are met

output_statement1 = "You qualify for the kiddle discount."
output_statement2 = "Age is but a number."
output_statement3 = "Congrats on your 21st!"
output_statement4 = "You're over the hill."
output_statement5 ="Enjoy your retirement!"
output_statement6 = "Sorry, you're dead."


"""
Setting the age conditions and statements as variables allows for future changes to the output
without having to reset the rest of the code
"""

# Start conditioning on various ages to output a response
# First condition based on ages strictly below age_condition 1
if age < age_condition1:
    print(output_statement1)
#(age checked is age_condition1 < age < age_condition2)
elif age < age_condition2:
    print(output_statement2)
#(age checked is age_condition2 = age)
elif age == age_condition2:
    print(output_statement3)
#(age checked is age_condition2 < age < age_condition3)
elif age < age_condition3:
    print(output_statement2)
#(age checked is age_condition3 <= age < age_condition4)
elif age < age_condition4:
    print(output_statement4)
#(age checked is age_condition4 <= age <= max_age)
elif age <= max_age:
    print(output_statement5)
#(age checked is max_age <age)
else:
    print(output_statement6)

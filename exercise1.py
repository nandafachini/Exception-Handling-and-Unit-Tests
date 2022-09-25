# In this question you should identify the problematic parts of the code 
# and rewrite it using exception handling.

# That is, all the exceptions that may be generated must be identified and, 
# for each one, the appropriate treatment must be given, which, in this exercise, 
# means alerting the user to the problem.

# ------------------------------------------------
# | x = int(input('First value:'))               |
# | y = int(input('Second value:'))              |
# | z = x / y                                    |
# | print('The result of the division is:', z)   |
# ------------------------------------------------


while True:
    try:
        x = int(input('First value: '))
        y = int(input('Second value: '))
        z = x/y

    except ZeroDivisionError:
        print('Cannot divide by zero. Try again.')
    except ValueError:
        print('Numbers must be integers. Try again')
    else:
        print('The result of the division is: ', z)
        print('Program completed successfully')
        break
# Create a dictionary to store student registrations.
# Use the student's RA as a key and the student's name as a value.
# The data must be informed by the user.
# Each student's ID must consist of a string of exactly 7 characters.

# If the ID informed is not in the correct format, it must be generated
# an exception of type ValueError (use the raise statement).

# If the ID informed is already registered in the dictionary,
# an exception of type TypeError must be generated (use the raise statement).

student_registrarions = {}

for x in range(2):
    try:
        id = input('Digite seu RA: ')
        if len(id) != 7:
            raise ValueError
        elif id in student_registrarions:
            raise TypeError
    except ValueError:
        print('Your ID must contain exactly 7 integers')
    except TypeError:
        print('This ID is already registered!')
    else:
        name = input('Insert your name: ')
        student_registrarions[id] = name
# The code below throws an exception and stops the program execution.
# Using exception handling, correct the program in order to alert the 
# user about the error that occurred, and prevent the program from being 
# interrupted abruptly.

# ---------------------------------------------------
# |  def function_1():                              |
# |      print('Start of function')                 |
# |      list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     |
# |      for i in range(15):                        |
# |          print(list[i])                         |
# |      print('End of function')                   |
# |                                                 |
# |  print('Start of function')                     |
# |  function_1()                                   |
# |  print('End of function')                       |
# ---------------------------------------------------

def function_1():
    print('Start of function')
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(15):
        print(list[i])
    print('End of function')
try:
    print('Program start')
    function_1()

except IndexError:
    print("You tried to access a non-existent index")
else:
    pass
finally:
    print('End of program')

    
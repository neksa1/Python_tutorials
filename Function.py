# FUNCTION**************************


# function that don't receives argument and don't return value
def hello_func():
    print 'Hello function'
# calling function
hello_func()


# Function that don't receives argument and that return value
def hello_function_1():
    return 'Hello function'
#  calling function, we can chain other function because function return string
print hello_function_1().upper()


# Function that receives argument and return value
def hello_function_2(greeting):
    return '{} Function.'.format(greeting)
print hello_function_2('hi')


# If we don't  pass argument
def hello_function_3(greeting, name='Nemanja'):
    return '{} {}'.format(greeting, name)
# passing only one argument
print hello_function_3('hi')


# Function
def student_info(*args, **kwargs):
    print args              # tuple with all of positional arguments
    print kwargs         # dictionaries with all of keyword values
student_info('Math', 'Art', name='Johan', age=22)


# Passing unpacked list and dictionaries
courses = ['Math', 'Art']
info = {'name': 'Johan', 'age': 22}
student_info(*courses, **info)



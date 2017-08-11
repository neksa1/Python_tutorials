# Dictionaries***********************

# create dictionaries with keys and values, keys are: name, age, courses, / values: John, 25, ['Math', 'CompSci']
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}


# print value for the key 'name'
# print student['name']

# keys can be any data type
# student_1 = {'1': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# print student_1['1']

# adding new key and values, if key exists then value is updated
# student['phone'] = '555-5555'
# student['name'] = 'Jane'

# Update multiple values at a time
# student.update({'name': 'Jane', 'age': 26, 'phone': '6666-666'})

# access a key that don't exists, default value
# print student.get('new', 'Not found')

# Delete key, or you can use pop function
# del student['age']
# name = student.pop('name')

# printing dict's items
# print len(student)
# print student.keys()
# print student.values()
# print student.items()

# loping true dictionaries
for key, value in student.items():
    print key, value

# Print dict
print student

# SETS ***************************

# values that are unordered and have no duplicate

# making empty set
new_set = set()

# sets
cs_courses_1 = {'History', 'Math', 'Physics', 'CompSci'}
cs_courses_2 = {'History', 'Math', 'Art', 'Design'}

#  remove duplicated values
cs_courses_3 = {'History', 'Math', 'Physics', 'CompSci', 'CompSci'}

# common in two sets
print (cs_courses_1.intersection(cs_courses_2))

# differences in two sets
print (cs_courses_1.difference(cs_courses_2))

# combine sets
print (cs_courses_1.union(cs_courses_2))

# membership test, return True/False
print ('Math' in cs_courses_1)


# print cs_courses_1
# print cs_courses_2
# print cs_courses_3

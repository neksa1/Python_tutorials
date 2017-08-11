# TUPLES*************************

# razlika u odnosu na liste je ta sto elemente tuples ne mozemo da menjamo


tuple_1 = ('History', 'Math', 'Physics', 'CompSCI')
tuple_2 = tuple_1

# TypeError: 'tuple' object does not support item assignment
# tuple_1[0] = 'Art'

print tuple_1
print tuple_2

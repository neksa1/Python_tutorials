#  List********************************************************
courses = ['history', 'Math', 'art', 'compsci']
# courses_2 = ['PLc', 'Mechanic']
# nums = [1, 5, 6, 2, 3, 4]

# insertuje celu listu na mesto clana 2
# courses.insert(0, courses_2)

# insertuje samo clanove liste
# courses.extend(courses_2)

#  Dodavanje clanova na kraj liste
# courses.append('Physics')

# Insertovanje clanova na odredjeno mesto u listi (mesto, vrednost )
# courses.insert(0, 'Education')

# brisanje clanova liste
# courses.remove('Math')

# izbacuje clanove iz liste i vraca vrednost clana koji je izbacen, ()- clan kojeg izbacujem
# popped = courses.pop(-2)

# sortiranje liste, originalna lista je sortirana
# courses.sort(reverse=True)
# nums.sort(reverse=True)

# sortiranje liste bez uticaja na originalnu listu, sorting function
# sorted_curses = sorted(courses)

# interiranje kroz clanove liste
# for item in courses:
#     print item

# ako nam treba i indeks clana  pri interiranju
# for index, cours in enumerate(courses, start=1):
#     print index, cours

# sve clanove liste prebacujemo u string
course_str = ', '.join(courses)

# string delimo na clanove liste
new_list = course_str.split(', ')

# Printanje cele liste
print new_list
# print sortrted_curses

# indexa clana liste
# print courses.index('art')

# provera da li se clan nalazi u listi vraca TRUE/FALSE
# print ('art' in courses)


# printanje od clana do clana
# [0:2] slicing, printa od 0 (ukljucujuci i nulti) pa sve do 2 clana(ali ne i drugi)
# print courses[0:2]

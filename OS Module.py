import os
from datetime import datetime

# got  current  working dir
# print (os.getcwd())

# change  directory
# os.chdir('C://Users//nisajlovic//Documents//Python//Tutoria//')

# make new file
# os.mkdir('Os-Demo-2')                                       # dubina je 1
# os.makedirs('Os-Demo-2/Sub-Dir-1-1')            # dubina > 1


# remove file
# os.rmdir('Os-Demo-2')                 # brise samo taj dir
# os.removedirs('Os-Demo-2/Sub-Dir-1-1')

# rename file
# os.rename('nesto.txt', 'demo.txt')



#  print file details
# print (os.stat('demo.txt').st_mtime)
 #.st_size                 size of file
# st_mtime               modification time (time stamp)


mod_time = os.stat('demo.txt').st_mtime
print (datetime.fromtimestamp(mod_time))

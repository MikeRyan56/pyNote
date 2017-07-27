import random
from datetime import datetime, timedelta
import lorem
# import sys
import csv


def random_date():
    start = datetime.now()
    end = start + timedelta(days=365)
    rd = start + (end - start) * random.random()
    print(rd.isoformat(timespec='microsecond'))
    return rd.isoformat(timespec='microsecond')

# for x in range(0, 3):
#     print("We're on time %d" % (x))

Note = []
notes = []

for x in range(0,2):
    #notes = []
    notes.append(Note(note=lorem.paragraph(),created_by=1))
    print(notes)

# print(len(notes))

x = len(notes)
#xx = open('C:\\Users\\mrstu\Documents\\_Development\\pyProjects\\flask-appbuilder\\notes.csv')
for x in notes:
    #notes = []
    #notes.append(lorem.sentence())
    print(x)


# n = 0 

# for y in notes:
#     print(notes[n])
#     n += 1

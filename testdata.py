import logging
from app import db
from app.models import Note,Idea,IdeaNotes,Tags,Mood
import random
from datetime import datetime


# def date_now(self):
#     s = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     return s

# addmood = ['Positive','Neutral', 'Negative','Mixed']
  

# def pre_fill_db():
#     try:
#         db.session.add(Mood(mood_name='Positive',is_active=True))#,created_by="1",created_date=date_now))
#         #db.session.add(Mood(mood_name='Neutral',is_active=True,created_by="1",created_date=date_now))
#         # db.session.add(Mood(mood_name='Negative',is_active=1,created_by=1,created_date=datetime.datetime.now()))
#         # db.session.add(Mood(mood_name='Mixed',is_active=1,created_by=1,created_date=datetime.datetime.now()))
#         # db.session.add(Tags(tag_name='Unknown',is_active=1,created_by=1,created_date=datetime.datetime.now()))
#         # db.session.add(Tags(tag_name='Work',is_active=1,created_by=1,created_date=datetime.datetime.now()))
#         # db.session.add(Tags(tag_name='Life',is_active=1,created_by=1,created_date=datetime.datetime.now()))
#         # db.session.add(Tags(tag_name='Fun',is_active=1,created_by=1,created_date=datetime.datetime.now()))
#         # db.session.add(JobNoteStatus(status = 'Applied'))
#         # db.session.add(JobNoteStatus(status = 'Follow Up'))
#         # db.session.add(JobNoteStatus(status = 'Interview - Phone'))
#         # db.session.add(JobNoteStatus(status = 'Interview - In Persone'))
#         # db.session.add(JobNoteStatus(status = 'Offer-Negotiation'))
#         # db.session.add(JobNoteStatus(status = 'Offer-Rejected'))
#         # db.session.add(JobNoteStatus(status = 'Offer - Accepted'))
#         # db.session.add(JobNoteStatus(status = 'Close'))
#         db.session.commit()
#     except:
#         db.session.rollback()

# pre_fill_db()

# log = logging.getLogger(__name__)

# def date_now(self):
#     s = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     return s

# addmood = ['Positive','Neutral', 'Negative','Mixed']

# def get_random_name(names_list, size=1):
#     name_lst = [names_list[random.randrange(0, len(names_list))].capitalize() for i in range(0, size)]
#     return " ".join(name_lst)

# try:
#     db.session.query(Tags).delete()
#     db.session.query(Mood).delete()
#     # db.session.query(Note).delete()
# except:
#     db.session.rollback()

# try:
#     ideas = []
#     ideas.append(Idea(name='This One'))
#     ideas.append(Idea(name='This Two'))
#     ideas.append(Idea(name='This Three'))
#     db.session.add(ideas[0])
#     db.session.add(ideas[1])
#     db.session.add(ideas[2])
#     print(ideas[0].id)
#     db.session.commit()
# except ValueError:
#     log.error("Creating Ideas: %s", ValueError)
#     db.session.rollback()


# try:
#     genders = []
#     genders.append(Gender(name='Male'))
#     genders.append(Gender(name='Female'))
#     db.session.add(genders[0])
#     db.session.add(genders[1])
#     db.session.commit()
# except Exception, e:
#     log.error("Creating Genders: %s", e)
#     db.session.rollback()

# f = open('NAMES.DIC', "rb")
# names_list = [x.strip() for x in f.readlines()]

# f.close()

# for i in range(1, 1000):
#     c = Contact()
#     c.name = get_random_name(names_list, random.randrange(2, 6))
#     c.address = 'Street ' + names_list[random.randrange(0, len(names_list))]
#     c.personal_phone = random.randrange(1111111, 9999999)
#     c.personal_celphone = random.randrange(1111111, 9999999)
#     c.contact_group = groups[random.randrange(0, 3)]
#     c.gender = genders[random.randrange(0, 2)]
#     year = random.choice(range(1900, 2012))
#     month = random.choice(range(1, 12))
#     day = random.choice(range(1, 28))
#     c.birthday = datetime(year, month, day)
#     db.session.add(c)
#     try:
#         db.session.commit()
#         print "inserted", c
#     except Exception, e:
#         log.error("Creating Contact: %s", e)
#         db.session.rollback()
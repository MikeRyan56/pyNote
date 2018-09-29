from flask import g
from flask_appbuilder  import Model
from flask_appbuilder.models.mixins import AuditMixin, BaseMixin, FileColumn, ImageColumn
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Text, DateTime, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timedelta,MINYEAR,date
import re
from flask_appbuilder import Base

"""


You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
mindate = date(MINYEAR, 1, 1)

def get_user():
    return g.user.id

def set_date_plus7(self):
    p7 = datetime.now() + timedelta(days=7)
    # return p7.strftime("%Y-%m-%d %H:%M:%S")
    return p7.strftime("%Y-%m-%d %H:%M:%S")

def date_now():
    n = datetime.now()
    return n.strftime("%Y-%m-%d %H:%M:%S")

class Mood(Model):
    id = Column(Integer, primary_key=True)
    mood_name = Column(String(150), unique = True, nullable=False)
    # is_active = Column(Boolean, unique=False, default=True)
    # created_by = Column(Integer, ForeignKey('ab_user.id'), default=get_user, nullable=False) 
    # created_date = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)

    def __unicode__(self):
        return self.mood_name

    def __repr__(self):
        return self.mood_name
    def __str__(self):
        return self.mood_name



class Tags(Model):
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(150), unique = True, nullable=False)
    # is_active = Column(Boolean, unique=False, default=True)
    # created_by = Column(Integer, ForeignKey('ab_user.id'), default=get_user, nullable=False) 
    # created_date = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)


    def __unicode__(self):
        return self.tag_name

    def __repr__(self):
        return self.tag_name

    def __str__(self):
        return self.tag_name

assoc_tags_notes = Table('tags_notes', Model.metadata,
                                      Column('id', Integer, primary_key=True),
                                      Column('tags_id', Integer, ForeignKey('tags.id')),
                                      Column('notes_id', Integer, ForeignKey('note.id'))
)

class Note(Model): 
    id = Column(Integer, primary_key=True)
    mood_id = Column(Integer, ForeignKey('mood.id'), nullable=False)
    mood = relationship("Mood")
    tags = relationship('Tags', secondary=assoc_tags_notes, backref='note')
    my_note = Column(Text(), nullable=False)
    created_by = Column(Integer, ForeignKey('ab_user.id'), default=get_user, nullable=False) # Column(Integer)
    created_date = Column(DateTime, default=date_now, nullable=False)

    # @hybrid_property
    # def first_words(self):
    #     x = self.my_note[:10]
    #     return x

    @hybrid_property
    def word_count(self):
        wc = re.findall("(\S+)", self.my_note)
        return len(wc)
 
    @hybrid_property
    def text_count(self):
        s = self.my_note
        return len(self.my_note)
    
    def month_year(self):
        date = self.created_date # or mindate
        return datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.created_date # or mindate
        return datetime(date.year, 1, 1)


class Idea(BaseMixin, Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(Text(),nullable=False)
    is_active = Column(Boolean, unique=False, default=True)
    created_by = Column(Integer, ForeignKey('ab_user.id'), default=get_user, nullable=False) # Column(Integer)
    created_date = Column(DateTime, default=date_now, nullable=False)

    @hybrid_property
    def days_created(self):
        cd = self.created_date
        n = datetime.now()
        diff = n - cd
        return diff.days

    @hybrid_property
    def word_count(self):
        wc = re.findall("(\S+)", self.description)
        return len(wc)
 
    @hybrid_property
    def text_count(self):
        s = self.my_note
        return len(self.description)

    def month_year(self):
        date = self.created_date # or mindate
        return datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.created_date # or mindate
        return datetime(date.year, 1, 1)

    def __repr__(self):
        return self.name


class IdeaNotes(BaseMixin, Base):
    id = Column(Integer, primary_key=True)
    title =  Column(String(150), nullable=False)
    description = Column(Text())
    is_active = Column(Boolean, unique=False, default=True)
    created_date = Column(DateTime, default=date_now, nullable=False)
    follow_up_date = Column(DateTime, default=set_date_plus7, nullable=False)
    created_by = Column(Integer, ForeignKey('ab_user.id'), default=get_user, nullable=False) 
    idea_id = Column(Integer, ForeignKey('idea.id'), nullable=False)
    idea_group = relationship("Idea")
    
    @hybrid_property
    def word_count(self):
        wc = re.findall("(\S+)", self.description)
        return len(wc)

    def month_year(self):
        date = self.created_date # or mindate
        return datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.created_date # or mindate
        return datetime(date.year, 1, 1)

    def __repr__(self):
        return self.title


# class Job(Model): # Change Contact to Note
#     id = Column(Integer, primary_key=True)
#     company = Column(String(150))
#     contact_name = Column(String(150))
#     address = Column(String(150))
#     city = Column(String(150))
#     state = Column(String(150))
#     postal_code = Column(String(50))
#     phone = Column(String(150))
#     email = Column(String(150))
#     website = Column(String(150))
#     is_active = Column(Boolean, unique=False, default=True)
#     created_by = Column(Integer, ForeignKey('ab_user.id'), default=get_user, nullable=False) # Column(Integer)
#     created_date = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
    
#     def __repr__(self):
#         return self.company

# class JobTitle(Model): # Change Contact to Note
#     id = Column(Integer, primary_key=True)
#     title = Column(String(150))
#     career_site_link = Column(String(150))
#     is_active = Column(Boolean, unique=False, default=True)
#     created_by = Column(Integer, ForeignKey('ab_user.id'), default=get_user, nullable=False) # Column(Integer)
#     created_date = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
#     job_id = Column(Integer, ForeignKey('job.id'), nullable=False)
#     job = relationship("Job")

#     def __repr__(self):
#             return self.title

# class JobNoteStatus(Model):
#     id = Column(Integer, primary_key=True)
#     status = Column(String(150))
#     is_active = Column(Boolean, unique=False, default=True)

#     def __unicode__(self):
#         return self.status

#     def __repr__(self):
#         return self.status

#     def __str__(self):
#         return self.status
    

# class JobNotes(Model):
#     id = Column(Integer, primary_key=True)
#     is_active = Column(Boolean, unique=False, default=True)
#     note = Column(Text(4000))
#     follow_up_date = Column(DateTime, default=set_date_plus7, nullable=False)
#     created_by = Column(Integer, ForeignKey('ab_user.id'), default=get_user, nullable=False) # Column(Integer)
#     created_date = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
#     jobstatus_id = Column(Integer, ForeignKey('jobnotestatus.id'), nullable=False)
#     jobstatus = relationship("JobNoteStatus")
#     jobtitle_id = Column(Integer, ForeignKey('jobtitle.id'), nullable=False)
#     JobTitle = relationship("JobTitle")




    def month_year(self):
        date = self.created_date # or mindate
        return datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.created_date # or mindate
        return datetime(date.year, 1, 1)

    
from flask import g
from flask_appbuilder  import Model
from flask_appbuilder.models.mixins import AuditMixin, BaseMixin, FileColumn, ImageColumn
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Text, DateTime, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
import datetime
import re
from flask_appbuilder import Base

"""


You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
mindate = datetime.date(datetime.MINYEAR, 1, 1)

        
class Mood(Model): # Change Gender to Mood
    id = Column(Integer, primary_key=True)
    mood_name = Column(String(150), unique = True, nullable=False)

    def __unicode__(self):
        return self.mood_name

    def __repr__(self):
        return self.mood_name
    def __str__(self):
        return self.mood_name



class Tags(Model):
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(150), unique = True, nullable=False)


    def __unicode__(self):
        return self.tag_name

    def __repr__(self):
        return self.tag_name

    def __str__(self):
        return self.tag_name

# def get_user_id(cls):
#         try:
#             return g.user.id
#         except Exception as e:
#             # log.warning("AuditMixin Get User ID {0}".format(str(e)))
#             return None

def get_user():
    return g.user.id

def set_date_plus7(self):
    p7 = datetime.datetime.now() + datetime.timedelta(days=7)
    return p7.strftime("%Y-%m-%d %H:%M:%S")

assoc_tags_notes = Table('tags_notes', Model.metadata,
                                      Column('id', Integer, primary_key=True),
                                      Column('tags_id', Integer, ForeignKey('tags.id')),
                                      Column('notes_id', Integer, ForeignKey('note.id'))
)

class Note(Model): # Change Contact to Note
    id = Column(Integer, primary_key=True)
    mood_id = Column(Integer, ForeignKey('mood.id'), nullable=False)
    mood = relationship("Mood")
    # tags_id = Column(Integer, ForeignKey('tags.id'), nullable=False)
    # tags = relationship("Tags")
    tags = relationship('Tags', secondary=assoc_tags_notes, backref='note')
    my_note = Column(Text(), nullable=False)
    created_by = Column(Integer, ForeignKey('ab_user.id'), default=get_user, nullable=False) # Column(Integer)
    created_date = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
#    txt_count = Column(Integer, default=text_count(my_note))


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
        return datetime.datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.created_date # or mindate
        return datetime.datetime(date.year, 1, 1)


# class ContactGroup(BaseMixin, Base):
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique = True, nullable=False)

#     def __repr__(self):
#         return self.name


# class Gender(BaseMixin, Base):
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique = True, nullable=False)

#     def __repr__(self):
#         return self.name


# class Contact(BaseMixin, Base):
#     id = Column(Integer, primary_key=True)
#     name =  Column(String(150), unique = True, nullable=False)
#     address = Column(String(564))
#     birthday = Column(Date, nullable=True)
#     personal_phone = Column(String(20))
#     personal_celphone = Column(String(20))
#     contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=False)
#     contact_group = relationship("ContactGroup")
#     gender_id = Column(Integer, ForeignKey('gender.id'), nullable=False)
#     gender = relationship("Gender")

#     def __repr__(self):
#         return self.name

class Idea(BaseMixin, Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)
    is_active = Column(Boolean, unique=False, default=True)
    created_by = Column(Integer, ForeignKey('ab_user.id'), default=get_user, nullable=False) # Column(Integer)
    created_date = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)

    def __repr__(self):
        return self.name


class IdeaNotes(BaseMixin, Base):
    id = Column(Integer, primary_key=True)
    # name = Column(String(200), default=name_note, nullable=False)
    title =  Column(String(150), nullable=False)
    description = Column(Text())
    is_active = Column(Boolean, unique=False, default=True)
    created_date = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
    follow_up_date = Column(DateTime, default=set_date_plus7, nullable=False)
    idea_id = Column(Integer, ForeignKey('idea.id'), nullable=False)
    idea_group = relationship("Idea")
    
    # @hybrid_property
    # def name_concate(self):
    #     s = str(title + ' - ' + created_date )
    #     return s

    @hybrid_property
    def word_count(self):
        wc = re.findall("(\S+)", self.description)
        return len(wc)

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
#     created_date = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
    
#     def __repr__(self):
#         return self.company

# class JobTitle(Model): # Change Contact to Note
#     id = Column(Integer, primary_key=True)
#     title = Column(String(150))
#     career_site_link = Column(String(150))
#     is_active = Column(Boolean, unique=False, default=True)
#     created_by = Column(Integer, ForeignKey('ab_user.id'), default=get_user, nullable=False) # Column(Integer)
#     created_date = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
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
#     created_date = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nullable=False)
#     jobstatus_id = Column(Integer, ForeignKey('jobnotestatus.id'), nullable=False)
#     jobstatus = relationship("JobNoteStatus")
#     jobtitle_id = Column(Integer, ForeignKey('jobtitle.id'), nullable=False)
#     JobTitle = relationship("JobTitle")




    def month_year(self):
        date = self.create_date # or mindate
        return datetime.datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.create_date # or mindate
        return datetime.datetime(date.year, 1, 1)

    
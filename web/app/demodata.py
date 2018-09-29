import logging
from app import db
from app.models import Note,Idea,IdeaNotes,Tags,Mood
import random
from datetime import datetime, timedelta
import lorem
# import sys
# #from . import const as c
log = logging.getLogger(__name__)

def random_date():
    start = datetime.now()
    end = start + timedelta(days=365)
    rd = start + (end - start) * random.random()
    print(rd.isoformat(timespec='microsecond'))
    return rd.isoformat(timespec='microsecond')

# # start = datetime.now()
# # end = start + timedelta(days=-365)
# # random_date = start + (end - start) * random.random()

# def import_application(app_package, appbuilder):
#     sys.path.append(os.getcwd())
#     # try:
#     #     _app = __import__(app_package)
#     # except Exception as e:
#     #     click.echo(click.style('Was unable to import {0} Error: {1}'.format(app_package, e), fg='red'))
#     #     exit(3)
#     # if hasattr(_app, 'appbuilder'):
#     #     return getattr(_app, appbuilder)
#     # else:
#     #     click.echo(click.style('There in no appbuilder var on your package, you can use appbuilder parameter to config', fg='red'))
#     #     exit(3)

# def createAdmin():
#     try:
        
#         app ='app'
#         appbuilder = 'appbuilder'
#         _appbuilder = import_application(app, appbuilder)
#         # auth_type = {c.AUTH_DB:"Database Authentications",
#         #             c.AUTH_OID:"OpenID Authentication",
#         #             c.AUTH_LDAP:"LDAP Authentication",
#         #             c.AUTH_REMOTE_USER:"WebServer REMOTE_USER Authentication",
#         #             c.AUTH_OAUTH:"OAuth Authentication"}
#         username = 'Admin'
#         firstname = 'Administrator'
#         lastname = 'Account'
#         email = 'pyNote@DevSetGo.com'
#         role_admin = _appbuilder.sm.find_role(_appbuilder.sm.auth_role_admin)
#         password = '$Password'

#         # click.echo(click.style('Recognized {0}.'.format(auth_type.get(_appbuilder.sm.auth_type,'No Auth method')), fg='green'))
#         role_admin = _appbuilder.sm.find_role(_appbuilder.sm.auth_role_admin)
#         user = _appbuilder.sm.add_user(username, firstname, lastname, email, role_admin, password)
#         if user:
#             print('Admin User {0} created.'.format(username))
#             # click.echo(click.style('Admin User {0} created.'.format(username), fg='green'))
#         else:
#             print('No user created an error occured')
#             # click.echo(click.style('No user created an error occured', fg='red'))

#         # admin = []
#         # db.session.add(ab_user[0])
#         # db.session.commit()
#     except ValueError:
#         log.error("Creating Admin: %s", ValueError)
#         print(db.error)
#         db.session.rollback()
#     return

# Prefill the database with sample data
def pre_fill_db():
    try:
        moods = []
        moods.append(Mood(mood_name='Positive'))#, is_active=1, created_by=1, created_date=datetime.now()))
        moods.append(Mood(mood_name='Neutral'))#, is_active=1, created_by=1, created_date=datetime.now()))
        moods.append(Mood(mood_name='Negative'))#, is_active=1, created_by=1, created_date=datetime.now()))
        # db.session.add(moods[0])
        # db.session.add(moods[1])
        # db.session.add(moods[2])
        m = len(moods)
        for y in moods:
            db.session.add(moods[m])
            m += 1

        tags = []
        tags.append(Tags(tag_name='Unknown'))#, is_active=1, created_by=1, created_date=datetime.now()))
        tags.append(Tags(tag_name='Work'))#, is_active=1, created_by=1, created_date=datetime.now()))
        tags.append(Tags(tag_name='Family'))#, is_active=1, created_by=1, created_date=datetime.now()))
        tags.append(Tags(tag_name='Friends'))#, is_active=1, created_by=1, created_date=datetime.now()))
        tags.append(Tags(tag_name='Development'))#, is_active=1, created_by=1, created_date=datetime.now()))
        db.session.add(tags[0])
        db.session.add(tags[1])
        db.session.add(tags[2])
        db.session.add(tags[3])

        notes = []
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, create_date=random_date()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, create_date=random_date()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, create_date=random_date()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, create_date=random_date()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, create_date=random_date()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, create_date=random_date()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, create_date=random_date()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, create_date=random_date()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, create_date=random_date()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, create_date=random_date()))
        db.session.add(notes[0])
        db.session.add(notes[1])
        db.session.add(notes[2])
        db.session.add(notes[3])
        db.session.add(notes[4])
        db.session.add(notes[5])
        db.session.add(notes[6])
        db.session.add(notes[7])
        db.session.add(notes[8])
        db.session.add(notes[9])

        # tagnote = []
        # tagnote.append(tags_notes(tags_id=1,notes_id=1))
        # tagnote.append(tags_notes(tags_id=2,notes_id=1))
        # tagnote.append(tags_notes(tags_id=3,notes_id=1))
        # tagnote.append(tags_notes(tags_id=4,notes_id=1))
        # tagnote.append(tags_notes(tags_id=2,notes_id=2))
        # tagnote.append(tags_notes(tags_id=3,notes_id=2))
        # tagnote.append(tags_notes(tags_id=4,notes_id=2))
        # tagnote.append(tags_notes(tags_id=3,notes_id=3))
        # tagnote.append(tags_notes(tags_id=4,notes_id=3))
        # tagnote.append(tags_notes(tags_id=4,notes_id=4))
        # db.session.add(tagnote[0])
        # db.session.add(tagnote[1])
        # db.session.add(tagnote[2])
        # db.session.add(tagnote[3])
        # db.session.add(tagnote[4])
        # db.session.add(tagnote[5])
        # db.session.add(tagnote[6])
        # db.session.add(tagnote[7])
        # db.session.add(tagnote[8])
        # db.session.add(tagnote[9])

        ideas = []
        ideas.append(Idea(name=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), created_by=1,create_date=random_date()))
        ideas.append(Idea(name=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), created_by=1,create_date=random_date()))
        db.session.add(ideas[0])
        db.session.add(ideas[1])

        ideanotes = []
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), idea_id=1,
        created_by=1, create_date=random_date(),follow_up_date=datetime.now() + timedelta(days=random.random())))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), idea_id=1,
        created_by=1, create_date=random_date(),follow_up_date=datetime.now() + timedelta(days=random.random())))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), idea_id=1,
        created_by=1, create_date=random_date(),follow_up_date=datetime.now() + timedelta(days=random.random())))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), idea_id=1,
        created_by=1, create_date=random_date(),follow_up_date=datetime.now() + timedelta(days=random.random())))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), idea_id=1,
        created_by=1, create_date=random_date(),follow_up_date=datetime.now() + timedelta(days=random.random())))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), idea_id=2,
        created_by=1, create_date=random_date(),follow_up_date=datetime.now() + timedelta(days=random.random())))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), idea_id=2,
        created_by=1, create_date=random_date(),follow_up_date=datetime.now() + timedelta(days=random.random())))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), idea_id=2,
        created_by=1, create_date=random_date(),follow_up_date=datetime.now() + timedelta(days=random.random())))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), idea_id=2,
        created_by=1, create_date=random_date(),follow_up_date=datetime.now() + timedelta(days=random.random())))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.choice([True, False]), idea_id=2,
        created_by=1, create_date=random_date(),follow_up_date=datetime.now() + timedelta(days=random.random())))
        db.session.add(ideanotes[0])
        db.session.add(ideanotes[0])
        db.session.add(ideanotes[1])
        db.session.add(ideanotes[2])
        db.session.add(ideanotes[3])
        db.session.add(ideanotes[4])
        db.session.add(ideanotes[5])
        db.session.add(ideanotes[6])
        db.session.add(ideanotes[7])
        db.session.add(ideanotes[8])
        db.session.add(ideanotes[9])
        
        db.session.commit()
    # except ValueError:
    except ValueError as e:
        # log.error("Creating mood: %s", ValueError)
        # print(db.error)
        print(e)
        db.session.rollback()

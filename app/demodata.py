import logging
from app import db
from app.models import Note,Idea,IdeaNotes,Tags,Mood
import random
import datetime
import lorem

# Prefill the database with sample data
def pre_fill_db():
    try:
        moods = []
        moods.append(Mood(mood_name='Positive', is_active=1, created_by=1, created_date=datetime.datetime.now()))
        moods.append(Mood(mood_name='Neutral', is_active=1, created_by=1, created_date=datetime.datetime.now()))
        moods.append(Mood(mood_name='Negative', is_active=1, created_by=1, created_date=datetime.datetime.now()))
        db.session.add(moods[0])
        db.session.add(moods[1])
        db.session.add(moods[2])

        tags = []
        tags.append(Tags(tag_name='Unknown', is_active=1, created_by=1, created_date=datetime.datetime.now()))
        tags.append(Tags(tag_name='Work', is_active=1, created_by=1, created_date=datetime.datetime.now()))
        tags.append(Tags(tag_name='Family', is_active=1, created_by=1, created_date=datetime.datetime.now()))
        tags.append(Tags(tag_name='Friends', is_active=1, created_by=1, created_date=datetime.datetime.now()))
        tags.append(Tags(tag_name='Development', is_active=1, created_by=1, created_date=datetime.datetime.now()))
        db.session.add(tags[0])
        db.session.add(tags[1])
        db.session.add(tags[2])
        db.session.add(tags[3])

        notes = []
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, created_date=datetime.datetime.now()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, created_date=datetime.datetime.now()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, created_date=datetime.datetime.now()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, created_date=datetime.datetime.now()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, created_date=datetime.datetime.now()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, created_date=datetime.datetime.now()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, created_date=datetime.datetime.now()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, created_date=datetime.datetime.now()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, created_date=datetime.datetime.now()))
        notes.append(Note(mood_id=random.randrange(1, 3), my_note=lorem.paragraph(), created_by=1, created_date=datetime.datetime.now()))
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
        ideas.append(Idea(name=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), created_by=1,created_date=datetime.datetime.now()))
        ideas.append(Idea(name=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), created_by=1,created_date=datetime.datetime.now()))
        db.session.add(ideas[0])
        db.session.add(ideas[1])

        ideanotes = []
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), idea_id=1,
        created_by=1, created_date=datetime.datetime.now(),follow_up_date=datetime.datetime.now() + datetime.timedelta(days=7)))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), idea_id=1,
        created_by=1, created_date=datetime.datetime.now(),follow_up_date=datetime.datetime.now() + datetime.timedelta(days=7)))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), idea_id=1,
        created_by=1, created_date=datetime.datetime.now(),follow_up_date=datetime.datetime.now() + datetime.timedelta(days=7)))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), idea_id=1,
        created_by=1, created_date=datetime.datetime.now(),follow_up_date=datetime.datetime.now() + datetime.timedelta(days=7)))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), idea_id=1,
        created_by=1, created_date=datetime.datetime.now(),follow_up_date=datetime.datetime.now() + datetime.timedelta(days=7)))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), idea_id=2,
        created_by=1, created_date=datetime.datetime.now(),follow_up_date=datetime.datetime.now() + datetime.timedelta(days=7)))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), idea_id=2,
        created_by=1, created_date=datetime.datetime.now(),follow_up_date=datetime.datetime.now() + datetime.timedelta(days=7)))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), idea_id=2,
        created_by=1, created_date=datetime.datetime.now(),follow_up_date=datetime.datetime.now() + datetime.timedelta(days=7)))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), idea_id=2,
        created_by=1, created_date=datetime.datetime.now(),follow_up_date=datetime.datetime.now() + datetime.timedelta(days=7)))
        ideanotes.append(IdeaNotes(title=lorem.sentence(), description=lorem.paragraph(), is_active=random.randrange(0, 1), idea_id=2,
        created_by=1, created_date=datetime.datetime.now(),follow_up_date=datetime.datetime.now() + datetime.timedelta(days=7)))
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
    except ValueError:
        log.error("Creating mood: %s", ValueError)
        # except ValueError:
#     log.error("Creating Ideas: %s", ValueError)
        #print(type(inst)) 
        print(db.error)
        db.session.rollback()
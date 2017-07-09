from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from flask_appbuilder.actions import action
from app import appbuilder, db
from flask_appbuilder.views import MasterDetailView
from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count, aggregate_sum, aggregate_avg
from flask_login import LoginManager, UserMixin, login_required
from flask import g
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction
import calendar
from .models import Note, Tags, Mood, Idea, IdeaNotes
# from .models import JobNoteStatus, JobTitle, Job, JobNotes
from wtforms import validators
from wtforms.fields import TextField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
import datetime
from flask_appbuilder.fieldwidgets import Select2AJAXWidget, Select2SlaveAJAXWidget, Select2Widget
from flask_appbuilder.fields import AJAXSelectField
from flask_appbuilder.widgets import FormHorizontalWidget, FormInlineWidget, FormVerticalWidget

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""


def pre_fill_db():
    try:
        db.session.add(Mood(mood_name='Positive'))
        db.session.add(Mood(mood_name='Neutral'))
        db.session.add(Mood(mood_name='Negative'))
        db.session.add(Mood(mood_name='Mixed'))
        db.session.add(Tags(tag_name='Unknown'))
        db.session.add(Tags(tag_name='Work'))
        db.session.add(Tags(tag_name='Life'))
        db.session.add(Tags(tag_name='Fun'))
        # db.session.add(JobNoteStatus(status = 'Applied'))
        # db.session.add(JobNoteStatus(status = 'Follow Up'))
        # db.session.add(JobNoteStatus(status = 'Interview - Phone'))
        # db.session.add(JobNoteStatus(status = 'Interview - In Persone'))
        # db.session.add(JobNoteStatus(status = 'Offer-Negotiation'))
        # db.session.add(JobNoteStatus(status = 'Offer-Rejected'))
        # db.session.add(JobNoteStatus(status = 'Offer - Accepted'))
        # db.session.add(JobNoteStatus(status = 'Close'))
        db.session.commit()
    except:
        db.session.rollback()

pre_fill_db()


class IdeaNotesGeneralView(ModelView):
    datamodel = SQLAInterface(IdeaNotes)

    label_columns = {'idea_group': 'idea'}
    list_columns = ['title', 'is_active','created_date','idea_group']

    base_order = ('created_date', 'desc')

    show_fieldsets = [
        ('Summary', {'fields': ['title','description','follow_up_date','idea_group']}),
        (
            'Idea Note Details',
            {'fields': ['is_active','created_date'], 'expanded': False}),
    ]

    add_fieldsets = [
        ('Summary', {'fields': ['title','description','follow_up_date','idea_group']}),
        (
            'Idea Note Details',
            {'fields': ['is_active','created_date'], 'expanded': False}),
        ]

    edit_fieldsets = [
        ('Summary', {'fields': ['title','description','follow_up_date','idea_group']}),
        (
            'Idea Note Details',
            {'fields': ['is_active','created_date'], 'expanded': False}),
        ]



class IdeaMasterView(MasterDetailView):
    datamodel = SQLAInterface(Idea)
    related_views = [IdeaNotesGeneralView]


class IdeaGeneralView(ModelView):
    datamodel = SQLAInterface(Idea)
    related_views = [IdeaNotesGeneralView]



class MoodModelView(ModelView):
    datamodel = SQLAInterface(Mood)

class TagsModelView(ModelView):
    datamodel = SQLAInterface(Tags)


# function to get the currently logged in user
# user to set created_by in multiple tables
# also to filter by on charts and views
def get_user():
    return g.user.id

class NoteModelView(ModelView):
    datamodel = SQLAInterface(Note)
    base_filters = [['created_by', FilterEqualFunction, get_user]]
    base_order = ('created_date', 'desc')
    # related_views = [MoodModelView, TagsModelView]
    list_columns = ['mood','tags','created_date','created_by']
    show_fieldsets = [
        ('Summary', {'fields': ['mood','tags','my_note']}),
        (
            'Note Details',
            {'fields': ['created_date'], 'expanded': False}),
    ]

    add_fieldsets = [
        ('Summary', {'fields': ['mood','tags','my_note']}),
        (
            'Note Details',
            {'fields': ['created_date'], 'expanded': False}),
    ]

    edit_fieldsets = [
        ('Summary', {'fields': ['mood','tags','my_note']}),
        (
            'Note Details',
            {'fields': ['created_date'], 'expanded': False}),
    ]

# class JobNotesModelView(ModelView):
#     datamodel = SQLAInterface(JobNotes)
#     related_views = [JobNoteStatus]

# class JobTitleModelView(ModelView):
#     datamodel = SQLAInterface(JobNoteStatus)
#     related_views = [JobNotesModelView]

# class JobModelView(ModelView):
#     datamodel = SQLAInterface(Job)
#     related_views = [JobTitleModelView]
#     base_filters = [['created_by', FilterEqualFunction, get_user]]
#     # base_order = ('created_date', 'dsc')
#     list_columns = ['Title','created_date','created_by','tags']        

# class JobNotesStatusModelView(ModelView):
#     datamodel = SQLAInterface(JobNoteStatus)
#     related_views = [JobTitleModelView]


# class GroupModelView(ModelView):
#     datamodel = SQLAInterface(Mood)
#     related_views = [NoteModelView]
#     search_columns = ['mood_name']



class NoteChartView(GroupByChartView):
    datamodel = SQLAInterface(Note)
    chart_title = 'Grouped Notes'
    label_columns = NoteModelView.label_columns
    chart_type = 'ColumnChart' #'ColumnChart' #PieChart'
    base_filters = [['created_by', FilterEqualFunction, get_user]]

    definitions = [
        {
            'label': 'Word Count by User',
            'group': 'created_by',
            'series': [(aggregate_sum, 'word_count')]
        },
        {
            'label': 'Word Count by Mood',
            'group': 'mood_id',
            'series': [(aggregate_sum, 'word_count')]
        },
        # {
        #     'label': 'Word Count by Tags',
        #     'group': 'tags_id',
        #     'series': [(aggregate_sum, 'word_count')]
        # },
        {
            'label': 'Character Count by User',
            'group': 'created_by',
            'series': [(aggregate_sum, 'text_count')]
        },
        {
            'label': 'Character Count by Mood',
            'group': 'mood_id',
            'series': [(aggregate_sum, 'text_count')]
        },
        # {
        #     'label': 'Character Count by Tags',
        #     'group': 'tags',
        #     'series': [(aggregate_sum, 'text_count')]
        # },
    ]


def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)

def pretty_year(value):
    return str(value.year)


class NoteTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Note)
    base_filters = [['created_by', FilterEqualFunction, get_user]]
    chart_title = 'Grouped Create Date'
    chart_type = 'ColumnChart' #'ColumnChart' 'PieChart''AreaChart'
    label_columns = NoteModelView.label_columns
    definitions = [
        {
            'label': 'Character Count by Month/Year',
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'text_count')]
        },
        {
            'label': 'Character Count by Year',
            'group': 'year',
            'formatter': pretty_year,
            'series': [(aggregate_sum, 'text_count')]
        },
        {
            'label': 'Count of Notes by Month/Year',
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_count, 'id')]
        },
        {
            'label': 'Count of Notes by Year',
            'group': 'year',
            'formatter': pretty_year,
            'series': [(aggregate_count, 'id')]
        }
    ]


# appbuilder.add_view(GroupModelView, "List Groups", icon="fa-folder-open-o", category="Notes", category_icon='fa-envelope')
# appbuilder.add_view(JobModelView, "Jobs", icon="fa-comment", category="Jobs", category_icon='fa-comment')
# appbuilder.add_separator("Jobs")

appbuilder.add_view(IdeaMasterView, "Update Ideas", icon="fa-folder-open-o", category="Ideas")
appbuilder.add_separator("Ideas")
appbuilder.add_view(IdeaGeneralView, "List of Ideas", icon="fa-folder-open-o", category="Ideas")
appbuilder.add_view(IdeaNotesGeneralView, "List Notes", icon="fa-envelope", category="Ideas")



appbuilder.add_view(NoteModelView, "Notes", icon="fa-comment", category="Thoughts", category_icon='fa-comment')
appbuilder.add_separator("Thoughts")
appbuilder.add_view(TagsModelView, "List Tags", icon="fa-tags", category="Thoughts", category_icon='fa-tags')
appbuilder.add_view(MoodModelView, "List Moods", icon="fa-tags", category="Thoughts", category_icon='fa-tags')

appbuilder.add_view(NoteChartView, "Notes Chart", icon="fa-dashboard", category="Charts")
appbuilder.add_view(NoteTimeChartView, "Notes Time Chart", icon="fa-dashboard", category="Charts")

appbuilder.security_cleanup()
"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()



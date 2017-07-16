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

from wtforms import validators
from wtforms.fields import TextField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
import datetime
from flask_appbuilder.fieldwidgets import Select2AJAXWidget, Select2SlaveAJAXWidget, Select2Widget
from flask_appbuilder.fields import AJAXSelectField
from flask_appbuilder.widgets import FormHorizontalWidget, FormInlineWidget, FormVerticalWidget, ListBlock,ListItem,ListThumbnail
from .models import Note, Tags, Mood, Idea, IdeaNotes
# from .models import JobNoteStatus, JobTitle, Job, JobNotes
from app.demodata import pre_fill_db

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""


def date_now(self):
    s = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return s

# function to get the currently logged in user
# user to set created_by in multiple tables
# also to filter by on charts and views
def get_user():
    return g.user.id

class IdeaNotesGeneralView(ModelView):
    datamodel = SQLAInterface(IdeaNotes)
    # related_views = [IdeaGeneralView]
    label_columns = {'idea_group': 'idea'}
    list_columns = ['title', 'is_active','created_date','idea_group']
    list_widget = ListBlock # ListBlock,ListItem,ListThumbnail
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
    base_filters = [['created_by', FilterEqualFunction, get_user]]
    base_order = ('created_date', 'desc')

class IdeaGeneralView(ModelView):
    datamodel = SQLAInterface(Idea)
    related_views = [IdeaNotesGeneralView]
    base_filters = [['created_by', FilterEqualFunction, get_user]]
    list_widget = ListBlock # ListBlock,ListItem,ListThumbnail

class MoodModelView(ModelView):
    datamodel = SQLAInterface(Mood)
    base_filters = [['created_by', FilterEqualFunction, get_user]]

class TagsModelView(ModelView):
    datamodel = SQLAInterface(Tags)
    base_filters = [['created_by', FilterEqualFunction, get_user]]

class NoteModelView(ModelView):
    datamodel = SQLAInterface(Note)
    base_filters = [['created_by', FilterEqualFunction, get_user]]
    base_order = ('created_date', 'desc')
    # related_views = [MoodModelView, TagsModelView]
    list_columns = ['mood','tags','created_date']
    list_widget = ListBlock # ListBlock,ListItem,ListThumbnail
    show_fieldsets = [
        ('Summary', {'fields': ['mood','tags','my_note', 'word_count']}),
        (
            'Note Details',
            {'fields': ['created_date',], 'expanded': False}),
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

def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)

def pretty_year(value):
    return str(value.year)

class NoteChartView(GroupByChartView):
    datamodel = SQLAInterface(Note)
    chart_title = 'Notes Character and Word Counts '
    label_columns = NoteModelView.label_columns
    chart_type = 'PieChart' #'ColumnChart' 'PieChart''AreaChart''LineChart'
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
        #     'group': 'month_year',
        #     'series': [(aggregate_avg, 'word_count'),(aggregate_avg, 'id')]
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
    ]

class NoteTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Note)
    base_filters = [['created_by', FilterEqualFunction, get_user]]
    chart_title = 'Notes by Created Date'
    chart_type = 'AreaChart'  #'ColumnChart' 'PieChart''AreaChart''LineChart'
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
            'series': [(aggregate_count, 'id'),(aggregate_avg, 'word_count')]
        },
        {
            'label': 'Count of Notes by Year',
            'group': 'year',
            'formatter': pretty_year,
            'series': [(aggregate_count, 'id'),(aggregate_avg, 'word_count')]
        }
    ]

class IdeaChartView(GroupByChartView):
    datamodel = SQLAInterface(Idea)
    chart_title = 'Ideas by Status'
    label_columns = IdeaNotesGeneralView.label_columns
    chart_type = 'PieChart' #'ColumnChart' 'PieChart''AreaChart''LineChart'
    base_filters = [['created_by', FilterEqualFunction, get_user]]

    definitions = [
        {
            'label': 'Idea by Status User',
            'group': 'is_active',
            'series': [(aggregate_count, 'id')]
        },
        # {
        #     'label': 'Idea by User',
        #     'group': 'idea_group',
        #     'series': [(aggregate_count, 'id')]
        # },
    ]

class IdeaTimeChartView(GroupByChartView):
    
    datamodel = SQLAInterface(IdeaNotes)
    base_filters = [['created_by', FilterEqualFunction, get_user]]
    chart_title = 'Ideas by Create Date'
    chart_type = 'ColumnChart' #'ColumnChart' 'PieChart''AreaChart''LineChart'
    label_columns = IdeaNotesGeneralView.label_columns
    definitions = [
        {
            'label': 'Character Count by Month/Year',
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_count, 'id')]
        },
        {
            'label': 'Character Count by Month/Year',
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_count, 'idea_id'), (aggregate_count, 'id')]
        },
    ]



# appbuilder.add_view(GroupModelView, "List Groups", icon="fa-folder-open-o", category="Notes", category_icon='fa-envelope')
# appbuilder.add_view(JobModelView, "Jobs", icon="fa-comment", category="Jobs", category_icon='fa-comment')
# appbuilder.add_separator("Jobs")

appbuilder.add_view(NoteModelView, "Notes", icon="fa-comment", category="Thoughts", category_icon='fa-comment')
appbuilder.add_separator("Thoughts")
appbuilder.add_view(IdeaGeneralView, "List of Ideas", icon="fa-folder-open-o", category="Thoughts")
appbuilder.add_separator("Thoughts")
appbuilder.add_view(IdeaMasterView, "Add/Update Ideas", icon="fa-folder-open-o", category="Thoughts")
appbuilder.add_view(IdeaNotesGeneralView, "List Notes", icon="fa-envelope", category="Thoughts")

appbuilder.add_view(NoteChartView, "Notes Chart", icon="fa-dashboard", category="Charts")
appbuilder.add_view(NoteTimeChartView, "Notes Time Chart", icon="fa-dashboard", category="Charts")
appbuilder.add_view(IdeaChartView, "Ideas Chart", icon="fa-dashboard", category="Charts")
appbuilder.add_view(IdeaTimeChartView, "Ideas Time Chart", icon="fa-dashboard", category="Charts")

appbuilder.add_view(TagsModelView, "List Tags", icon="fa-tags", category="Configuration", category_icon='fa-tags')
appbuilder.add_view(MoodModelView, "List Moods", icon="fa-tags", category="Configuration", category_icon='fa-tags')

appbuilder.security_cleanup()

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()
#pre_fill_db()
pre_fill_db()


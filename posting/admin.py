from django.contrib import admin

from posting.models import Letter, Logic, Posting_tuning


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('topic_letter',)
    # list_filter = ('name',)
    search_fields = ('topic_letter',)
    filter_horizontal = ['clients']


@admin.register(Logic)
class LogicAdmin(admin.ModelAdmin):
    list_display = ('data_time_last', 'status_attempts', 'answer_srv_mail')
    list_filter = ('data_time_last',)
    search_fields = ('data_time_last',)


@admin.register(Posting_tuning)
class Posting_tuningAdmin(admin.ModelAdmin):
    list_display = ('data_start','period','data_start')
    list_filter = ('period',)
    search_fields = ('data_start',)



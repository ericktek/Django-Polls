from django.contrib import admin
from .models import Question, Choice
from django.utils import timezone
import datetime

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    def was_published_recently(self, obj):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= obj.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

admin.site.register(Question, QuestionAdmin)
from django.contrib import admin
from django.forms import RadioSelect, CharField

from .forms import QuestionForm
from .models import Question, Test, Testing


class QuestionAdmin(admin.ModelAdmin):
    """Модель для админки вопросов."""

    form = QuestionForm
    search_fields = ('topic', 'question_text')
    radio_fields = {'correct_option': admin.HORIZONTAL}
    fieldsets = (
        (None, {
            'fields': ('moderator', 'topic')
        }),
        ('Вопрос', {
            'fields': ('question_text', 'description')
        }),
        ('Варианты ответа', {
            'fields': ('option_a', 'option_b', 'option_c', 'option_d', 'correct_option')
        }),
        (None, {
            'fields': ('explanation',)
        }),
        (None, {
            'fields': ('data_create', 'data_update')
        }),
    )
    readonly_fields = ('data_create', 'data_update', 'moderator')


# Register models.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Test)
admin.site.register(Testing)

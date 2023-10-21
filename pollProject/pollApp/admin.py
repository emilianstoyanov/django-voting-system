from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "The Poll Mall"
admin.site.site_header = "Voting Admin Area"
admin.site.site_header = "Welcome to our Voting Admin Area"


class ChoiceLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceLine]


admin.site.register(Question, QuestionAdmin)

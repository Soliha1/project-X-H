from django.contrib import admin
from .models import *

class IncorrectInline(admin.StackedInline):
    model=Incorrect
    extra = 1


@admin.register(Correct)
class correctAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)
    inlines = [IncorrectInline,]

@admin.register(Incorrect)
class incorrectAdmin(admin.ModelAdmin):
    list_display = ('word', 'correct',)
    search_fields =  ('word', 'correct',)

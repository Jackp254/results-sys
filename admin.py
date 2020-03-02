from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('Code','Title','Cat','Exam','Total','Grade')
admin.site.register(Student,StudentAdmin)

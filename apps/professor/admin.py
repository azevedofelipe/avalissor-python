from django.contrib import admin
from .models import Course, Tag, Professor, ReviewProfessor

# Register your models here.
admin.site.register(Tag)
admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(ReviewProfessor)

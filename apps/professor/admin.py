from django.contrib import admin
from .models import Tag, Professor, ReviewProfessor

# Register your models here.
admin.site.register(Tag)
admin.site.register(Professor)
admin.site.register(ReviewProfessor)

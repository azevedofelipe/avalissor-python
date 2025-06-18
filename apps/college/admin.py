from django.contrib import admin
from .models import College, Campus, ReviewCampus

# Register your models here.
admin.site.register(College)
admin.site.register(Campus)
admin.site.register(ReviewCampus)

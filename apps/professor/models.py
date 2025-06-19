from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.college.models import Campus

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)

class Course(models.Model):
    # Maybe normalize names in future if needed
    name = models.CharField(max_length=50, unique=True)

class Professor(models.Model):
    campus = models.ForeignKey(Campus,on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course,related_name='professor')
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class ReviewProfessor(models.Model):
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE, related_name='professor')
    course = models.ForeignKey(Course,on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    comment = models.CharField(max_length=300)
    tags = models.ManyToManyField(Tag, related_name="professors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.professor.campus.name) + " - " + str(self.professor.name) + " - " + str(self.rating)

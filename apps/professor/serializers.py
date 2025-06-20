from rest_framework import fields, serializers
from apps.professor.models import Course, Tag, Professor, ReviewProfessor


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id","name"]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id","name"]

class ProfessorSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField()
    rating_count = serializers.IntegerField()
    # Many to Many fields require many=True
    courses = CourseSerializer(read_only=True, many=True)

    class Meta:
        model = Professor
        fields = ["id","campus","courses","name","avg_rating","rating_count","created_at","updated_at"]

class ProfessorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ["id","name"]

class ReviewProfessorSerializer(serializers.ModelSerializer):
    professor = ProfessorMiniSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    
    class Meta:
        model = ReviewProfessor
        fields = ["id","rating","professor","course", "comment","tags","created_at","updated_at"]


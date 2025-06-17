from rest_framework import fields, serializers

from apps.college.models import Campus, College, ReviewCampus

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ["id","name","tipo","created_at","updated_at"]

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ["id", "name","location","created_at","updated_at"]
        read_only_fields = ["college"]

class CampusReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewCampus
        fields = ["id","rating","comment","created_at","updated_at"]
        read_only_fields = ["campus"]

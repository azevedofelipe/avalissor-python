from rest_framework import fields, serializers

from apps.college.models import Campus, College, ReviewCampus

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ["name","tipo","created_at","updated_at"]


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ["college","name","location","created_at","updated_at"]

class CampusReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewCampus
        fields = ["campus","rating","comment","created_at","updated_at"]

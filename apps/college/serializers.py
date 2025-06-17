from rest_framework import fields, serializers

from apps.college.models import Campus, College

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ["name","tipo","created_at","updated_at"]


class CampusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campus
        fields = ["college","name","location","created_at","updated_at"]

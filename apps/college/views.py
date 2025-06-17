from django.shortcuts import render
from rest_framework import permissions, viewsets
from apps.college.models import Campus, College
from django.contrib.auth.models import User
from apps.college.serializers import CollegeSerializer, CampusSerializer

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all().order_by('-updated_at')
    serializer_class = CollegeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CampusViewSet(viewsets.ModelViewSet):
    serializer_class = CampusSerializer

    def get_queryset(self):
        return Campus.objects.filter(college=self.kwargs['college_pk'])
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

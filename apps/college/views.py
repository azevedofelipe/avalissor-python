from rest_framework import permissions, viewsets
from apps.college.models import Campus, College, ReviewCampus
from apps.college.serializers import CampusReviewSerializer, CollegeSerializer, CampusSerializer
from django.shortcuts import get_object_or_404

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all().order_by('-updated_at')
    serializer_class = CollegeSerializer
    permission_classes = [permissions.AllowAny]

class CampusViewSet(viewsets.ModelViewSet):
    serializer_class = CampusSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Campus.objects.filter(college=self.kwargs['college_pk'])

    def perform_create(self, serializer):
        college = get_object_or_404(College, pk=self.kwargs['college_pk'])
        serializer.save(college=college)

class CampusReviewViewSet(viewsets.ModelViewSet):
    serializer_class = CampusReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ReviewCampus.objects.filter(campus=self.kwargs['campus_pk'])

    def perform_create(self,serializer):
        campus = get_object_or_404(Campus, pk=self.kwargs['campus_pk'])
        serializer.save(campus=campus)

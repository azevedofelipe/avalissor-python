from rest_framework import permissions, viewsets
from apps.professor.models import Tag, Professor, ReviewProfessor
from django.shortcuts import get_object_or_404

from apps.professor.serializers import ProfessorSerializer, ReviewProfessorSerializer, TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all().order_by("-updated_at")
    serializer_class = ProfessorSerializer
    permission_classes = [permissions.AllowAny]

class ProfessorReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewProfessorSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ReviewProfessor.objects.filter(professor=self.kwargs['professor_pk'])

    def perform_create(self, serializer):
        professor = get_object_or_404(Professor, pk=self.kwargs['professor_pk'])
        serializer.save(professor=professor)






"""
URL configuration for avalissor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter 

from apps.college import views as college_views
from apps.professor import views as professor_views


router = DefaultRouter()
router.register(r"colleges", college_views.CollegeViewSet, basename="college")

colleges_router = NestedSimpleRouter(router, r'colleges',lookup='college')
colleges_router.register(r'campuses',college_views.CampusViewSet, basename='college-campuses')

campuses_router = NestedSimpleRouter(colleges_router,r'campuses',lookup='campus')
campuses_router.register(r'reviews',college_views.CampusReviewViewSet, basename='campus-reviews')

router.register(r"professors",professor_views.ProfessorViewSet, basename="professor")
router.register(r"tags",professor_views.TagViewSet, basename='tag')

professor_router = NestedSimpleRouter(router, r'professors', lookup='professor')
professor_router.register(r'reviews',professor_views.ProfessorReviewViewSet, basename='professor-reviews')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/',include(colleges_router.urls)),
    path('api/',include(campuses_router.urls)),
    path('api/',include(professor_router.urls)),
]

from django.urls import path

from app import views

urlpatterns = [
    path("", views.Study_management, name="Study_management"),
    path('Study_View/<int:id>/', views.Study_View, name="StudyView"),
    path('Study_Edit', views.Study_Edit, name="StudyEdit"),
    path("Add_study",views.Add_study,name="Add_study"),
    path('Study_Edit/<int:id>/',views.Study_Edit,name="StudyEdit"),
    path("StudyDelete/<int:id>/",views.StudyDelete,name="StudyDelete"),
    path("delete_study",views.delete_study,name="delete_study")
]

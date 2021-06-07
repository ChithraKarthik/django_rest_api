from django.urls import path
from cbv_firstapp import views


urlpatterns = [
    path("student/", views.StudentListall.as_view()),
    path("mark/",views.MarkListall.as_view()),
    path("student/<int:pk>/", views.StudentListDetail.as_view()),
    path("mark/<int:pk>/",views.MarkListDetail.as_view()),

]

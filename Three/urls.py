from django.conf.urls import url

from Three import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^getgrade/', views.get_grade),
    url(r'^getstudent/', views.get_student),
]
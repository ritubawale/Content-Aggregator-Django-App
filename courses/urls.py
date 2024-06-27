from django.urls import path
import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
]

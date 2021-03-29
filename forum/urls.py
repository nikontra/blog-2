from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum_home'),
    path('practice', views.practice, name="practice"),
    path('lesson', views.lesson, name='lesson'),
    path('about', views.about, name='about'),
    path('example/test/Some', views.some, name='some')
]

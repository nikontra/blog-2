from django.urls import path
from . import views as userViews

urlpatterns = [
    path('', userViews.register, name = 'reg'),
]

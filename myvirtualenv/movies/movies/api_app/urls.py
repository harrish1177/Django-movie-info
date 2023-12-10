from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
path('movie/', views.get_data),
]
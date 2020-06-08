from django.contrib import admin
from django.urls import path,include
from .views import UpdateModelListAPIView, UpdateModelDetailAPIView

urlpatterns = [
    path('',UpdateModelListAPIView.as_view()), #api/update -> List /create
    path('<int:id>/',UpdateModelDetailAPIView.as_view()),
    ]

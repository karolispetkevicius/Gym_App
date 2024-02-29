from django.urls import path
from programbuilder.views import TestView
from django.contrib import admin

urlpatterns = [
    path('api/test/', TestView.as_view()),
    path('admin/', admin.site.urls)
]
from _operator import index

from django.contrib import admin
from django.urls import path
from lesson.views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
  ]

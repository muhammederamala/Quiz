"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from questions.views import (

    home, quiz_list_view, add_quiz_view, delete_quiz_view,

    )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("quiz_list_view/",quiz_list_view, name="quiz_list_view"),
    path("add_quiz_view/", add_quiz_view, name="add_quiz_view"),
    path("delete_quiz_view/<int:new_quiz_id>/", delete_quiz_view, name="delete_quiz_view"),
]

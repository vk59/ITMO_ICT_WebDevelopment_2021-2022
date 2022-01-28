"""LW2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views

from conference.views import ConferenceList, review
from conference import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name='conf/login.html'), name="login"),
    path("register", views.register, name="register"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("regtoconf/", views.conf_for_reg, name='regtoconf'),
    path("regtoconf/<int:pk>/", views.registration_to_conf, name='registration_to_conf'),

    # path('conferences', views.Conference.as_view(template_name='conf/conferences.html'), name='conferences')
    path('accounts/', include('django.contrib.auth.urls')),
    path('', ConferenceList.as_view(), name="home"),
    path('newreview/', review, name="newreview"),
    path('members/', views.members_of_conference, name="members")
]

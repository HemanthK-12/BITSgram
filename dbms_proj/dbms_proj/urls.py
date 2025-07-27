"""
URL configuration for dbms_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from social_media.views import index

admin.site.site_header = "BITSBuzz"
admin.site.site_title = "BITSBuzz Database Portal"
admin.site.index_title = "Welcome to BITSBuzz Database Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social_media/',index),
    path('', admin.site.urls),
]

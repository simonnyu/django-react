"""django_react URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from hello.views import hello_world
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

# 不需要以「語言」開頭的 URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('react',TemplateView.as_view(template_name='index.html'))]
# 設置以「語言」開頭的 URL 如 /en/demo 或是 /zh-TW/demo
urlpatterns += i18n_patterns(
    path('', include('hello.urls')),
)

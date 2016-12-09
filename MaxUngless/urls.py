"""MaxUngless URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Blog import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^topics/$', views.view_topics),
    url(r'^topics/(?P<user_topic>.+)/', views.topic),
    url(r'^posts/(?P<post_slug>.+)/', views.view_post),
    url(r'^work/', TemplateView.as_view(template_name="Blog/work.html")),
    url(r'^contact/', TemplateView.as_view(template_name="Blog/contact.html")),
]

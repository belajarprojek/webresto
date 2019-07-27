from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', include('contact.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^profil/', include('profil.urls')),
    url(r'^$', views.index),
]

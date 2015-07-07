from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^image/', views.image, name="views.uploader.image"),
]

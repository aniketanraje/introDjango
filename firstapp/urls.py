from django.urls import path

from . import views

urlpatterns = [
    path("http-response/", views.hello, name="hello"),
    path("", views.hello_from_html, name="html"),
    path("add/", views.add, name="add"),

]

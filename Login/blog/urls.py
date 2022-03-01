from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="Blog"),
    path('<str:slug>', views.blogPost, name="blogPost"),
]
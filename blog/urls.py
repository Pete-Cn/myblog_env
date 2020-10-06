from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000
    path('',views.blog_list,name="blog_list"),
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>',views.blog_with_type, name="blog_with_type"),
]
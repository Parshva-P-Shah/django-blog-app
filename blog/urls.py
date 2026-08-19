from django.urls import path
from . import views
urlpatterns = [
    path('', views.Blog_list, name="blog_list"),
    path('blog/<int:blog_id>/', views.Blog_page, name="blog_page"),
    path('create/', views.Blog_create, name="blog_create"),
    path('<int:blog_id>/edit/', views.Blog_edit, name="blog_edit"),
    path('<int:blog_id>/delete/', views.Blog_delete, name="blog_delete"),
    path('profile/<str:username>/', views.Profile, name="profile"),
    path('register/', views.Register, name="register"),
]
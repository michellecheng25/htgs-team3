from django.urls import path
from forum import views


urlpatterns = [
    path("", views.all_posts, name="all_posts"),
    path("add-post", views.add_post, name="add-post"),
    path("get-post/<postId>", views.get_post, name="get-post"),
]

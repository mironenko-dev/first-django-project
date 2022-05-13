from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, EditView, DeletePostView


urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_details"),
    path('addpost/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', EditView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post')
]






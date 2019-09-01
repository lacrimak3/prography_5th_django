from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
    path('', views.mainView, name='mainview'),
    path('<int:pk>/', views.detailView, name='detail'),
    path('create/', views.createPost, name='createpost'),
    path('<int:pk>/delete/', views.deletePost, name='deletepost'),
    path('<int:pk>/update/', views.updatePost, name='updatepost'),    
]
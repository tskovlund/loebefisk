from django.urls import path

from . import views


app_name = 'gallery'
urlpatterns = [
    path('', views.LatestView.as_view(), name='latest'),
    path('<int:pk>/', views.DetailView.as_view(), name='post'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('random/', views.RandomView.as_view(), name='random'),
]

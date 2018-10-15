from django.urls import path

from . import views


app_name = 'gallery'
urlpatterns = [
    path('', views.LatestView.as_view(), name='latest'),
    path('<int:pk>/', views.DetailView.as_view(), name='post'),
    path('list/', views.IndexView.as_view(), name='index'),
]

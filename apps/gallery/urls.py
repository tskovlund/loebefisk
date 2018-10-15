from django.urls import path

from . import views


app_name = 'gallery'
urlpatterns = [
    path('', views.LatestView.as_view(), name='latest'),
    path('p/<int:pk>/', views.PreviousView.as_view(), name='previous'),
    path('n/<int:pk>/', views.NextView.as_view(), name='next'),
    path('<int:pk>/', views.DetailView.as_view(), name='post'),
    path('list/', views.IndexView.as_view(), name='index'),
]

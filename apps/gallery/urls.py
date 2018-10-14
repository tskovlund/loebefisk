from django.urls import path

from . import views


app_name = 'gallery'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PostView.as_view(), name='post'),
]

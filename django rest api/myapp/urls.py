from django.urls import path
from myapp import views
urlpatterns = [
    path('api_list/', views.api_list, name='api_list'),
    path('api_detail/<int:pk>/', views.api_detail, name='api_detail'),
   
]
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home_page'),
    path('properties/', views.properties, name='properties_page'),
    path('properties/<slug:slug>/', views.properties_detail, name='properties_detail'),
    path('contact_us/', views.contact_us, name='contact_us'),
   
]
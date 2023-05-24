from django.urls import path 
from . import views 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [ 
    path('', views.index),
    path('about/', views.index1),
    path('contact/', views.contact),
    path('register/', views.register, name="register"),
    # path('search/', views.search, name="search"),
    path('login/', LoginView.as_view(template_name='page/login.html'), name='login'),
   
   path('logout/',LogoutView.as_view(next_page='/'),name='logout'),
    
]

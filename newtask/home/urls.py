from django.contrib import admin
from django.urls import path
from . import views
# from .views import SearchResultsView

app_name = 'home'


urlpatterns = [
    path('registration/', views.registration, name='registration'),    
    path('login/', views.login, name='login'),  
    path('lobby/', views.lobby, name='lobby'),  
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    path('user-add/', views.AddUser, name='add-user'),

]
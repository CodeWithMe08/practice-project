from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('add_user/', views.add_user, name='add-user'),
    path('show_record/', views.show_record, name='show-record'),

]
from django.urls import path
from . import views

app_name='drugs'

urlpatterns = [
    path('', views.ApiOverView, name='home'),
    #Create view
    path('ings/create/', views.add_ing, name='add_ing'),
    path('drugs/create/', views.add_drug, name='add_drug'),
    #Retrive view
    path('ings/', views.view_ings, name='view_ings'),
    path('drugs/', views.view_drugs, name='view_drugs'),
    #Update view
    path('ings/update/<int:pk>/', views.update_ing, name='update_ing'),
    path('drugs/update/<int:pk>', views.update_drug, name='update_drug'),
    #Delete view
    path('ings/<int:pk>/delete', views.delete_ing, name='delete_ing'),
    path('drugs/<int:pk>/delete', views.delete_ing, name='delete_ing'),
]
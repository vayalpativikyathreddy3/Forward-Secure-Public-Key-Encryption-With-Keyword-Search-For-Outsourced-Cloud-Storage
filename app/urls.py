from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('datasenderregister/', views.datasenderregister, name='datasenderregister'),
    path('datasenderlogin/', views.datasenderlogin, name='datasenderlogin'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('datareceiverregister/', views.datareceiverregister, name='datareceiverregister'),
    path('datareceiverlogin/', views.datareceiverlogin, name='datareceiverlogin'),
    path('cloudlogin/', views.cloudlogin, name='cloudlogin'),
    path('uploadfile/', views.uploadfile, name='uploadfile'),
    path('viewmyfiles/', views.viewmyfiles, name='viewmyfiles'),
    path('searchfile/', views.searchfile, name='searchfile'),
    path('requestfile/<int:id>/', views.requestfile, name='requestfile'),
    path('viewallfiles/', views.viewallfiles, name='viewallfiles'),
    path('viewrequestedfiles/', views.viewrequestedfiles, name='viewrequestedfiles'),
    path('acceptrequestfile/<int:id>/', views.acceptrequestfile, name='acceptrequestfile'),
    path('viewfiletransactions/', views.viewfiletransactions, name='viewfiletransactions'),
    path('viewresponses/', views.viewresponses, name='viewresponses'),
    path('download/<int:id>/', views.download, name='download'),


    





]

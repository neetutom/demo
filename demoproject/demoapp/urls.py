from django.urls import path

from . import views


urlpatterns = [
    path('', views.Homepage, name='homepage'),
    path('about/', views.About, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('details/', views.details, name='details'),
    path('thank-you/', views.thankyou, name='thanyou'),

]


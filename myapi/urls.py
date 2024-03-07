from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='account-list'),
    path('register/<int:pk>/', RegisterAPIView.as_view(), name='account-detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('get_taxi/', GetTaxiFormListCreateView.as_view(), name='yourmodel-list-create'),
    path('get_taxi/<int:pk>/', GetTaxiFormRetrieveUpdateDestroyView.as_view(), name='yourmodel-retrieve-update-destroy'),
    path('drivers/', DriverListCreateView.as_view(), name='driver-list-create'),
    path('drivers/<int:pk>/', DriverDetailView.as_view(), name='driver-detail'),
    path("emailNewRegistratinos/", SendmailRegistrations.as_view(), name = "emailNewRegistratinos"),
    path('contact/', ContactNameListCreateView.as_view(), name='your-model-list-create'),
    path('contact/<int:pk>/', ContactNameRetrieveUpdateDestroyView.as_view(), name='your-model-retrieve-update-destroy'),

    path('upload_invoice/', upload_invoice, name='upload_invoice'),
     path('get_invoices/', get_invoices, name='get_invoices'),

   

]



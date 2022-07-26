from django.urls import path
from country import views

urlpatterns = [
    path('country/', views.country_list),
    path('countrydetail/<int:pk>/', views.country_detail),
]
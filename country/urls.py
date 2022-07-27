from django.urls import path
from country import views

urlpatterns = [
    path('country/', views.country_list),
    path('country-detail/<int:id>/', views.country_detail),
]
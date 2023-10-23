from django.urls import path
from . import views
from .views import menuview, bookingview, menuitemsview, singlemenuitemsview
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', menuview.as_view()),
    path('menu-items/', menuitemsview.as_view()),
    path('menu-items/<int:pk>', singlemenuitemsview.as_view()),
    path('booking-data/', bookingview.as_view()),
    path('api-token-auth/', obtain_auth_token),
]

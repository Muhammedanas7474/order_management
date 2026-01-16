from django.urls import path
from .views import RegisterAPIView, ProductAPIView, OrderAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('products/', ProductAPIView.as_view()),
    path('orders/', OrderAPIView.as_view()),
]

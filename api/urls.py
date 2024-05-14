from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegistrationAPIView, UserLoginAPIView, ParagraphListCreateAPIView, ParagraphDetailAPIView,ParagraphSearchView

urlpatterns = [
    # User registration and login endpoints
    path('register/', UserRegistrationAPIView.as_view(), name='user_register'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),

    # API endpoints for paragraphs
    path('paragraphs/', ParagraphListCreateAPIView.as_view(), name='paragraph_list_create'),
    path('paragraphs/<int:pk>/', ParagraphDetailAPIView.as_view(), name='paragraph_detail'),
    path('search/', ParagraphSearchView.as_view(), name='paragraph_search'),

    # Obtain authentication token endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # For DRF Token Auth
]


"""
URL configuration for webservices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dogapp.views import dog_service
from dogapp.views import rest_get_dog
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from dogapp.schema import schema
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from dogapp.views import DogDetailAPIView
from dogapi.views import DogListCreateView, DogRetrieveUpdateDestroyView, BreedListCreateView, BreedRetrieveUpdateDestroyView
from dogapi.controllers import DogList, DogDetail



urlpatterns = [
    path('admin/', admin.site.urls),
    path('soap/dogservice/', dog_service),
    path('rest/dog/<int:dog_id>/', rest_get_dog, name='rest_get_dog'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rest/dog/<int:pk>/', DogDetailAPIView.as_view(), name='rest_get_dog'),
    path('dogs/', DogListCreateView.as_view(), name='dog-list-create'),
    path('dogs/<int:pk>/', DogRetrieveUpdateDestroyView.as_view(), name='dog-detail'),
    path('breeds/', BreedListCreateView.as_view(), name='breed-list-create'),
    path('breeds/<int:pk>/', BreedRetrieveUpdateDestroyView.as_view(), name='breed-detail'),
    path('dogs/', DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
]

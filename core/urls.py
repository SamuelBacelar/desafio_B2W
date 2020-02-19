from django.urls import include, path
from .views import PlanetView


urlpatterns = [
    path('users/', include('accounts.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    #path('planets/', PlanetView.as_view())
]
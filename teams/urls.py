from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teams import views

router = DefaultRouter()

urlpatterns = [
    path('teams/', include(router.urls)),
    path('teams/players/', views.PlayerViewSet.as_view({'get': 'list'}), name='players'),
    path('teams/players/<int:pk>', views.PlayerViewSet.as_view({'get': 'retrieve'}), name='players'),
]

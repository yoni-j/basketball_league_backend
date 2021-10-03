from django.urls import path, include
from rest_framework.routers import DefaultRouter
from league import views

router = DefaultRouter()

urlpatterns = [
    path('league/', include(router.urls)),
    path('league/leagues_list', views.GetLeagues.as_view(), name='leagues_list'),
    path('league/scoreboard/<int:pk>', views.GetScoreBoard.as_view({'get': 'retrieve'}), name='scoreboard'),
]

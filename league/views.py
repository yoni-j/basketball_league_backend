from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from league.models import League, Game, Round
from league.serializers import GameSerializer, RoundSerializer, LeagueSerializer
from teams.models import Coach, Player
from teams.serializers import PlayersListSerializer, PlayerDetailsSerializer

from teams.permissions import IsCoach


class GetScoreBoard(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = League.objects.all()
        league = get_object_or_404(queryset, pk=pk)
        serializer = LeagueSerializer(league)
        return Response(serializer.data)

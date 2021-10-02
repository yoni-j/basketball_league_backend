from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from teams.models import Coach, Player
from teams.serializers import PlayersListSerializer, PlayerDetailsSerializer
from teams.permissions import IsCoach


class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsCoach]

    def list(self, request):
        coach = Coach.objects.get(pk=self.request.user.pk)
        queryset = coach.team.players.all()
        serializer = PlayersListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Player.objects.all()
        player = get_object_or_404(queryset, pk=pk)
        serializer = PlayerDetailsSerializer(player)
        return Response(serializer.data)


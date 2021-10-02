from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from fixtures.set_data import set_data
from league.models import League
from teams.models import User, Coach, Player
import json


class BaseApiTestCase(APITestCase):
    def setUp(self):
        set_data()
        coach_user = User.objects.get(username="coach_Team1")
        coach_user.set_password("coachpass")
        coach_user.save()
        self.coach = Coach.objects.get(user=coach_user)
        player_user = User.objects.get(username="player1_Team1")
        self.player = Player.objects.get(user=player_user)
        login_resp = self.client.post(f'/api-token-auth/', data={"username": "coach_Team1", "password": "coachpass"})
        self.token = login_resp.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')


class PlayersApiTestCase(BaseApiTestCase):
    def test_scoreboard(self):
        url = reverse('scoreboard', args=[League.objects.all()[0].pk])
        response = self.client.get(url)
        content = json.loads(response.content)
        self.assertEqual(content["name"], "Champions League")
        self.assertEqual(len(content["rounds"]), 4)
        self.assertEqual(len(content["rounds"][0]["games"]), 8)

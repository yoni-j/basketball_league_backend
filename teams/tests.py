import json

from rest_framework.test import APITestCase
from fixtures.set_data import set_data
from django.urls import reverse
from teams.models import User, Coach, Player


# Create your tests here.


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
    def test_players_list(self):
        url = reverse('players')
        response = self.client.get(url)
        content = json.loads(response.content)
        self.assertEqual(content[0]["user"], "player1_Team1")

    def test_player_details(self):
        url = reverse('players', args=[self.player.pk])
        response = self.client.get(url)
        content = json.loads(response.content)
        self.assertIn("user", content)
        self.assertIn("height", content)
        self.assertIn("avg_score", content)
        self.assertIn("played_games", content)

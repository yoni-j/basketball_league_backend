import random

from django.db.models import Sum

from league.models import League, Round, Game, GameTeam, GamePlayer
from teams.models import Team, User, Player, Coach
from league.choices import ResultChoices


def set_data():
    reset()
    create_superuser()
    create_teams()
    create_players_and_coaches()
    create_league()
    create_rounds()
    create_all_rounds_games()


def reset():
    Team.objects.all().delete()
    User.objects.all().delete()
    Round.objects.all().delete()
    Game.objects.all().delete()
    Player.objects.all().delete()
    GameTeam.objects.all().delete()
    GamePlayer.objects.all().delete()
    League.objects.all().delete()


def create_superuser():
    User.objects.create_user(username='admin',
                             email='admin@admin.com',
                             password='admin1234',
                             is_staff=True,
                             is_active=True,
                             is_superuser=True
                             )


def create_teams():
    teams = []
    for i in range(1, 17):
        teams.append(Team(name=f"Team{i}"))
    Team.objects.bulk_create(teams)


def create_players_and_coaches():
    users = []
    players = []
    for team in Team.objects.all():
        creator = create_players(team)
        users += creator[0]
        players += creator[1]
        create_coach(team)
    User.objects.bulk_create(users)
    Player.objects.bulk_create(players)



def create_players(team):
    users = []
    players = []
    for i in range(1, 10):
        user = User(username=f"player{i}_{team.name}", password="playerpassword")
        users.append(user)
        players.append(Player(user=user, team=team, height=190 + i))
    return users, players

def create_coach(team):
    user = User.objects.create(username=f"coach_{team.name}", password="coachpass")
    Coach.objects.create(user=user, team=team)


def create_league():
    League.objects.create(name="Champions League")


def create_rounds():
    league = League.objects.get(name="Champions League")
    rounds = []
    for stage in range(1,5):
        rounds.append(Round(stage=stage, league=league))
    Round.objects.bulk_create(rounds)


def create_all_rounds_games():
    league = League.objects.get(name="Champions League")
    for round in league.rounds.all():
        create_round_games(round)


def create_round_games(round):
    games = []
    game_teams = []
    teams = list(get_stage_teams(round.stage))
    for i in range(0, 16, round.stage ** 2):
        if teams:
            games_creator = create_game(round, teams[:2])
            games.append(games_creator[0])
            game_teams += [games_creator[1], games_creator[2]]
            del teams[:2]
    Game.objects.bulk_create(games)
    GameTeam.objects.bulk_create(game_teams)
    associate_players_to_games(round)
    set_games_win_team(round)


def create_game(round, teams):
    game = Game(round=round)
    gt1 = GameTeam(game=game, team=teams[0])
    gt2 = GameTeam(game=game, team=teams[1])
    return game, gt1, gt2


def associate_players_to_games(round):
    game_players = []
    for gt in GameTeam.objects.filter(game__round=round).all():
        players = gt.team.players.all()[:8]
        for player in players:
            game_players.append(GamePlayer(player=player, game=gt.game, score=random.randint(1, 20)))
    GamePlayer.objects.bulk_create(game_players)


def set_games_win_team(round):
    for game in Game.objects.filter(round=round).all():
        teams = game.teams.all()
        teams1, teams2 = GameTeam.objects.get(pk=teams[0].pk), GameTeam.objects.get(pk=teams[1].pk)
        team1_score = GamePlayer.objects.filter(game=game, player__team=teams[0].team).aggregate(Sum('score'))[
            'score__sum']
        team2_score = GamePlayer.objects.filter(game=game, player__team=teams[1].team).aggregate(Sum('score'))[
            'score__sum']
        if team1_score > team2_score:
            teams1.result = "Won"
            teams2.result = "Lost"
        else:
            teams1.result = "Lost"
            teams2.result = "Won"
        teams1.save()
        teams2.save()

        game.save()


def get_stage_teams(stage):
    if stage == 1:
        return Team.objects.all()
    else:
        return [gt.team for gt in GameTeam.objects.filter(game__round__stage=stage - 1).filter(
            result=ResultChoices.WON)]

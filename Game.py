import random

from Team import Team


class Game:
    def __init__(self, home: Team, away: Team):
        self.home = home
        self.away = away

    def points_in_game(self):
        home_bonus = int(self.home.talent * 10)
        away_bonus = int(self.away.talent * 10)
        self.home.points_in_curr_game += random.randint(55, 100) + home_bonus
        self.away.points_in_curr_game += random.randint(50, 100) + away_bonus
        self.home.positive_points += self.home.points_in_curr_game
        self.away.positive_points += self.away.points_in_curr_game
        self.home.negative_points += self.away.points_in_curr_game
        self.away.negative_points += self.home.points_in_curr_game

    def winner_loser(self):
        # home won
        if self.home.points_in_curr_game > self.away.points_in_curr_game:
            self.update_winner_loser(self.home, self.away)
        # away won
        elif self.home.points_in_curr_game < self.away.points_in_curr_game:
            self.update_winner_loser(self.away, self.home)
        # draw
        # give the advantage to the team with the better curr wins strike
        elif self.home.curr_win_strike > self.away.curr_win_strike:
            self.update_winner_loser(self.home, self.away)
        elif self.home.curr_win_strike < self.away.curr_win_strike:
            self.update_winner_loser(self.away, self.home)
        # give the advantage to the away team
        else:
            self.update_winner_loser(self.away, self.home)

        # now clear the points from curr game
        self.home.points_in_curr_game = 0
        self.away.points_in_curr_game = 0

    def print_game(self):
        print(self.home.name, " VS. " , self.away.name)


    def start_game(self):
        self.points_in_game()
        self.winner_loser()

    def update_winner_loser(self, winner: Team, loser: Team):
        winner.team_won()
        loser.team_lost()

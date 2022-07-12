import random
class Team:
    def __init__(self , name: str):
        self.talent = float(0)
        self.wins = int(0)
        self.losses = int(0)
        self.positive_points = int(0)
        self.negative_points = int(0)
        self.curr_win_strike = int(0)
        self.curr_losses_strike = int(0)
        self.points_in_curr_game = int(0)
        self.longest_wins_strike = int(0)
        self.longest_losses_strike = int(0)
        self.name = name

    def give_talent(self):
        self.talent = random.uniform(0,1)

    def update_win_strike(self):
        if self.curr_win_strike > self.longest_wins_strike:
            self.longest_wins_strike = self.curr_win_strike
        self.curr_win_strike = 0

    def update_loss_strike(self):
        if self.curr_losses_strike > self.longest_losses_strike:
            self.longest_losses_strike = self.curr_losses_strike
        self.curr_losses_strike = 0

    def team_won(self):
        self.wins += 1
        self.curr_win_strike += 1
        self.update_loss_strike()

    def team_lost(self):
        self.losses += 1
        self.curr_losses_strike += 1
        self.update_win_strike()


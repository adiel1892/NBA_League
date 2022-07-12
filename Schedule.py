from Game import Game
from League import League


class Schedule:
    def __init__(self, league: League):
        self.league = league
        self.round_number = []
        self.matches = []
        self.matches_per_round = len(self.league.teams)
        self.num_teams = len(self.league.teams)
        self.rounds = (self.num_teams - 1) * 2
        for r in range(0, self.rounds):
            for match in range(0, self.matches_per_round):
                if r + 1 <= 19:
                    home = (r + match) % (self.num_teams - 1)
                    away = (self.num_teams - 1 - match + r) % (self.num_teams - 1)
                    if match == 0:
                        away = self.num_teams - 1
                    curr_game = Game(self.league.teams[home], self.league.teams[away])
                    self.round_number.append(curr_game)
                    if len(self.round_number) == self.matches_per_round:
                        self.matches.append(self.round_number)
                        self.round_number.clear()
                else:
                    away = (r + match) % (self.num_teams - 1)
                    home = (self.num_teams - 1 - match + r) % (self.num_teams - 1)
                    if match == 0:
                        home = self.num_teams - 1
                    curr_game = Game(self.league.teams[home], self.league.teams[away])
                    self.round_number.append(curr_game)
                    if len(self.round_number) == self.matches_per_round:
                        self.matches.append(self.round_number)
                        self.round_number.clear()

    def print_schedule(self):
        for r in range(0, self.rounds):
            print("Round number ", r + 1, ":")
            for match in range(0, self.matches_per_round):
                # print(self.matches)
                self.matches[r][match].print_game()

    def print_matches_in_round(self, r: int):
        print("Round number ", r, ":")
        for match in range(0, self.matches_per_round):
            self.matches[r - 1][match].print_game()

    def run_the_season(self):
        for r in range(0, self.rounds):
            for match in range(0, self.matches_per_round):
                print(r, " ", match)
                self.matches[r][match].start_game()

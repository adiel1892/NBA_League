from Team import Team
import functools


class League:
    def __init__(self):
        self.teams_names = ["Boston Celtics", "New York Knicks",
                            "Toronto Raptors", "Chicago Bulls",
                            "Cleveland Cavaliers", "Detroit Pistons",
                            "Milwaukee Bucks", "Miami Heat",
                            "Washington Wizards", "Orlando Magic",
                            "Denver Nuggets", "New Orleans Pelicans",
                            "Utah Jazz", "Golden State Warriors",
                            "LA Clippers", "Los Angeles Lakers",
                            "Phoenix Suns", "Houston Rockets",
                            "Memphis Grizzlies", "San Antonio Spurs"]
        self.teams = []
        if len(self.teams_names) != 20:
            raise Exception("Sorry, the number of teams in the league is 20")
        for i in self.teams_names:
            curr_team = Team(i)
            curr_team.give_talent()
            self.teams.append(curr_team)

    def longest_wins_strike(self) -> int:
        res = 0
        index = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].longest_wins_strike > res:
                res = self.teams[i].longest_wins_strike
                index = i
        print("The longest wins strike is ", res, " by ", self.teams[index].name)
        return res

    def longest_losses_strike(self) -> int:
        res = 0
        index = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].longest_losses_strike > res:
                res = self.teams[i].longest_losses_strike
                index = i
        print("The longest losses strike is ", res, " by ", self.teams[index].name)
        return res

    def positive_points_teams(self) -> int:
        res = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].positive_points - self.teams[i].negative_points > 0:
                res += 1
        print("The number of teams with positive points is ", res)
        return res

    def most_positive_points_team(self) -> str:
        points = self.teams[0].positive_points
        res = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].positive_points > points:
                points = self.teams[i].positive_points
                res = i
        print("The team with the most positive points in the league is ", self.teams[res].name, " with ", points,
              " points!")
        return self.teams[res].name

    def lowest_positive_points_team(self) -> str:
        points = self.teams[0].positive_points
        res = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].positive_points < points:
                points = self.teams[i].positive_points
                res = i
        print("The team with the lowest positive points in the league is ", self.teams[res].name, " with ", points,
              " points!")
        return self.teams[res].name

    def most_negative_points_team(self) -> str:
        points = self.teams[0].negative_points
        res = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].negative_points > points:
                points = self.teams[i].negative_points
                res = i
        print("The team with the most negative points in the league is ", self.teams[res].name, " with ", points,
              " points!")
        return self.teams[res].name

    def lowest_negative_points_team(self) -> str:
        points = self.teams[0].negative_points
        res = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].negative_points < points:
                points = self.teams[i].negative_points
                res = i
        print("The team with the lowest negative points in the league is ", self.teams[res].name, " with ", points,
              " points!")
        return self.teams[res].name

    def compare_teams(self):
        res = 0
        for i in self.teams:
            if i.wins > res:
                res = i.wins
        return res

    def show_table_when_season_over(self):
        # first sort by wins , if equal sort by difference
        self.teams.sort(key=lambda x: (x.wins , x.positive_points - x.negative_points),reverse=True)
        for i in range(0, len(self.teams)):
            curr_team = self.teams[i]
            print(i + 1, ") ", curr_team.name, " , wins: ", curr_team.wins, " , difference: ",
            curr_team.positive_points - curr_team.negative_points)

    def print_top_teams(self, top):
        print("Top ", top, " teams:")
        for i in range(0, top):
            print(i + 1, ") ", self.teams[i].name)

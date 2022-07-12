import functools

from Team import Team


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

    def longest_wins_strike(self):
        res = 0
        index = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].longest_wins_strike > res:
                res = self.teams[i].longest_wins_strike
                index = i
        print("The longest wins strike is ", res, " by ", self.teams[index].name)
        return res

    def longest_losses_strike(self):
        res = 0
        index = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].longest_losses_strike > res:
                res = self.teams[i].longest_losses_strike
                index = i
        print("The longest losses strike is ", res, " by ", self.teams[index].name)
        return res

    def positive_points_teams(self):
        res = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].positive_points - self.teams[i].negative_points > 0:
                res += 1
        print("The number of teams with positive points is " , res)
        return res

    def most_positive_points_team(self):
        points = self.teams[0].positive_points
        res = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].positive_points > points:
                points = self.teams[i].positive_points
                res = i
        print("The team with the most positive points in the league is ", self.teams[res].name, " with ", points,
              " points!")
        return self.teams[res].name

    def lowest_positive_points_team(self):
        points = self.teams[0].positive_points
        res = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].positive_points < points:
                points = self.teams[i].positive_points
                res = i
        print("The team with the lowest positive points in the league is ", self.teams[res].name, " with ", points,
              " points!")
        return self.teams[res].name

    def most_negative_points_team(self):
        points = self.teams[0].negative_points
        res = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].negative_points > points:
                points = self.teams[i].negative_points
                res = i
        print("The team with the most negative points in the league is ", self.teams[res].name, " with ", points,
              " points!")
        return self.teams[res].name


    def lowest_negative_points_team(self):
        points = self.teams[0].negative_points
        res = 0
        for i in range(0, len(self.teams)):
            if self.teams[i].negative_points < points:
                points = self.teams[i].negative_points
                res = i
        print("The team with the lowest negative points in the league is ", self.teams[res].name, " with ", points,
              " points!")
        return self.teams[res].name

    def compare_teams(self , a: Team , b: Team):
        if a.wins > b.wins:
            return True
        elif a.wins < b.wins:
            return False
        elif a.positive_points - a.negative_points > b.positive_points - b.negative_points:
            return True
        else:
            return False

    def show_table_when_season_over(self):
       sorted(self.teams , key=functools.cmp_to_key(self.compare_teams()))

    def print_top_teams(self , top):
        print("Top " , top , " teams:")
        for i in range(0,top):
            print(i + 1 , ") " , self.teams[i].name)



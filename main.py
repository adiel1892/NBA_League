from League import League
from Schedule import Schedule

if __name__ == '__main__':
    league = League()
    sch = Schedule(league)
    sch.run_the_season()
    league.show_table_when_season_over()
    league.print_top_teams(5)
    league.longest_wins_strike()
    league.longest_losses_strike()
    league.lowest_negative_points_team()
    league.lowest_positive_points_team()
    league.most_negative_points_team()
    league.most_positive_points_team()



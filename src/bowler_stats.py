import numpy as np
from dataframe import csv_dataset
import pandas as pd
from matplotlib import pyplot as plt


class Bowler():
    def __init__(self, bowler_name, match_dataframe, deliveries_dataframe):
        assert isinstance(bowler_name, str) and isinstance(deliveries_dataframe, pd.DataFrame) \
            and isinstance(match_dataframe, pd.DataFrame)
        self.bowler_name = bowler_name
        self.data = deliveries_dataframe
        self.match_data = match_dataframe
        self.valid_years = np.arange(2008, 2018)

    def get_bowler_match_stat(self, year):
        assert 2008 <= year <= 2017
        #Extract IDs
        match_ids = self.match_data.query(f"season == {year}")["id"]
        bowler_col = self.data.loc[self.data["bowler"] == self.bowler_name]
        bowler_match_stat = bowler_col[bowler_col.match_id.isin(list(match_ids))]
        return bowler_match_stat
    
    def get_number_of_games(self, year):
        assert 2008 <= year <= 2017
        bowler_stat = self.get_bowler_match_stat(year)
        return bowler_stat["match_id"].nunique()

    def get_number_of_runs(self, year):
        assert 2008 <= year <= 2017
        #Get bowler's statistics for the season
        bowler_stat = self.get_bowler_match_stat(year)
        number_of_games_played = self.get_number_of_games(year)
        return (number_of_games_played, bowler_stat["total_runs"].sum())
    
    def get_average_runs(self, year):
        assert 2008 <= year <= 2017
        games, runs = self.get_number_of_runs(year)
        return round(runs / games, 2)

    def compare_bowlers(self, other):
        #Calculate runs conceived per year and games played per year
        bowler_1_runs, bowler_2_runs = [], []
        bowler_1_games, bowler_2_games = [], []
        for year in self.valid_years:
            num_games_1, runs_1 = self.get_number_of_runs(year)
            num_games_2, runs_2 = other.get_number_of_runs(year)
            bowler_1_runs.append(runs_1)
            bowler_2_runs.append(runs_2)
            bowler_1_games.append(num_games_1)
            bowler_2_games.append(num_games_2)

        runs_combined = np.array(list(zip(bowler_1_runs, bowler_2_runs)))
        games_combined = np.array(list(zip(bowler_1_games, bowler_2_games)))
        # return runs_combined, games_combined
        
        #Calculate bowling average per year
        bowler_1_avg, bowler_2_avg = [], []
        for year in self.valid_years:
            b1_avg = self.get_average_runs(year)
            b2_avg = other.get_average_runs(year)
            bowler_2_avg.append(b2_avg)
            bowler_1_avg.append(b1_avg)
        average_combined = np.array(list(zip(bowler_1_avg, bowler_2_avg)))
        return runs_combined, games_combined, average_combined


if __name__ == "__main__":
    bowler_name_1 = "P Kumar"
    bowler_name_2 = "Harbhajan Singh"
    match_dataframe = pd.read_csv("../data/matches_2017.csv")
    deliveries_dataframe = pd.read_csv("../data/deliveries_2017.csv")

    bowler = Bowler()

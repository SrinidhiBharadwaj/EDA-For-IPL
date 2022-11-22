import pandas as pd
from pathlib import Path
import os
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


def plot_correlation():
    '''
    This function perfoms the following tasks:
    1. Loads matches and auctions datasets
    2. Removes unnecessary columns and rename any column to achieve machinge column names
    3. Creates two new data frames:
      a) auctionSpending: shows the total amount spent by each team each year
      b) winLossRatio:    shows the win/loss ratio for each team each year
    4. Calculates
    '''
    matches = pd.read_csv('../data/matches.csv')
    matches = matches.drop(
        matches.columns[[0, 2, 3, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17]], axis=1)
    matches = matches.rename(columns={"season": "Year", "winner": "Winner",
                                      "player_of_match": "MVP", "team1": "Team1", "team2": "Team2"})
    theTable = pd.read_csv('../data/IPL Player Auction 08-22.csv')

    # For each team, look into auction table and sum all the spending per year and save in a list
    totalBidYr = []
    for elem in matches["Team1"].unique():
        yearbid = []
        for year in range(8, 17):
            yearbid.append(sum(theTable[(theTable['Year'] == (
                2000+year)) & (theTable['Team'] == elem)]['Amount'].tolist()))
        totalBidYr.append(yearbid)

    # for each team get the total games played and total wins per year and calculate the ratio and save in a list
    totalWLYr = []
    for elem in matches["Team1"].unique():
        winLossYr = []
        for year in range(8, 17):
            gamesYr = matches[(matches['Year'] == (2000+year)) & ((matches['Team1']
                                                                   == elem) | (matches['Team2'] == elem))]["Winner"].tolist()
            occuranceYr = gamesYr.count(elem)
            if len(gamesYr) > 0:
                winLossYr.append((occuranceYr/(len(gamesYr) - occuranceYr)))
            else:
                winLossYr.append(np.nan)
        totalWLYr.append(winLossYr)

    # sum of bids per year for each team until 2016
    totalBidMat = np.array([np.array(xi) for xi in totalBidYr])
    # Win Loss ration for each team per year until 2016
    totalWLMat = np.array([np.array(xi) for xi in totalWLYr])

    # change year type to str from np.int64
    years = []
    for elem in range(len(matches["Year"].unique().tolist())):
        years.append(matches["Year"].unique()[elem].astype(str))

    # dataframe of sum of bids until 2016
    totalBidPerYear = pd.DataFrame(totalBidMat, columns=years, index=[
        matches["Team1"].unique()])
    # dataframe win loss ratio until 2016
    winLossPerYear = pd.DataFrame(totalWLMat, columns=years, index=[
                                  matches["Team1"].unique()])
    # save the new dataframes to local folder
    totalBidPerYear.to_csv('../data/auctionSpending.csv', index=True)
    winLossPerYear.to_csv('../data/winLossRatio.csv', index=True)

    # Average of the total sum of win/loss ratio for each team per year
    allTeamWLRatioAvg = []
    for i in range(len(years)):
        allTeamWLRatioAvg.append(sum(winLossPerYear[winLossPerYear[years[i]].notna(
        )][years[i]].to_numpy())/winLossPerYear.count()[i])
    # Average of total sum of spending on auction for all teams each year
    allTeamBidYear = []
    for i in range(len(years)):
        allTeamBidYear.append(
            sum(totalBidPerYear[years[i]].to_numpy())/len(matches["Team1"].unique()))

    # plot the total spending during auction  vs the win/loss ratio for each team per year
    for ind, elem in enumerate(list(totalBidPerYear.index.values)):
        plt.plot(totalBidPerYear[years[:]].iloc[ind].sort_values(
            ascending=True), winLossPerYear[years[:]].iloc[ind].sort_values(ascending=True), 'o', label=elem)
    xleft, xright = plt.xlim()
    yleft, yright = plt.ylim()
    plt.xlim([0.1, xright])
    plt.ylim([0.1, yright])
    plt.xlabel('Money Spent (1M $)')
    plt.ylabel('W/L Ratio')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title("W/L Ratio in relation with Money Spent in Auction")
    plt.savefig('../graphs/win_loss ratio vs Speding.png')

    # plot average of the total spending during auction  vs the win/loss ratio per year
    plt.plot(allTeamBidYear, allTeamWLRatioAvg, 'o')  # spending to win/ratio
    fig, ax = plt.subplots()
    ax.scatter(allTeamBidYear, allTeamWLRatioAvg)
    for ind, year in enumerate(years):
        ax.annotate(year, (allTeamBidYear[ind], allTeamWLRatioAvg[ind]))
    plt.xlabel('Money Spent (1M $)')
    plt.ylabel('W/L Ratio')
    plt.title(
        "Average W/L Ratio in relation with Money Spent in Auction for All Teams")
    plt.savefig('../graphs/win_loss ratio vs speding average.png')

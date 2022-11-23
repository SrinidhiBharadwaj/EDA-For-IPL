# ECE 143 Project - Group 3

## Date of Presentation: 11/23/2022

## Table of contents

1. [Overview](#ProjectOverview)
2. [Repository Structure](#RepositoryStructure)
   - [Datasets](#Datasets)
   - [Source Code](#SourceCode)
   - [Jupyter Notebook](#JupyterNotebook)
   - [Graphs](#Graphs)
3. [Third Party Modules](#ThirdPartymodules)
4. [Implementation](#Implementation)
5. [Presentation](#Presentation)

## Project Overview

Indian Premier League (IPL) is a cricket tournament, wherein 10 teams play league matches and compete for the final trophy each season. IPL started off in 2008 and the latest edition was in 2022.

We currently have collated data from matches season 2008 to 2017 from [Kaggle](https://www.kaggle.com/code/ambarish/exploratory-data-analysis-ipl) that we analyze for this project. We also scarped part of auction data from [Wiki](https://en.wikipedia.org/wiki/List_of_2009_Indian_Premier_League_personnel_changes).

## Repository Structure

### Datasets

The `data/` folder contains:

- [matches.csv](/data/matches.csv) contains all details of matches played in IPL through season 2008 to 2017. [Link to source](https://www.kaggle.com/code/ambarish/exploratory-data-analysis-ipl)
- [deliveries.csv](/data/deliveries.csv) contains details of every ball delivery through all matches in IPL sean 2008 to 2017. [Link to source](https://www.kaggle.com/code/ambarish/exploratory-data-analysis-ipl)
- [IPLPlayerAuction.csv](/data/IPLPlayerAuction.csv) contains IPL auction details from 2013 to 2022. [Link to source](https://www.kaggle.com/datasets/kalilurrahman/ipl-player-auction-dataset-from-start-to-now)
- [IPL Player Auction 08-22.csv](/data/IPL%20Player%20Auction.csv) contains IPL auction details limited to teams, players, years, and winning bid from 2008 to 2022.
- [auctionSpending.csv](/data/auctionSpending.csv) contains IPL total auction spending for each team for years 2008 to 2016
- [winLossRatio.csv](/data/winLossRatio.csv) contains IPL match info regarding win/loss ration for each team from 2008 to 2016

### Source Code

Source code for all data scraping and data analysis files are within the `src/` folder. [Link to Folder](src/)

Data scraping files:

- [wsBids.py](src/wsBids.py) is the web scraper

Pre-Processing files:

- [dataframe.py](src/dataframe.py) - Return a class object to load any dataset as a d_frame.
- [load_datasets.py](src/load_datasets.py) - Loads datasets using dataframe class.

Data processing files:

- [batsman_stats.py](src/batsman_stats.py) - Obtains basic batsman stats from the data.
- [player_performance.py](src/player_performance.py) - Collates player statistics to plot graphs.
- [bid_VS_performance.py](src/bid_VS_performance.py) - Calculate teams W:L ratio and total auction spending per year and plot their graph.
- [bowler_stats.py](src/bowler_stats.py) - Extracts bowler statistics for the given bowler
- [innings.py](src/innings.py) - Extracts information about bowlers given a match and innings
- [data_process.py](src/data_process.py) - Helper class to read and process the CSV files

### Jupyter Notebook

The [Jupyter Notebook](src/plot_support_book.ipynb) has all the plotting code. All analyzed data is stored as one cell for easy reproducibility.

### Graphs

The [`Graphs`](graphs/) folder has images as `.png` of all the analysis plots computed.

## Third Party Modules

The third party modules used are as listed below. They are included as [`requirements.txt`](requirements.txt).

- requests
- numpy
- pandas
- jupyter
- matplotlib
- seaborn
- BeautifulSoup

## Implementation

We used a conda virtual environment with the 3.9.13 python version to work on.
Make sure you are set up to use Python version - 3.9.13

Install all required libraries -

```
pip install -r requirements.txt
```

Auction Data Web Scarping -

Run create_auction_data() in wsBids.py
```
python -c 'import wsBids; wsBids.create_auction_data()' 
```

Source Code for analysis -

- Run any python files from within `src/` folder

```
src % python batsman_stats.py
```

Jupyter Notebook -

- Run compete notebook or particular cells of [`plot_support_book.ipynb`](src/plot_support_book.ipynb) for viewing the plots.

## Presentation

Final Presentation - [Link to Presentation](/Presentation/Final_Presentation.pdf)

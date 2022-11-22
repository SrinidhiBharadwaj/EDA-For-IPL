n# ECE 143 Project - Group 13 
## Date of Presentation: 11/23/2022

## Table of contents

1. [Overview](#ProjectOverview)
2. [Repository Structure](#RepositoryStructure)
    - [Datasets](#Datasets)
    - [Source Code](#SourceCode)
    - [Jupyter Notebook](#JupyterNotebook)
    - [Graphs](#Graphs)
3. [Third Party Modules](#ThirdPartymodules)
5. [Implementation](#Implementation)
6. [Presentation](#Presentation)

## Project Overview
Indian Premier League (IPL) is a cricket tournament, wherein 10 teams play league matches and compete for the final trophy each season. IPL started off in 2008 and the latest edition was in 2022.

We currently have collated data from matches season 2008 to 2017 that we analyze for this project.

## Repository Structure
### Datasets
The `data/` folder contains:
- [matches.csv](/data/matches.csv) contains all details of matches played in IPL through season 2008 to 2017. [Link to source](https://www.kaggle.com/code/ambarish/exploratory-data-analysis-ipl)
- [deliveries.csv](/data/deliveries.csv) contains details of every ball delivery through all matches in IPL sean 2008 to 2017. [Link to source](https://www.kaggle.com/code/ambarish/exploratory-data-analysis-ipl)

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
Auction Data Web Scarping -
```
```

Source Code for analysis -
- Run any python files from within `src/` folder
```
src % python batsman_stats.py
```

Jupyter Notebook -
- Run compete notebook or particular cells of [`plot_support_book.ipynb`](src/plot_support_book.ipynb) for viewing the plots.

## Presentation
Final Presentation - [Link to Presentation](/Presentation/Presentation.pdf)

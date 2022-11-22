import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import os
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


def parse_web(url, index, ignoreColumn, year, columnHeader, conversion):
    '''
    Using beautiful soup to parse html of a url from web
    Find the tables.
    Since the tables don't have a specific class or id and the column -
        headers may vary I manualy found the index of the tables that -
        display auction information
    Find the Table headers and place them in a list
    Create a pandas DataFrame using the table headers as columns
    Place all the table rows from selected table in the parsed html in to the DataFrame
    Remove any spacing or special characters 
    Remove unnecessary columns
    Change the Name of the columns to be same as other tables
    Change the type of columns as needed
    Convert the money as needed
    Add Year column

    url:          is the address of website for webscrapping
    index:        is the position of the table in the website (I had to do this manually because there were no specific ids for the tables)
    ignoreColumn: is the columns to be ignored in the table
    year:         is the year which data belongs to
    columnHeader: are the names to achieve a universal naming for all the columns
    conversion:   conversion for the currency used in the table
    '''
    assert isinstance(url, str)
    assert isinstance(index, int)
    assert isinstance(ignoreColumn, list)
    assert isinstance(year, int)
    assert isinstance(columnHeader, dict)
    assert isinstance(conversion, (int, float))
    assert index >= 0 and year > 2007 and conversion > 0.0
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all("table")
    headers = []
    for th in table[index].find_all('th'):
        title = th.text.strip()
        headers.append(title)

    theTable = pd.DataFrame(columns=headers)
    for tr in table[index].find_all('tr')[1:]:
        rowData = tr.find_all('td')
        row = [elem.text.strip().replace('$', '').replace(',', '')
               for elem in rowData]
        length = len(theTable)
        theTable.loc[length] = row
    theTable = theTable.drop(theTable.columns[ignoreColumn], axis=1)
    theTable = theTable.rename(
        columns=columnHeader)
    theTable["Amount"] = pd.to_numeric(theTable["Amount"])
    theTable['Amount'] = theTable["Amount"].apply(lambda x: x*conversion)
    theTable["Year"] = year
    return theTable


def combine_tables(theTables):
    '''
    Combine all the DataFrames from 2008 to 2012
    Read in csv to DataFrames
    Remove unnecessary columns
    Combine DataFrames to include data from 2008 to 2022
    Write to a new csv file

    theTables: pd.DataFrame list which consists of all previous tables
    '''
    assert isinstance(theTables, list)
    assert all(isinstance(elem, pd.DataFrame) for elem in theTables)
    assert len(theTables) > 0
    theTable08To12 = pd.concat(theTables)
    theTable13_22 = pd.read_csv(
        '../data/IPLPlayerAuctionData13-22.csv')
    theTable13_22 = theTable13_22.drop(theTable13_22.columns[[1, 5]], axis=1)
    theTable = pd.concat([theTable08To12, theTable13_22])
    theTable["Amount"] = pd.to_numeric(theTable["Amount"])
    theTable['Amount'] = theTable["Amount"].apply(lambda x: x//81.53).round(-3)
    theTable.loc[theTable['Team'] ==
                 'Pune Warriors India', 'Team'] = 'Pune Warriors'
    theTable.loc[theTable['Team'] ==
                 'Delhi Capitals', 'Team'] = 'Delhi Daredevils'
    theTable.loc[theTable['Team'] == 'Rising Pune Supergiant',
                 'Team'] = 'Rising Pune Supergiants'
    theTable.to_csv('../data/IPL Player Auction 08-22.csv', index=False)


'''
these are the used parameters including urls for web scraping
("https://en.wikipedia.org/wiki/List_of_2008_Indian_Premier_League_auctions_and_personnel_signings", 
          2, [0, 1, 3, 4, 5], 2008, {"Name": "Player", "Auctioned Price(in US$ thousands)": "Amount"}, 81525)
("https://en.wikipedia.org/wiki/List_of_2009_Indian_Premier_League_personnel_changes", 
          7, [0, 4], 2009, {"Winning bid": "Amount"}, 81.53)
("https://en.wikipedia.org/wiki/List_of_2010_Indian_Premier_League_personnel_changes", 
          0, [3], 2010, {"Franchise": "Team", "Sold price (USD)": "Amount"}, 81.53)
("https://en.wikipedia.org/wiki/List_of_2011_Indian_Premier_League_personnel_changes", 
          2, [0, 4], 2011, {"Winning bid": "Amount"}, 81.53)
("https://en.wikipedia.org/wiki/List_of_2012_Indian_Premier_League_personnel_changes", 
          9, [0, 3], 2012, {"Winning bid": "Amount"}, 81.53)
'''

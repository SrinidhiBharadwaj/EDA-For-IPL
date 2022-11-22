import numpy as np
import pandas as pd
from collections import defaultdict
from matplotlib import pyplot as plt

class Innings(object):
    '''
    Helper class to extract innings related information for a given bowler
    '''
    def __init__(self, data, match_id):
        '''
        Constructor
        Input:
        data: Input dataframe from deliveries
        '''
        assert isinstance(data, pd.DataFrame)
        self.data = data
        self.id = match_id
        if "match_id" in self.data:
            self.match_deets = self.data.loc[self.data["match_id"] == self.id]
        else:
            assert False, "Invalid dataframe"

    def get_over_info(self, inning_deets, over):
        '''
        Method to return the runs conceived by the bowler in a given over
        Input:
        inning_deets: Dataframe containing all the information regarding the given match and innings
        over: Over number to get the informaiton of
        Return:
        Tuple of bowler name and runs conceived by that bowler
        '''
        assert isinstance(inning_deets, pd.DataFrame)

        over_deets = inning_deets.loc[inning_deets["over"] == over]
        bowler_name = np.unique(over_deets["bowler"])

        runs_conceived = over_deets["total_runs"].sum()
        return (bowler_name[0], runs_conceived)

    def get_bowling_stat_inning(self, innings):
        '''
        Method to return the bowling statistics of all the bowlers in a given innings
        Input:
        innings: Innings number
        Return:
        Dictionary containing individual bowler performance
        '''
        assert isinstance(innings, int) and innings in [1, 2]

        bowler_dict = defaultdict(list) #List of bowlers per innings
        inning_deets = self.match_deets.loc[self.data["inning"] == innings]

        overs = np.unique(inning_deets["over"])
        for over in overs:
            bowler, runs = self.get_over_info(inning_deets, over)
            bowler_dict[bowler].append(runs)

        return bowler_dict
    
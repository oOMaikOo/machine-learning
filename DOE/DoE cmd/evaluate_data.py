# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:12:11 2019

@author: maikl
Version : 0.0.1
"""

import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.factorplots import interaction_plot
import csv

class plots:
    __Names = {}
    def __init__self(self):
        pass
    
    def plot_interaction_plot(self,f):
        
        with open(f) as csv_file:
            reader = csv.reader(csv_file, delimiter='\t')
            header_row = next(reader)
    
            for index, column_header in enumerate(header_row):
                self.__Names[index] = column_header
                
        df = pd.read_csv(f, delimiter='\t')
        i = 0
        while i < (len(self.__Names)-3):
            fig, ax = plt.subplots(figsize=(16, 16))
            interaction_plot(x=df[self.__Names[i+2]], trace=df[self.__Names [i+1]], response=df[self.__Names[len(self.__Names)-1]], 
                           colors=['red', 'blue'], markers=['D', '^'], ms=10, ax=ax)
            i += 1
        i = 0
        while i < (len(self.__Names)-3):
            fig, ax = plt.subplots(figsize=(16, 16))
            interaction_plot(x=df[self.__Names[i+1]], trace=df[self.__Names [i+2]], response=df[self.__Names[len(self.__Names)-1]], 
                           colors=['red', 'blue'], markers=['D', '^'], ms=10, ax=ax)
            i += 1
        plt.show()
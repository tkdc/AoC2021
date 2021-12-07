# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:50:51 2021

@author: T. Katemann
@description: AoC 2021 07
"""

import numpy as np
from scipy import optimize

class AoC_2107_Calc:
    
    def __init__(self):
        self.ar_data = np.array([])

        print('# AoC 21 07 init #')

    # read raw data from file
    def get_file_data(self, strFile):
        file = open(strFile, 'r')
        self.ar_data = np.array(file.read().splitlines())

    def prep_data(self):
        # string array to num array
        self.ar_data_num = np.array(list(map(float,oA.ar_data[0].split(','))))
        print("Num Crab Init: %d" % (len(self.ar_data_num)))

    # crab fun 1
    def fun_crab1(self,x):
        x1=np.ones(self.ar_data_num.size)*x
        d_diff = abs(self.ar_data_num - x1)
        return sum(d_diff)
    # crab fun 2
    def fun_crab2(self,x):
        x1=np.ones(self.ar_data_num.size)*x
        d_diff = abs(self.ar_data_num - x1)
        return sum(d_diff*(d_diff+1)/2)
            
    # evaluate data a
    def eval_data(self):
        print()
        x0 = np.mean(self.ar_data_num)   
        self.res1 = optimize.minimize(self.fun_crab1, x0, method='SLSQP')
        self.d_pos_min_1 = np.int(np.round(self.res1.x[0]))
        self.d_pos_min_fuel_1 = self.fun_crab1(self.d_pos_min_1)
        print("P1: Min Pos: %d, Fuel: %d" % (self.d_pos_min_1,self.d_pos_min_fuel_1))
        
        self.res2 = optimize.minimize(self.fun_crab2, x0, method='SLSQP')
        self.d_pos_min_2 = np.int(np.round(self.res2.x[0]))
        self.d_pos_min_fuel_2 = self.fun_crab2(self.d_pos_min_2)
        print("P2: Min Pos: %d, Fuel: %d" % (self.d_pos_min_2,self.d_pos_min_fuel_2))

#------------------------------------------------------------------------------
# execute by file call
if __name__ == '__main__':   
    oA = AoC_2107_Calc()
    oA.get_file_data('aoc_2107_data.dat')
    oA.prep_data()
    oA.eval_data()


# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:27:37 2021

@author: T. Katemann
@description: AoC 2021 06
"""

import numpy as np

class AoC_2106_Calc:
    
    def __init__(self):
        self.ar_data = np.array([])
        self.num_days = 256
        self.bVerbose = 0
        self.d_num_diff = 0
        
        print('# AoC 21 06 init #')

    # read raw data from file
    def get_file_data(self, strFile):
        file = open(strFile, 'r')
        self.ar_data = np.array(file.read().splitlines())
    
    def prep_data(self):
        # string array to num array
        self.ar_data_num = np.array(list(map(int,oA.ar_data[0].split(','))))
        print(self.ar_data_num)
        print("Num Fish Init: %d" % (len(self.ar_data_num)))  

    # evaluate data a
    def eval_data_a(self):
        print()
        for idx in range(1,self.num_days+1):
            
            num_new_fish = sum(self.ar_data_num == 0)
            self.ar_data_num -= 1
            if (num_new_fish > 0):
                self.ar_data_num[self.ar_data_num < 0] = 6
                self.ar_data_num = np.append(
                    self.ar_data_num, 
                    np.ones(num_new_fish, dtype=int)*8)
                                
        print("A: Num fish: %d after idx %d" % (len(self.ar_data_num),idx))
        
    # evaluate data b 
    def eval_data_b(self):

        self.ar_interval = np.zeros(9, dtype=int)
        for idx_fish in self.ar_data_num:
            self.ar_interval[idx_fish] += 1 
            
        for idx in range(self.num_days):
            idx_int = np.mod(idx, 9)
            idx_int_shft = np.mod((idx_int + 7), 9)
            self.ar_interval[idx_int_shft] += self.ar_interval[idx_int]
                
        print("B: Num fish: %d after idx %d" % (sum(self.ar_interval),idx+1))

    
#------------------------------------------------------------------------------
# execute by file call
if __name__ == '__main__':   
    oA = AoC_2106_Calc()
    oA.get_file_data('aoc_2106_data.dat')
    oA.prep_data()
    oA.eval_data_b()

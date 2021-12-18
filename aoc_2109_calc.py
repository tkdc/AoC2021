# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 06:42:55 2021

@author: T. Katemann
@description: AoC 2021 09
"""

import numpy as np

class AoC_2109_Calc:
    
    def __init__(self):
        self.ar_data = np.array([])
        self.b_verbose = 0

        print('# AoC 21 09 init #')
        
    # read raw data from file
    def get_file_data(self, strFile):
        file = open(strFile, 'r')
        self.ar_data = (file.read().splitlines())

    def prep_data(self):
        # string array to num array
        br=len(self.ar_data[0])
        self.width = br
        self.height = len(self.ar_data)
        
        print('width:',br, 'height:', self.height)
        
        self.ar_data_map = [10*np.ones(br+2)]
        for row in self.ar_data:
            ar = np.array(list(map(int, row)))
            ar = np.append(np.array([10]),ar)
            ar = np.append(ar,np.array([10]))          
            self.ar_data_map.append(ar)
        self.ar_data_map.append(10*np.ones(br+2))
        
        self.ar_data_map1 = np.array(self.ar_data_map)
        if 1:
            print(self.ar_data_map1)
        
    def chk_min(self, idx):
        
        poi = self.ar_data_map1[idx[0],idx[1]]
        # vertical neigbar
        poi_b = np.append(
            self.ar_data_map1[[idx[0]+1,idx[0]-1],idx[1]],
            self.ar_data_map1[idx[0],[idx[1]+1,idx[1]-1]]
            )
        bMin = not all(poi_b>poi)
        #print(poi,poi_b, bMin)
        return bMin
     
    def chk_bas(self, idx):
        
        poi = self.ar_data_map1[idx[0],idx[1]]
        poi1 = self.ar_data_map1[idx[0]+1,idx[1]]
        poi2 = self.ar_data_map1[idx[0]-1,idx[1]]
        poi3 = self.ar_data_map1[idx[0],idx[1]+1]
        poi4 = self.ar_data_map1[idx[0],idx[1]-1]
        
        incr = []
        if poi1 > poi and poi1 < 9:
                incr.append([idx[0]+1,idx[1]])
        if poi2 > poi and poi2 < 9:
                incr.append([idx[0]-1,idx[1]])
        if poi3 > poi and poi3 < 9:
                incr.append([idx[0],idx[1]+1])
        if poi4 > poi and poi4 < 9:
                incr.append([idx[0],idx[1]-1])
                
        return incr  
           
    # evaluate data a
    def eval_data(self):
        
        self.sum_risk = 0
        self.min_loc = []
        
        # Part 1
        # vertical loop
        for idx_v in range(1,self.height+1):
            # horizontal loop
            for idx_h in range(1,self.width+1):
            
                b_min = self.chk_min([idx_v,idx_h])
                if b_min == 0:
                    self.min_loc.append([idx_v,idx_h])
                    # disp
                    if self.b_verbose:
                        print([idx_v,idx_h],
                          self.ar_data_map1[idx_v,idx_h])
                    
                    self.sum_risk += (1+self.ar_data_map1[idx_v,idx_h])
        
        print('P1: SumRisk:',self.sum_risk)
        
        # Part 2: find basin
        self.ar_sum_loc = []
        self.ar_sum_loc_max3 = np.array([],dtype=int)
        for item1 in self.min_loc:
            act_coord = [item1]
            bRun = True
            sum_bas = 1
            sum_coord = [item1]
            while(bRun):
                next1 = self.chk_bas(act_coord[-1])
                act_coord.pop()
                for item in next1:
                    if item not in sum_coord:
                        act_coord.append(item)
                        sum_coord.append(item)
                
                if self.b_verbose:
                    print('next coord', act_coord)
                    
                if len(act_coord) == 0:
                    bRun = False
                    sum_bas = len(sum_coord)
                    self.ar_sum_loc.append(sum_bas)
                    if self.b_verbose:
                        print('sum coord for one min', sum_bas)
        
        print('P2: all basin len:', self.ar_sum_loc)
        
        # find top 3
        self.ar_sum_loc = np.array(self.ar_sum_loc)
        for idx in range(0,3):
            actmax=np.where(self.ar_sum_loc  == self.ar_sum_loc.max())

            self.ar_sum_loc_max3 = np.append(self.ar_sum_loc_max3, 
                                             self.ar_sum_loc[actmax[0]])
            self.ar_sum_loc = np.delete(self.ar_sum_loc,actmax[0])
        
            if len(self.ar_sum_loc_max3) >= 3:
                break
        
        
        print('P2: top3 basin len:', self.ar_sum_loc_max3)
        print('P2: top3 basin len sum:', np.prod(self.ar_sum_loc_max3))

            
#------------------------------------------------------------------------------
# execute by file call
if __name__ == '__main__':   
    oA = AoC_2109_Calc()
    oA.get_file_data('aoc_2109_data.dat')
    oA.prep_data()
    oA.eval_data()


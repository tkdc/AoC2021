# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 09:32:06 2021

@author: T. Katemann
@description: AoC 2021 11
"""

import numpy as np

class AoC_2111_Calc:
    
    def __init__(self):
        self.ar_data = np.array([])
        self.num_it = 100
        self.bVerbose = 0
        self.bStopAtAll = 1
        print('# AoC 21 11 init #')
        
    # read raw data from file
    def get_file_data(self, strFile):
        file = open(strFile, 'r')
        self.ar_data = (file.read().splitlines())

    def prep_data(self):
        # size
        self.width = len(self.ar_data[0])
        self.height = len(self.ar_data)
        
        print('width:',self.width, 'height:', self.height)
        
        self.ar_data_map = [10*np.ones(self.width+2)]
        for row in self.ar_data:
            ar = np.array(list(map(int, row)))
            ar = np.append(np.array([10]),ar)
            ar = np.append(ar,np.array([10]))          
            self.ar_data_map.append(ar)
        self.ar_data_map.append(10*np.ones(self.width+2))
        
        self.ar_data_map1 = np.array(self.ar_data_map, dtype=int)
        if self.bVerbose:
            print('START')
            print(self.ar_data_map1)
    
    def chk_adj(self, idx):
        
        # adapt neighbors        
        for idx_v in range(idx[0]-1,idx[0]+2):
            for idx_h in range(idx[1]-1,idx[1]+2):
                if self.ar_data_map1[idx_v,idx_h] >= 9:
                    self.ar_data_map1[idx_v,idx_h]+=1
                elif self.ar_data_map1[idx_v,idx_h] == 0:
                    self.ar_data_map1[idx_v,idx_h]=0
                else:
                    self.ar_data_map1[idx_v,idx_h]+=1
                    
        self.ar_data_map1[idx[0],idx[1]] = 0

        return 0
    
    def chk_li(self):
        self.at_lim = np.array(np.where(self.ar_data_map1[
                   range(1,self.height+1),:]\
                    [:,range(1,self.width+1)] >= 10 ))+1
            
        if self.bVerbose: 
           print ('cKL', self.at_lim)
        

    # evaluate data a
    def eval_data(self):
        self.sum_flash=0
        
        for idx_it in range(0,self.num_it):
            if self.bVerbose:
                print ('IT',idx_it+1)

            for idx_v in range(1,self.height+1):
                
                # horizontal loop
                for idx_h in range(1,self.width+1):
                #print(self.ar_data_map1[1,idx])
                    self.ar_data_map1[idx_v,idx_h] += 1
            
            
            self.chk_li()
            idx_c=0
            while(len(self.at_lim[0]) != 0):
                num_fl = len(self.at_lim[0])
                idx_c +=1
                if self.bVerbose:
                    print ('LOOP',idx_c,'fl:',num_fl)
                
                self.sum_flash += num_fl
                    
                for idx_ck in range(0,num_fl):
                    idx_v = self.at_lim[0][idx_ck]
                    idx_h = self.at_lim[1][idx_ck]
                    self.chk_adj([idx_v,idx_h])
                
                self.chk_li()
                if len(self.at_lim [0]) == 0:
                    break
            
            num_fl_it = np.sum(self.ar_data_map1[
                   range(1,self.height+1),:]\
                    [:,range(1,self.width+1)] == 0)
                

            if self.bVerbose:
                print(self.ar_data_map1)
                
            if num_fl_it == (self.height*self.width):
                if self.bVerbose:
                    print('IT',idx_it+1, 'SumFlashIT',num_fl_it)
                    print(self.ar_data_map1)
                if self.bStopAtAll:
                    break
        if self.bVerbose:
            print('END')
            print(self.ar_data_map1)
        print('SumFlash',self.sum_flash)
        print('CntFlash',idx_it+1)


#------------------------------------------------------------------------------
# execute by file call
if __name__ == '__main__':   
    oA = AoC_2111_Calc()
    oA.get_file_data('aoc_2111_data.dat')
    # Part 1
    print('## PART 1 ##')
    oA.num_it = 100
    oA.bStopAtAll = 0
    oA.prep_data()
    oA.eval_data()
     # Part 2
    print('## PART 2 ##')
    oA.num_it = 500
    oA.bStopAtAll = 1
    oA.prep_data()
    oA.eval_data()   

    


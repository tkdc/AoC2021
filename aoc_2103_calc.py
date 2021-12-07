# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:00:28 2021

@author: T. Katemann
@description: AoC 2021 03
"""

import os
import numpy as np

class AoC_2103_Calc:
    
    def __init__(self):
        self.str_cwd = os.getcwd()
        self.ar_data = np.array([])
        
        self.ar_data_bin_num = 0
        self.d_data_gamma_dec = 0
        self.d_data_eps_dec = 0
        self.d_data_oxy_dec = 0
        self.d_data_co2_dec = 0

        self.bVerbose = 1
        
        print('# AoC 21 03 init #')

    # read raw data from file
    def get_file_data(self, strFile):
        str_file_path = os.path.join(self.str_cwd,strFile)
        file = open(str_file_path, 'r')
        self.ar_data = file.readlines()
    
    # calc bin to decimal
    def bin2dec(self, bin_value):
        dec_value = 0
        for idx_bit in range(len(bin_value)):
            dec_value += \
                (bin_value[idx_bit] * np.power(2, len(bin_value)-idx_bit-1))
        return dec_value

    # reduce bit vector to relevant range
    def bit_list_red_num(self, idx_col, idx_range, num_dom):
        # num_dom (1,0): dominant bit for relevanz        
        
        if sum(idx_range)>1:
            if self.bVerbose > 1:
                print('#' + str(num_dom) + 'Col:' + str(idx_col))
                print('#' + str(num_dom) + 'Rng:' + str(sum(idx_range)))
                #print(self.ar_data_bin_num[idx_range,:])
                
            # get numbers of true and false
            num_1 = sum(self.ar_data_bin_num[idx_range,idx_col] == 1)
            num_0 = sum(self.ar_data_bin_num[idx_range,idx_col] == 0)
    
            # compare and determine next range 
            if num_1 >= num_0:
                idx_range = np.bitwise_and(idx_range, 
                    (self.ar_data_bin_num[:,idx_col] == (num_dom == 1)))
            else:
                idx_range = np.bitwise_and(idx_range, 
                    (self.ar_data_bin_num[:,idx_col] == (num_dom == 0)))
                    
        else:
            if self.bVerbose > 1:
                print('#' + str(num_dom) + 'Col:' + str(idx_col))
                print('#' + str(num_dom) + 'Rng:' + str(sum(idx_range)))
                #print(self.ar_data_bin_num[idx_range,:])
                   
        return idx_range
    
    # evaluate bin list
    def eval_data(self):
        # format bin data
        self.ar_data_bin_num = np.array([ 
            [int(i) for i in str(x) if str(i).isnumeric()] 
                for x in self.ar_data ] )

        # shape of data
        numbitrow = self.ar_data_bin_num.shape[0]
        numbitcol = self.ar_data_bin_num.shape[1]
        print("BitColNumber: %d" % (numbitcol))
        print("BitRowNumber: %d" % (numbitrow))
        
        # init gamma vector
        ar_data_gamma = np.ones(numbitcol, dtype=int)
        
        # init ranges woth true vector
        idx_range_1 = np.ones(numbitrow, dtype=bool)
        idx_range_2 = np.ones(numbitrow, dtype=bool)

        # loop ovr bit column
        for idx_col in range((numbitcol)):
            
            # P2: reduce to required line
            idx_range_1 = self.bit_list_red_num(idx_col, idx_range_1, 1)
            idx_range_2 = self.bit_list_red_num(idx_col, idx_range_2, 0)
            
            # P1 most common bit
            ar_data_gamma[idx_col]=int(
                ( sum(self.ar_data_bin_num[:,idx_col]==1) 
                > sum(self.ar_data_bin_num[:,idx_col]==0))
                )
        
        #----------------------------------------------------------------------
        # P1 calculate and disp final decimal value
        self.d_data_gamma_dec = self.bin2dec(ar_data_gamma)
        self.d_data_eps_dec = self.bin2dec(ar_data_gamma==0) # not

        print("P1 Gamma: %d, Eps: %d" % 
            (self.d_data_gamma_dec, self.d_data_eps_dec))
        print("P1 Result: %d" % 
            (self.d_data_gamma_dec * self.d_data_eps_dec))
        
        # P2 calculate and disp decimal value
        if self.ar_data_bin_num[idx_range_1,:].shape[0] == 1 and \
           self.ar_data_bin_num[idx_range_2,:].shape[0] == 1:
               
            # if reduced properly to one line
            self.d_data_oxy_dec = \
                self.bin2dec(np.squeeze(self.ar_data_bin_num[idx_range_1,:]))
            self.d_data_co2_dec = \
                self.bin2dec(np.squeeze(self.ar_data_bin_num[idx_range_2,:]))
            
            print("P2 Oxy: %d, CO2: %d" % 
                (self.d_data_oxy_dec, self.d_data_co2_dec))
            print("P2 Result: %d" % 
                (self.d_data_oxy_dec * self.d_data_co2_dec))
                
            if self.bVerbose > 0:
                print("+ P2 Result Bit Row, Oxy and Co2")
                print(self.ar_data_bin_num[idx_range_1,:])
                print(self.ar_data_bin_num[idx_range_2,:])
        else:
            # in case reduction not successful
            print("P2 Oxy / CO2 Reduction Failure")
            print("Oxy:")
            print(self.ar_data_bin_num[idx_range_1,:])
            print("CO2:")
            print(self.ar_data_bin_num[idx_range_2,:])
        
#------------------------------------------------------------------------------
# execute by file call
if __name__ == '__main__':   
    oAoC03 = AoC_2103_Calc()
    oAoC03.get_file_data('aoc_2103_data.dat')
    oAoC03.eval_data()
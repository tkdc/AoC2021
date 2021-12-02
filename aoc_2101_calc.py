# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 20:04:06 2021

@author: T. Katemann
@description: AoC 2021 01
"""

import os
import numpy as np

class AoC_2101_Calc:
    
    def __init__(self):
        self.str_cwd = os.getcwd()
        self.ar_data = []
        print('# Aoc2021 init #')

    def get_file_data(self, strFile):
        str_file_path = os.path.join(self.str_cwd,strFile)
        file = open(str_file_path, 'r')
        self.ar_data = file.readlines()
        
    def eval_data(self):
        self.data_num = [int(x) for x in self.ar_data]
        self.data_num_diff = np.diff(self.data_num)
        self.data_num_dir = np.sign(self.data_num_diff)
        
        # check direction
        print('#P1 num :'+str(len(self.data_num_dir)))
        print('#P1 Incr:'+str(sum(self.data_num_dir > 0)))
        print('#P1 Eq  :'+str(sum(self.data_num_dir == 0)))
        print('#P1 Decr:'+str(sum(self.data_num_dir < 0)))

        # check direction of convolve
        self.data_num_conv = np.convolve(self.data_num, np.ones(3), 'valid');
        self.data_num_conv_diff = np.diff(self.data_num_conv)
        print('#P2 num :'+str(len(self.data_num_conv_diff)))
        print('#P2 Incr:'+str(sum(self.data_num_conv_diff > 0)))
        print('#P2 Eq  :'+str(sum(self.data_num_conv_diff == 0)))
        print('#P2 Decr:'+str(sum(self.data_num_conv_diff < 0)))
              
# execute by file call
if __name__ == '__main__':   
    oAoC01 = AoC_2101_Calc()
    oAoC01.get_file_data('aoc_2101_data.dat')
    oAoC01.eval_data()
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:54:31 2021

@author: T. Katemann
@description: AoC 2021 05
"""

import os
import numpy as np
import re

class AoC_2105_Calc:
    
    def __init__(self):
        self.str_cwd = os.getcwd()
        self.ar_data = np.array([])
        
        self.bVerbose = 0
        
        print('# AoC 21 05 init #')

    # read raw data from file
    def get_file_data(self, strFile):
        str_file_path = os.path.join(self.str_cwd,strFile)
        file = open(str_file_path, 'r')
        self.ar_data = np.array(file.readlines())
    
    
    def prep_data(self):
        
        ar_data_coord = [];
        ar_data_coord_red = [];
        ar_data_coord_diag = [];
        
        for cur_line in self.ar_data:
            str_coord_val = np.array(re.findall(r'\d+', cur_line))
            d_ar_coord_val = [int(x) for x in str_coord_val]
           
           # all coord
            ar_data_coord.append(d_ar_coord_val)
            
            # only horz or vert vents
            if d_ar_coord_val[0] == d_ar_coord_val[2] \
            or d_ar_coord_val[1] == d_ar_coord_val[3]:
                ar_data_coord_red.append(d_ar_coord_val)
                
            # only horz or vert vents
            if np.abs(d_ar_coord_val[0] - d_ar_coord_val[2]) == \
               np.abs(d_ar_coord_val[1] - d_ar_coord_val[3]):
                ar_data_coord_diag.append(d_ar_coord_val)       
                
        # Coord x1,y1, x2,y2 
        self.ar_data_coord = np.array(ar_data_coord);
        self.ar_data_coord_red = np.array(ar_data_coord_red);
        self.ar_data_coord_diag = np.array(ar_data_coord_diag);
        self.ar_data_coord_both = np.append(self.ar_data_coord_red,
                                            self.ar_data_coord_diag,axis=0)

        print('Num All  Coord: %d' % (self.ar_data_coord.shape[0]))
        print('Num H/V  Coord: %d' % (self.ar_data_coord_red.shape[0]))
        print('Num Diag Coord: %d' % (self.ar_data_coord_diag.shape[0]))
        
        # get area
        self.d_area_x0 = np.min(self.ar_data_coord_both[:,[0,2]])
        self.d_area_y0 = np.min(self.ar_data_coord_both[:,[1,3]])
        self.d_area_x1 = np.max(self.ar_data_coord_both[:,[0,2]])
        self.d_area_y1 = np.max(self.ar_data_coord_both[:,[1,3]])

        print('Area: x0,y0 : %d,%d / x1,y1 : %d,%d' % \
            (self.d_area_x0,self.d_area_y0,self.d_area_x1,self.d_area_y1))
        
        self.d_mat_area = np.zeros(
            [self.d_area_y1+1,self.d_area_x1+1],dtype=int)
        
    # evaluate data
    def eval_data(self):
        
        # apply horz / vert points
        for idx in range(self.ar_data_coord_red.shape[0]):
            
            cur_vec = self.ar_data_coord_red[idx,:]
            y1 = min([cur_vec[1],cur_vec[3]]);
            y2 = max([cur_vec[1],cur_vec[3]]);
            x1 = min([cur_vec[0],cur_vec[2]]);
            x2 = max([cur_vec[0],cur_vec[2]]);
            # apply vector
            self.d_mat_area[range(y1,y2+1), range(x1,x2+1)] += 1
        
        # count relevant points
        self.num_req_hv = np.sum(oA.d_mat_area>=2);
        
        # apply diagonal points
        for idx in range(self.ar_data_coord_diag.shape[0]):
            
            cur_vec = self.ar_data_coord_diag[idx,:]
            max_len = np.abs(cur_vec[3]-cur_vec[1])
            
            x_dir = np.sign((cur_vec[2] - cur_vec[0]))
            x_vec = np.arange(cur_vec[0], cur_vec[2] + x_dir, x_dir)
            y_dir = np.sign((cur_vec[3] - cur_vec[1]))
            y_vec = np.arange(cur_vec[1], cur_vec[3] + y_dir, y_dir)
            
            # loop over vector elements
            for idx_d in range(0, max_len + 1 ):
                
                x_cur = x_vec[idx_d]
                y_cur = y_vec[idx_d]
                # apply point
                self.d_mat_area[y_cur, x_cur] += 1
        
        # count relevant points
        self.num_req_hvd = np.sum(oA.d_mat_area>=2);
        
        # Show Results
        print('Num H/V      >= 2: %d' % (self.num_req_hv))
        print('Num H/V/Diag >= 2: %d' % (self.num_req_hvd))
    
#------------------------------------------------------------------------------
# execute by file call
if __name__ == '__main__':   
    oA = AoC_2105_Calc()
    oA.get_file_data('aoc_2105_data.dat')
    oA.prep_data()
    oA.eval_data()

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:32:31 2021

@author: T. Katemann
@description: AoC 2021 04
"""

import os
import numpy as np

class AoC_2104_Calc:
    
    def __init__(self):
        self.str_cwd = os.getcwd()
        self.ar_data = np.array([])
        
        self.bVerbose = 0
        
        print('# AoC 21 04 init #')

    # read raw data from file
    def get_file_data(self, strFile):
        str_file_path = os.path.join(self.str_cwd,strFile)
        file = open(str_file_path, 'r')
        self.ar_data = np.array(file.readlines())
    
    # evaluate bin list
    def eval_data(self):
        
        # get number string for bingo
        self.ar_data_vec = np.array([ 
            int(i) for i in self.ar_data[0].split()[0].split(',') 
                if str(i).isnumeric()])
                
        print("BingoVector Length: %d" % (len(self.ar_data_vec)))
        print(self.ar_data_vec)
        
        # get matrix seperator        
        self.idx_vec = np.squeeze(np.where((oA.ar_data) == '\n'))
        self.idx_vec = np.append(self.idx_vec,
            self.idx_vec[-1]+(self.idx_vec[-1]-self.idx_vec[-2]))
        
        # extract matrices
        self.ar_data_mat=[]
        for idx in range(len(self.idx_vec)-1):
            ar_data_mat = np.array([ 
            [int(i) for i in str(x).split() if str(i).isnumeric()] 
            for x in self.ar_data[self.idx_vec[idx]+1:self.idx_vec[idx+1]]
            ])
            self.ar_data_mat.append(ar_data_mat)
        self.ar_data_mat = np.array(self.ar_data_mat)
        
        # init check bingo matrix
        self.ar_data_mat_check = np.zeros(self.ar_data_mat.shape, dtype=bool)

        # get shape of data set
        num_mat_cnt = (self.ar_data_mat_check.shape[0])
        num_mat_row = (self.ar_data_mat_check.shape[1])
        num_mat_col = (self.ar_data_mat_check.shape[2])
        print("MatrixCount: %d" % (num_mat_cnt))
        print("MatrixShape: %d x %d" % (num_mat_row,num_mat_col))   
        
        # flag
        bFirstFound = 0
        bLastFound = 0
        
        # init memory for prev result
        b_ar_win_mat_prev = np.zeros(num_mat_cnt, dtype=bool)
        
        # loop over numbers
        for idx in range(len(self.ar_data_vec)):
            
            # check numbers matching with bingo matrices
            self.ar_data_mat_check = np.bitwise_or(
                self.ar_data_mat_check, 
                self.ar_data_mat==self.ar_data_vec[idx])
            
            # bingo in any row for each matrix by bool vector
            b_bing_any_row = np.sum(
                self.ar_data_mat_check, axis=1) == num_mat_row
            # bingo in any colun for each matrix by bool vector
            b_bing_any_col = np.sum(
                self.ar_data_mat_check, axis=2) == num_mat_col
                
            # index of matrix win rows and cols and combined
            b_ar_win_mat_by_row = np.sum(b_bing_any_row, axis=1) > 0
            b_ar_win_mat_by_col = np.sum(b_bing_any_col ,axis=1) > 0
            b_ar_win_mat = np.bitwise_or(b_ar_win_mat_by_row, 
                                         b_ar_win_mat_by_col)
            
            if self.bVerbose == 1:
                print('# Idx'+ str(idx))
                print('# Num'+ str(self.ar_data_vec[idx]))            
                print(b_ar_win_mat)

            # find first winner
            if bFirstFound == 0:
                if (b_ar_win_mat).any():
                    # store properties of first bingo
                    self.b_ar_win_mat_first = b_ar_win_mat
                    self.d_win_num_val = self.ar_data_vec[idx]
                    self.d_win_num_idx = idx
                    self.mat_win = self.ar_data_mat[b_ar_win_mat]
                    self.mat_win_check = self.ar_data_mat_check[b_ar_win_mat]
                    bFirstFound = 1
                
            # find last winner
            if bLastFound == 0:
                if (b_ar_win_mat).all():
                    
                    b_ar_win_last = (
                        np.bitwise_and(b_ar_win_mat, b_ar_win_mat_prev) == 0)
                    # store properties of last bingo
                    self.b_ar_win_mat_last = b_ar_win_last
                    self.d_win_num_val2 = self.ar_data_vec[idx]
                    self.d_win_num_idx2 = idx
                    self.mat_win2 = self.ar_data_mat[b_ar_win_last]
                    self.mat_win_check2 = self.ar_data_mat_check[b_ar_win_last]
                    bLastFound = 1
                    break
            
            # mem status for next round
            b_ar_win_mat_prev = b_ar_win_mat
                
        #----------------------------------------------------------------------
        # Results:
 
        mat_win_val = sum(self.mat_win[self.mat_win_check==0])
        print('## P1 Result ##')
        #print(self.b_ar_win_mat_first)
        print('bingo idx     : '+str(self.d_win_num_idx))
        print('bingo val     : '+str(self.d_win_num_val))
        print('sum unchecked : '+str(mat_win_val))
        print('p1 result     : '+str(mat_win_val*self.d_win_num_val))
        
        mat_win_val2 = sum(self.mat_win2[self.mat_win_check2==0])
        print('## P2 Result ##')
        #print(self.b_ar_win_mat_last)
        print('bingo idx     : '+str(self.d_win_num_idx2))
        print('bingo val     : '+str(self.d_win_num_val2))
        print('sum unchecked : '+str(mat_win_val2))
        print('p2 result     : '+str(mat_win_val2*self.d_win_num_val2))
        
#------------------------------------------------------------------------------
# execute by file call
if __name__ == '__main__':   
    oA = AoC_2104_Calc()
    oA.get_file_data('aoc_2104_data.dat')
    oA.eval_data()
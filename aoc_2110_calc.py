# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 06:42:55 2021

@author: T. Katemann
@description: AoC 2021 10
"""

import numpy as np

class AoC_2110_Calc:
    
    def __init__(self):
        self.ar_data = np.array([])
        self.pairs={"{":"}","(":")","[":"]","<":">"}
        self.score={"}":1197,")":3,"]":57,">":25137}
        self.score2={"{":3,"(":1,"[":2,"<":4}
        self.str_open = "([{<"
        self.str_close = ">}])"
        
        self.b_verbose = 0
        print('# AoC 21 10 init #')
        

    # read raw data from file
    def get_file_data(self, strFile):
        file = open(strFile, 'r')
        self.ar_data = (file.read().splitlines())

    def eval_data(self):
        # string array to num array
        self.ar_score2_sum =[]
        sum_err_score=0
        for str_cur in self.ar_data:
            bRes1 = self.chk_bal1(str_cur)
            bRes2,stack = self.chk_bal2(str_cur)
            if bRes2>0:
                if self.b_verbose:
                    print('corrupt',bRes1)
            else:
                if bRes1:
                    if self.b_verbose:
                        print('correct', bRes1)
                else:
                    if self.b_verbose:
                        print('incomplete', bRes1, stack)
                    sum1 = 0
                    for idx in range(len(stack)):
                        idxi = len(stack)-idx-1
                        sum1 = (sum1*5)+self.score2[stack[idxi]]
                    self.ar_score2_sum.append(sum1)
                    
            sum_err_score+=bRes2
        print("P1 SumScore:",sum_err_score)
        
        med=(
            np.round(
                np.median(np.array(oA.ar_score2_sum,dtype=int))))
        print('P2 Median',med)
    
    # check any balance
    def chk_bal1(self,str_pat):
        
        stack = []
        for chr_cur in str_pat:
            if chr_cur in self.str_open:
                stack.append(chr_cur)
            elif stack and chr_cur in self.str_close:
                stack.pop()
            else:
                return False
            
        return len(stack) == 0
   
   # check excact balance
    def chk_bal2(self,str_pat):

        stack = []
        for chr_cur in str_pat:
            if chr_cur in self.str_open:
                stack.append(chr_cur)
            elif stack and chr_cur==self.pairs[stack[-1]]:
                stack.pop()
            else:
                return self.score[chr_cur], stack
            
        return 0, stack
    

#------------------------------------------------------------------------------
# execute by file call
if __name__ == '__main__':   
    oA = AoC_2110_Calc()
    oA.get_file_data('aoc_2110_data.dat')
    oA.eval_data()


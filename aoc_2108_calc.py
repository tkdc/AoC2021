# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:56:59 2021

@author: T. Katemann
@description: AoC 2021 08
"""

import numpy as np
import difflib as dl

class AoC_2108_Calc:
    
    def __init__(self):
        self.ar_data = np.array([])

        print('# AoC 21 08 init #')
        self.dig_map = ['cagedb','ab','gcdfa','fbcad','eafb','cdfbe',
        'cdfgeb','dab','acedgfb','cefabd']

    # read raw data from file
    def get_file_data(self, strFile):
        file = open(strFile, 'r')
        self.ar_data = (file.read().splitlines())

    def prep_data(self):
        # string array to num array
        self.ar_data_seq = []
        for seq in self.ar_data:
            seq1, seq2 = seq.split(' | ')
            self.ar_data_seq.append([seq1.split(), seq2.split()])
        print("Num Seq Init: %d" % (len(self.ar_data_seq)))
           
    # evaluate data a
    def eval_data(self):
        note1 = self.ar_data_seq[0][1][0]
        print(note1)
        self.sum_m_tot = 0
        for seq in self.ar_data_seq:
            ar_seq2_len = np.array(list(map(len,seq[1])))
            sum_m = sum(ar_seq2_len==2)+sum(ar_seq2_len==3)\
              +sum(ar_seq2_len==4)+sum(ar_seq2_len==7)
            self.sum_m_tot += sum_m
            
        print(self.sum_m_tot)

        for seq in self.ar_data_seq:
            print('#####')
            for note1 in seq[1]:
                
                note1_sort = ''.join(sorted(note1))
                print()
                print(note1_sort)
                self.match_vec = np.zeros(10,dtype=int)
                self.match_vec2 = np.zeros(10,dtype=int)
                for idx_dig in range(len(self.dig_map)):
                    dig = self.dig_map[idx_dig]
                    dig_seq = seq[0][idx_dig]
                    
                    dig_sort = ''.join(sorted(dig))
                    dig_seq_sort = ''.join(sorted(dig_seq))
                    
                    seqm_1 = dl.SequenceMatcher(None,note1_sort,dig_seq_sort)
                    seqm_2 = dl.SequenceMatcher(None,note1_sort,dig_sort)
                    
                    rqr1 = seqm_1.real_quick_ratio()
                    rqr2 = seqm_2.real_quick_ratio()
                    self.seqm_1 = seqm_1
                    if rqr1 > 0.9999:
                        print(str(seqm_1.ratio())+' '\
                        +str(seqm_1.real_quick_ratio())+' '+dig_seq_sort)
                        mb = seqm_1.get_matching_blocks()
                        #print(mb)
                        asize = np.array([x.size for x in mb])
                        asize[asize==0] = 1
                        print("idx: %d, sum: %d" % (idx_dig,sum(asize)))
                        self.match_vec[idx_dig] = sum(asize)
                        
                    if rqr2 > 0.9999:
                        print(str(seqm_2.ratio())+' '\
                        +str(seqm_2.real_quick_ratio())+' '+dig_sort)
                        mb = seqm_2.get_matching_blocks()
                        #print(mb)
                        asize = np.array([x.size for x in mb])
                        asize[asize==0] = 1
                        print("B idx: %d, sum: %d" % (idx_dig,sum(asize)))
                        self.match_vec2[idx_dig] = sum(asize)                  
                        
                        
                        
                idx_max = np.argmax(self.match_vec)
                print(idx_max)
                idx_max = np.argmax(self.match_vec2)
                print(idx_max)



#------------------------------------------------------------------------------
# execute by file call
if __name__ == '__main__':   
    oA = AoC_2108_Calc()
    oA.get_file_data('aoc_2108_data.dat')
    oA.prep_data()
    oA.eval_data()


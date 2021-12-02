# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:34:06 2021

@author: tk
@description: AoC 2021 02
"""

import os

class AoC_2102_Calc:
    
    def __init__(self):
        
        # public parameter
        self.str_cwd = os.getcwd()
        self.ar_op_list = []
        
        self.d_count_op = 0
        self.d_pos_horz = 0
        self.d_pos_vert = 0
        self.d_pos_aim = 0
        self.d_pos_vert_aim = 0
        
        self.veh_ops = {
            'forward': self.forward,
            'down': self.down,
            'up':self.up}
            
        print('# Aoc21 02 init #')
    
    def get_file_data(self, strFile):
        str_file_path = os.path.join(self.str_cwd, strFile)
        file = open(str_file_path, 'r')
        self.ar_op_list = file.readlines()
        
    # move forward
    def forward(self, x):
        self.d_pos_horz = self.d_pos_horz + x # P1
        self.d_pos_vert_aim = self.d_pos_vert_aim + self.d_pos_aim * x # P2
        self.d_count_op = self.d_count_op + 1
    
    # move down
    def down(self, x):
        self.d_pos_vert = self.d_pos_vert + x # P1
        self.d_pos_aim  = self.d_pos_aim + x  # P2
        self.d_count_op = self.d_count_op + 1
    
    # move up
    def up(self, x):
        self.d_pos_vert = self.d_pos_vert - x # P1
        self.d_pos_aim  = self.d_pos_aim - x  # P2
        self.d_count_op = self.d_count_op + 1
    
    # vehicle operate
    def call_op(self, act_op, value):
        if act_op in self.veh_ops:
            if str(value).isnumeric(): # check value
                # call specific operation
                self.veh_ops[act_op](int(value))
            else:
                self.disp_error(act_op, value)
        else:
            self.disp_error(act_op, value)

    # call operation list
    def eval_op_list(self):
        print("HorzPos: %d" % (self.d_pos_horz))
        print("VertPos: %d" % (self.d_pos_vert))
        
        for act_op in self.ar_op_list:
            # clean and split input
            act_op_split = (" ".join(act_op.strip().split())).split()
            if len(act_op_split) == 2:
                # call operation
                self.call_op(act_op_split[0],act_op_split[1])
            else:
                self.disp_error(act_op, '')
        
        # Print result
        print("-Operated: %d of %d" % (self.d_count_op, len(self.ar_op_list)))
        print("HorzPos : %d" % (self.d_pos_horz))
        print("VertPos : %d" % (self.d_pos_vert))
        print("VertAim: %d" % (self.d_pos_aim))
        print("VertPosA: %d" % (self.d_pos_vert_aim))
        print("ResultP1: %d" % (self.d_pos_vert*self.d_pos_horz))
        print("ResultP2: %d" % (self.d_pos_vert_aim*self.d_pos_horz))
        
    # display error
    def disp_error(self, act_op, value):
        print("# No Valid Op: L%d : %s : %s" % 
            (self.d_count_op+1, act_op, value))

# execute by file call
if __name__ == '__main__':   
    oAoC02 = AoC_2102_Calc()
    oAoC02.get_file_data('aoc_2102_data.dat')
    oAoC02.eval_op_list()


#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

import os
import argparse
import sys
import subprocess
import git 
import re

list to str
cmd = ''.join(p_name)


def read_file():
    chip_name = raw_input("Please input chip name:")
    file_name = chip_name+'.pd'
    try:
        with open(file_name, 'r') as f:
            return f.readlines()
    except IOError:
        print("ERROR: not found file:%s" % file_name)
        sys.exit(1)
        
if __name__ == '__main__':
    if not os.environ['SDK']:
        print("Please set $SDK environment variable")
        sys.exit(1)
    else:
        print("SDK: {}".format(os.environ['SDK']))
		

def diff(left_file, right_file):
    try:
        resultList = []
#        cmd = ["diff", left_file, right_file]
        cmd = ["diff", './nfa_0_1_0/bcm56880_a0_nfa_0_1_0_rate.c', './dna_4_6_6/bcm56880_a0_dna_4_6_6_rate.c']
        resultList = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        print resultList
        return resultList
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
#        sys.exit(1)  
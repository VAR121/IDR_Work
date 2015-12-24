#!/usr/bin/env python3
#Date: Dec-23-2015
#Purpose: Extract D and O blocks
#Input: Intermediate file generted by "homo_block_msa_extraction.py script"

import sys

file1 = sys.argv[1]
IN1 = open(file1, 'r')

inp_1 = IN1.readlines()
inp_1 = list(map(str.strip, inp_1))

start = others = end = 0
threshold = 3
In_O = In_D = False

for i in range(0, len(inp_1)):

    if(inp_1[i] == "D" and not In_O):

        if(start == 0):
            start = i+1

        if (i < len(inp_1) - threshold):

            n_list = inp_1[i+1:i+threshold+1]
            In_D = True
            others = n_list.count("O") + n_list.count("N")

            if(others == threshold):
                end = i + 1
                if(end - start >= threshold):
                    print ("D", start, end)
                    In_D = False
                    start = 0
                    continue
        else:
            end = len(inp_1)
            print("D", start, end)
            break

    if(inp_1[i] == "O" and not In_D):

        if(start == 0):
            start = i+1

        if (i < len(inp_1) - threshold):

            n_list = inp_1[i+1:i+threshold+1]

            In_O = True

            others = n_list.count("D") + n_list.count("N")

            if (others == threshold):
                end = i + 1
                if(end - start >= threshold):
                    print("O", start, end)
                    In_O = False
                    start = 0
                    continue
        else:
            end = len(inp_1)
            print("O", start, end)
            break
exit(0)

#!/usr/bin/python3
#Date: 2nd Dec 2015
#Purpose: Take out Disorder Order block
#Input_file: Intermediate file generated from dis_bound_homo_block_msa_extraction.py (*.int)

import sys

in_1 = sys.argv[1]

inp_1 = open(in_1, 'r')
input_lines_1 = inp_1.readlines()
inp_1.close()

length_1 = len(input_lines_1)

sres = 0
d_count = 0
o_count = 0
n_count = 0
eres = 0

line = 0

while line < length_1:

    in_file = input_lines_1[line]
    lines = in_file.strip('\n')

    if lines == "D":

        if d_count == 0:
            sres = line + 1  # Starting boundary

        d_count += 1

        if n_count < 4:
            n_count = 0
        if o_count < 4:
            o_count = 0

    if (d_count != 0) and lines == "O":
        o_count += 1

    if (d_count != 0) and lines == "N":
        n_count += 1

    if (d_count != 0) and ((o_count == 4) or (n_count == 4) or ((o_count + n_count) == 4)):

        if (d_count <= 3):
            o_count = n_count = d_count = sres = 0
            line += 1
            continue

        eres = (line - 3)
        line = eres

        print("D", sres, eres, sep='\t')

    if eres > 0:
        sres = 0
        d_count = 0
        o_count = 0
        n_count = 0
        eres = 0

    line += 1


sres = eres = line = 0

while line < length_1:

    in_file = input_lines_1[line]
    lines = in_file.strip('\n')

    if lines == "O":

        if o_count == 0:
            sres = line + 1  # Starting boundary

        o_count += 1

        if n_count < 4:
            n_count = 0
        if d_count < 4:
            d_count = 0

    if (o_count != 0) and lines == "D":
        d_count += 1

    if (o_count != 0) and lines == "N":
        n_count += 1

    if (o_count != 0) and ((d_count == 4) or (n_count == 4) or ((d_count + n_count) == 4)):

        if (o_count <= 3):
            o_count = n_count = d_count = sres = 0
            line += 1
            continue

        eres = (line - 3)
        line = eres

        print("O", sres, eres, sep='\t')
        # print("Diag", line, o_count)

    if eres > 0:
        sres = 0
        d_count = 0
        o_count = 0
        n_count = 0
        eres = 0

    line += 1

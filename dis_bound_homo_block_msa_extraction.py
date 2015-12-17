#!/usr/bin/python3
#Date: 10-11-15
#Purpose: Extract sequence without gaps MSA using species name
#Input file: Multiple Sequence Alignment File (MSA)

import sys
import re
import pprint
from collections import Counter

in_1 = sys.argv[1]
out_file = in_1.replace("_sel_ortho_seq.cw.aln", ".don.int")
out = open(out_file, "w")

inp_1 = open(in_1, 'r')
input_lines_1 = inp_1.readlines()
inp_1.close()

length_1 = len(input_lines_1)

sp_list = dict()
sp_list = {'QueryDom': None,
           'Monodelphisdomestica': None,
           'Pongoabelii': None,
           'Bostaurus': None,
           'Equuscaballus': None,
           'Canislupusfamiliaris': None,
           'Caviaporcellus': None,
           'Rattusnorvegicus': None,
           'Musmusculus': None,
           'Macacamulatta': None,
           'Pantroglodytes': None}

sp_list_keys = ['QueryDom',
                'Monodelphisdomestica',
                'Pongoabelii',
                'Bostaurus',
                'Equuscaballus',
                'Canislupusfamiliaris',
                'Caviaporcellus',
                'Rattusnorvegicus',
                'Musmusculus',
                'Macacamulatta',
                'Pantroglodytes']

for line in range(3, length_1):

    line = input_lines_1[line].strip("\n")
    if not (re.match("^[A-Z]", line)):
        continue

    words = line.split()

    sps_name = words[0]
    seq = words[1]

    if sps_name in sp_list:

        if (sp_list[sps_name] is None):
            sp_list[sps_name] = seq
        else:
            sp_list[sps_name] = sp_list[sps_name] + seq

d_dict = dict()

for key in sp_list_keys:

    if (sp_list[key] is not None):
        sp_list[key] = list(sp_list[key])

        d_file = in_1
        d_str = key + ".diso"
        d_file = d_file.replace("sel_ortho_seq.cw.aln", d_str)

        d_f = open(d_file, 'r')
        d_lines = d_f.readlines()
        d_f.close()

        pred_list = list()

        d_dict[key] = None

        temp_list = sp_list[key]

        cur = -1   #  For counting the position

        for i in range(0, len(temp_list)):

            if (re.match("[A-Z]", temp_list[i])):
                cur += 1

                current = d_lines[cur + 3].strip('\n')
                words = current.split()

                if(float(words[3]) >= 0.5):
                    status = "D"
                    pred_list.extend(status)
                else:
                    status = "O"
                    pred_list.extend(status)
            else:
                status = "N"
                pred_list.extend(status)

        d_dict[key] = pred_list


def red(name):
    print ("\033[91m{}\033[00m" .format(name), end="")


def green(name):
    print ("\033[92m{}\033[00m" .format(name), end="")


def yellow(name):
    print ("\033[93m{}\033[00m" .format(name), end="")

# for i in sp_list_keys:
#     if (sp_list[i] is not None):
#         d_list = d_dict[i]
#         a_list = sp_list[i]
#         # print(i,":",end="", sep="")
#         for j in range(0, len(d_list) - 1):
#             if (d_list[j] == "D"):
#                 red(a_list[j])
#             else:
#                 print(a_list[j], end="")
#     print()

q_dom_d_list = d_dict["QueryDom"]
length = len(q_dom_d_list)
stat_list = list()

for i in range(0, length):
    cur_block = list()

    for j in sp_list_keys:
        temp_list = d_dict[j]
        cur_ele = temp_list[i]
        cur_block.extend(cur_ele)

    counts = Counter(cur_block)

    d_per = float(counts["D"] / len(cur_block))
    o_per = float(counts["O"] / len(cur_block))
    n_per = float(counts["N"] / len(cur_block))

    if(n_per >= 0.5):
        stat_list.extend("N")
        for m in cur_block:
            yellow(m)

    elif(d_per > o_per):

        stat_list.extend("D")
        for k in cur_block:
            red(k)

    elif(o_per > d_per):

        stat_list.extend("O")
        for l in cur_block:
            green(l)

    elif(d_per == o_per):

        stat_list.extend("N")
        for m in cur_block:
            yellow(m)

    else:

        stat_list.extend("N")
        for m in cur_block:
            yellow(m)

    # print("", d_per, o_per, n_per)
    print()


for i in range(0, length):
    print(stat_list[i], file=out)

exit()

#!/usr/bin/python3
#Date: 15th June 2016
#Purpose: To get final Helix and Sheet position from pdbs
#Input_file : output file of uid_mapping_pdb_map.py (*.pdb_all)
#Outout_file : final helix and sheet positions as per uid psitions
#Author : Rakesh Trivedi

import sys
import pprint as pp
in_1 = sys.argv[1]

inp_1 = open(in_1, 'r')
Input_file_1 = inp_1.readlines()
inp_1.close()

helix = list()
sheet = list()

for struc in range(0, len(Input_file_1)):

    struc_line = Input_file_1[struc]
    struc_line = struc_line.strip('\n')

    fields = struc_line.split()

    if (fields[0] == "HELIX"):
        temp_list = list(range(int(fields[2]), int(fields[4]) + 1))
        helix.extend(temp_list)
    else:
        temp_list = list(range(int(fields[2]), int(fields[4]) + 1))
        sheet.extend(temp_list)

helix = sorted(list(set(helix)), key=int)
sheet = sorted(list(set(sheet)), key=int)

start = end = None

for res in range(0, len(helix)):

    if(start == None):
        start = helix[res]
    elif ((res == len(helix) - 1) or ((helix[res] + 1) != (helix[res + 1]))):
        end = helix[res]
        print("HELIX", start, end, sep="\t")
        start = end = None

start = end = None

for res in range(0, len(sheet)):

    if(start == None):
        start = sheet[res]
    elif ((res == len(sheet) - 1) or ((sheet[res] + 1) != (sheet[res + 1]))):
        end = sheet[res]
        print("SHEET", start, end, sep="\t")
        start = end = None

exit(0)

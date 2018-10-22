#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import codecs
import random
import math

### Random seat placement script for Yoyo ###
list_1280, list_880, list_580 = [], [], []
with codecs.open("/Users/Ying/Desktop/1_nknanjing.csv","r","utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    for row in reader:
        row = row[0].split(",")
        if row[2].strip() == '1280':
            list_1280.append(row[1].strip())
        if row[2].strip() == '880':
            list_880.append(row[1].strip())
        if row[2].strip() == '580':
            list_580.append(row[1].strip())
        
print("1280 ordered: ", list_1280)
print("880 ordered: ", list_880)
print("580 ordered: ", list_580)
random.shuffle(list_1280)
random.shuffle(list_880)
random.shuffle(list_580)
print("\n1280 random: ", list_1280)
print("\n880 random: ", list_880)
print("\n580 random: ", list_580)

for l in [{'group':'1280','list':list_1280},
          {'group':'880','list':list_880},
          {'group':'580','list':list_580}]:
    group = l['group']
    names = l['list']
    print ("\nSection {0}".format(group), end=" ")
    rows = int(math.ceil(len(names)/20))
    remainder = len(names) % 20
    for i in range(rows):
        print("\nrow {0}:".format(i+1), end=" ")
        if i == (rows-1):
            for j in range(len(names)-i*20):
                print(names[i*20+j], end=" ")
        else:
            for j in range(20):
                print(names[i*20+j], end=" ")
    print("\n")

import numpy as np
import sys
import os
import re
from paper_dictionary import paper_dict


for paper_name in paper_dict.keys():
    paper = paper_dict[paper_name]
    authors = paper['authors'].split(",")
    lasts = [name.split(" ")[-1] for name in authors]
    firsts = [list(filter(None, name.split(" ")[:-1])) for name in authors]
    for i in range(len(firsts)):
        if len(firsts[i]) == 4:
            temp = firsts[i][1]+firsts[i][2]
            firsts[i] = [firsts[i][0], temp, firsts[i][3]]

    comb_firsts = [" ".join(name) for name in firsts]

    authors_new = ["{"+l+"}, "+f for l,f in zip(lasts,comb_firsts)]

    full_list = " and ".join(authors_new)

    outfile = paper_name + "_bibtex.bib"
    with open(outfile, "w") as f:
        print("@ARTICLE{2021_"+paper_name+"_in_press,", file=f)
        print("       author = {"+full_list+"},", file=f)
        print('       title = "{'+paper['title']+'}",', file=f)
        print("       journal = {\\apjs},", file=f)
        print("       year = 2021,", file=f)
        print("       volume = {in press},", file=f)
        print("       archivePrefix = {arXiv},", file=f)
        print("       eprint = {2006.16187},", file=f)
        print("}", file=f)

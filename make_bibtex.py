import numpy as np
import sys
import os
import re


with open("authors_per_paper.txt") as authFile:
    authors_per_paper = authFile.readlines()


for paper in authors_per_paper:
    authors = paper.split(",")
    lasts = [name.split(" ")[-1] for name in authors]
    firsts = [list(filter(None, name.split(" ")[:-1])) for name in authors]
    for i in range(len(firsts)):
        if len(firsts[i]) == 4:
            temp = firsts[i][1]+firsts[i][2]
            firsts[i] = [firsts[i][0], temp, firsts[i][3]]

    comb_firsts = [" ".join(name) for name in firsts]

    new = ["{"+l+"}, "+f for l,f in zip(lasts,comb_firsts)]

    print(new)




'''
with open("project_dirs.txt") as dirFile:
    for projid, line in enumerate(dirFile):
        stage_37_log = line[:-1]+"weblog/stage37/casapy.log"

        lookup = "tclean::::casa	tclean( vis="

        num_lock=None
        with open(stage_37_log) as logFile:
            for num, logline in enumerate(logFile, 1):
                if lookup in logline:
                    print('found at line:', num)
                    command_master = logline[40:]
                    break

        outfile = "tclean_commands_" + projects[projid][:-1] + ".py"
        if not os.path.exists(projects[projid][:-1]):
            os.makedirs(projects[projid][:-1])
        with open(outfile, "w") as f:
            print('casalog.filter("INFO3")', file=f)
            print("", file=f)
            command = command_master
            command = command.replace("/lustre/naasc/sciops/comm/cbrogan/pipeline/root/", "/lustre/naasc/sciops/comm/cbrogan/pipeline/root/Benchmark_2020/")
            command = command.replace("imagename='", "imagename='"+projects[projid][:-1]+"/")
            command = command.replace("iter0',", "iter0.pcwdF',")
            command = command.replace("parallel=False", "parallel=True")
'''

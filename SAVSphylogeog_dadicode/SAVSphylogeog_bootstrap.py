#!/usr/bin/env python 

import numpy.random as npr
import dadi
import os

usage="""
import dadi input file 
randomly sample snps with replacement from MARKERS column
which contains info on locus and snp location 
"""

InFileName = "dadi_input_finaldataset_3Jan2017.tsv"
InFile = open(InFileName, 'r')
LineNum = 0
GeneDict = {}
header = ''
for line in InFile:
	if LineNum == 1:
		header = line
	elif LineNum > 1:
		line = line.strip('\n')
		newline = line.split('\t')
		PosKey= newline[8]
		GeneDict[PosKey] = line
	LineNum += 1	
Data = GeneDict.keys()	
print len(Data)	


for i in range(100):
	print i	
	perturb = npr.choice(Data,size=(1,len(Data)),replace=True)
	OutFileName = "bootstraps/tempsnpfile_%d.txt" % i
	OutFile = open(OutFileName, 'w')
	OutFile.write("#dadi SNP input file\n")
	OutFile.write(header)
	for list in perturb:
		UniqueId = 0
		for gene in list:
			output = "%s_%s\n" % (GeneDict[gene],str(UniqueId))
			OutFile.write(output)
			UniqueId += 1
	OutFile.close()		

for boot in range(100):
	OutBootName = "bootstraps/fsboot_%d" % boot
	file = 	"bootstraps/tempsnpfile_%d.txt" % boot
	dd = dadi.Misc.make_data_dict(file)
	FoldedSpec = dadi.Spectrum.from_data_dict(dd, ['CON','MEX'], [25,16], polarized=False)	
	FoldedSpec.to_file(OutBootName)							  
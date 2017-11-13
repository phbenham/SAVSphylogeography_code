#!/usr/local/bin/bash
nsam='163'
nreps='100000'
mkdir 1popAnalysis/mtDNA_constantB

#ms commands based on the range of population sizes from 500,000 to 1,650,00 and best parameter estimates form ∂a∂i
ms ${nsam} ${nreps} -t 5.73 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.630 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_1
ms ${nsam} ${nreps} -t 6.30 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.573 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_2
ms ${nsam} ${nreps} -t 6.87 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.525 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_3
ms ${nsam} ${nreps} -t 7.44 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.485 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_4
ms ${nsam} ${nreps} -t 8.02 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.450 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_5
ms ${nsam} ${nreps} -t 8.59 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.420 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_6
ms ${nsam} ${nreps} -t 9.16 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.394 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_7
ms ${nsam} ${nreps} -t 9.73 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.371 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_8
ms ${nsam} ${nreps} -t 10.31 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.350 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_9
ms ${nsam} ${nreps} -t 10.88 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.332 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_10
ms ${nsam} ${nreps} -t 11.45 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.315 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_11
ms ${nsam} ${nreps} -t 12.02 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.300 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_12
ms ${nsam} ${nreps} -t 12.60 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.287 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_13
ms ${nsam} ${nreps} -t 13.17 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.274 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_14
ms ${nsam} ${nreps} -t 13.74 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.263 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_15
ms ${nsam} ${nreps} -t 14.31 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.252 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_16
ms ${nsam} ${nreps} -t 14.89 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.242 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_17
ms ${nsam} ${nreps} -t 15.46 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.234 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_18
ms ${nsam} ${nreps} -t 16.03 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.225 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_19
ms ${nsam} ${nreps} -t 16.60 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.217 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_20
ms ${nsam} ${nreps} -t 17.18 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.210 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_21
ms ${nsam} ${nreps} -t 17.75 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.203 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_22
ms ${nsam} ${nreps} -t 18.32 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.197 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_23
ms ${nsam} ${nreps} -t 18.89 -es 0 1 0.97 -en 0 1 0.49 -en 0 2 0.51 -ej 0.191 2 1 | sample_stats >1popAnalysis/mtDNA_constantB/outfile_24

#remove labels from sample_stats output to facilitate import and processing in r
END=24
for i in $(seq 1 $END)
do
	cat ./1popAnalysis/mtDNA_constantB/outfile_$i | sed -E 's/[A-z]+\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)/\1	\2	\3	\4	\5/g' >./1popAnalysis/mtDNA_constantB/outfile_finalout_$i
	rm ./1popAnalysis/mtDNA_constantB/outfile_$i
done
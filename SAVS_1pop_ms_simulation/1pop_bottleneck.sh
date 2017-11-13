#!/usr/local/bin/bash
nsam='163'
nreps='100000'
mkdir 1popAnalysis/BottleOut

#ms commands based on the range of population sizes from 500,000 to 1,650,00 and best parameter estimates form ∂a∂i
ms ${nsam} ${nreps} -t 5.73 -eN 0.119 0.14 -eN 0.674 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_1
ms ${nsam} ${nreps} -t 6.30	-eN 0.109 0.14 -eN 0.612 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_2
ms ${nsam} ${nreps} -t 6.87 -eN 0.100 0.14 -eN 0.561 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_3
ms ${nsam} ${nreps} -t 7.44	-eN 0.092 0.14 -eN 0.518 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_4
ms ${nsam} ${nreps} -t 8.02	-eN 0.085 0.14 -eN 0.481 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_5
ms ${nsam} ${nreps} -t 8.59	-eN 0.080 0.14 -eN 0.449 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_6
ms ${nsam} ${nreps} -t 9.16	-eN 0.075 0.14 -eN 0.421 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_7
ms ${nsam} ${nreps} -t 9.73	-eN 0.070 0.14 -eN 0.396 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_8
ms ${nsam} ${nreps} -t 10.31 -eN 0.066 0.14 -eN 0.374 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_9
ms ${nsam} ${nreps} -t 10.88 -eN 0.063 0.14 -eN 0.355 0.004	| sample_stats >1popAnalysis/BottleOut/outfile_10
ms ${nsam} ${nreps} -t 11.45 -eN 0.060 0.14 -eN 0.337 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_11
ms ${nsam} ${nreps} -t 12.02 -eN 0.057 0.14 -eN 0.321 0.004	| sample_stats >1popAnalysis/BottleOut/outfile_12	
ms ${nsam} ${nreps} -t 12.60 -eN 0.054 0.14 -eN 0.306 0.004	| sample_stats >1popAnalysis/BottleOut/outfile_13
ms ${nsam} ${nreps} -t 13.17 -eN 0.052 0.14 -eN 0.293 0.004	| sample_stats >1popAnalysis/BottleOut/outfile_14
ms ${nsam} ${nreps} -t 13.74 -eN 0.050 0.14 -eN 0.281 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_15	
ms ${nsam} ${nreps} -t 14.31 -eN 0.048 0.14 -eN 0.269 0.004	| sample_stats >1popAnalysis/BottleOut/outfile_16
ms ${nsam} ${nreps} -t 14.89 -eN 0.046 0.14 -eN 0.259 0.004	| sample_stats >1popAnalysis/BottleOut/outfile_17
ms ${nsam} ${nreps} -t 15.46 -eN 0.044 0.14 -eN 0.249 0.004| sample_stats >1popAnalysis/BottleOut/outfile_18
ms ${nsam} ${nreps} -t 16.03 -eN 0.043 0.14	-eN 0.241 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_19
ms ${nsam} ${nreps} -t 16.60 -eN 0.041 0.14 -eN 0.232 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_20
ms ${nsam} ${nreps} -t 17.18 -eN 0.040 0.14	-eN 0.225 0.004| sample_stats >1popAnalysis/BottleOut/outfile_21
ms ${nsam} ${nreps} -t 17.75 -eN 0.039 0.14 -eN 0.217 0.004| sample_stats >1popAnalysis/BottleOut/outfile_22
ms ${nsam} ${nreps} -t 18.32 -eN 0.037 0.14 -eN 0.210 0.004	| sample_stats >1popAnalysis/BottleOut/outfile_23
ms ${nsam} ${nreps} -t 18.89 -eN 0.036 0.14	-eN 0.204 0.004 | sample_stats >1popAnalysis/BottleOut/outfile_24

#remove labels from sample_stats output to facilitate import and processing in r
END=24
for i in $(seq 0 $END)
do
	cat ./1popAnalysis/BottleOut/outfile_$i | sed -E 's/[A-z]+\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)/\1	\2	\3	\4	\5/g' >./1popAnalysis/BottleOut/outfile_finalout_$i
	rm ./1popAnalysis/BottleOut/outfile_$i
done
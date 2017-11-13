#!/usr/local/bin/bash
nsam='163'
nreps='100000'
mkdir 1popAnalysis/ConstantOut

#ms commands based on the range of population sizes from 500,000 to 1,650,00 and best parameter estimates form ∂a∂i
ms ${nsam} ${nreps} -t 5.73 | sample_stats >1popAnalysis/ConstantOut/Constant_01
ms ${nsam} ${nreps} -t 6.30	| sample_stats >1popAnalysis/ConstantOut/Constant_02
ms ${nsam} ${nreps} -t 6.87	| sample_stats >1popAnalysis/ConstantOut/Constant_03
ms ${nsam} ${nreps} -t 7.44	| sample_stats >1popAnalysis/ConstantOut/Constant_04
ms ${nsam} ${nreps} -t 8.02	| sample_stats >1popAnalysis/ConstantOut/Constant_05
ms ${nsam} ${nreps} -t 8.59	| sample_stats >1popAnalysis/ConstantOut/Constant_06
ms ${nsam} ${nreps} -t 9.16	| sample_stats >1popAnalysis/ConstantOut/Constant_07
ms ${nsam} ${nreps} -t 9.73	| sample_stats >1popAnalysis/ConstantOut/Constant_08
ms ${nsam} ${nreps} -t 10.31	| sample_stats >1popAnalysis/ConstantOut/Constant_09
ms ${nsam} ${nreps} -t 10.88	| sample_stats >1popAnalysis/ConstantOut/Constant_10
ms ${nsam} ${nreps} -t 11.45	| sample_stats >1popAnalysis/ConstantOut/Constant_11
ms ${nsam} ${nreps} -t 12.02	| sample_stats >1popAnalysis/ConstantOut/Constant_12	
ms ${nsam} ${nreps} -t 12.60	| sample_stats >1popAnalysis/ConstantOut/Constant_13
ms ${nsam} ${nreps} -t 13.17	| sample_stats >1popAnalysis/ConstantOut/Constant_14
ms ${nsam} ${nreps} -t 13.74	| sample_stats >1popAnalysis/ConstantOut/Constant_15	
ms ${nsam} ${nreps} -t 14.31	| sample_stats >1popAnalysis/ConstantOut/Constant_16
ms ${nsam} ${nreps} -t 14.89	| sample_stats >1popAnalysis/ConstantOut/Constant_17
ms ${nsam} ${nreps} -t 15.46	| sample_stats >1popAnalysis/ConstantOut/Constant_18
ms ${nsam} ${nreps} -t 16.03	| sample_stats >1popAnalysis/ConstantOut/Constant_19
ms ${nsam} ${nreps} -t 16.60	| sample_stats >1popAnalysis/ConstantOut/Constant_20
ms ${nsam} ${nreps} -t 17.18	| sample_stats >1popAnalysis/ConstantOut/Constant_21
ms ${nsam} ${nreps} -t 17.75	| sample_stats >1popAnalysis/ConstantOut/Constant_22
ms ${nsam} ${nreps} -t 18.32	| sample_stats >1popAnalysis/ConstantOut/Constant_23
ms ${nsam} ${nreps} -t 18.89	| sample_stats >1popAnalysis/ConstantOut/Constant_24

#remove labels from sample_stats output to facilitate import and processing in r
END=24
for i in $(seq 0 $END)
do
	cat ./1popAnalysis/ConstantOut/Constant_$i | sed -E 's/[A-z]+\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)/\1	\2	\3	\4	\5/g' >./1popAnalysis/ConstantOut/Constant_finalout_$i
	rm ./1popAnalysis/ConstantOut/Constant_$i
done
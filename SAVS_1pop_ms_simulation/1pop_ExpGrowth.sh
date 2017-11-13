#!/usr/local/bin/bash
nsam='163'
nreps='100000'
mkdir 1popAnalysis/ExpGrow

#ms commands based on the range of population sizes from 500,000 to 1,650,00 and best parameter estimates form ∂a∂i
ms ${nsam} ${nreps} -t 5.73 -G 5.47 -eG 0.94 0 -eN 0.94 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_1
ms ${nsam} ${nreps} -t 6.30 -G 6.02 -eG 0.85 0 -eN 0.85 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_2
ms ${nsam} ${nreps} -t 6.87 -G 6.57 -eG 0.78 0 -eN 0.78 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_3
ms ${nsam} ${nreps} -t 7.44 -G 7.11 -eG 0.72 0 -eN 0.72 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_4
ms ${nsam} ${nreps} -t 8.02 -G 7.66 -eG 0.67 0 -eN 0.67 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_5
ms ${nsam} ${nreps} -t 8.59 -G 8.21 -eG 0.62 0 -eN 0.62 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_6
ms ${nsam} ${nreps} -t 9.16 -G 8.75 -eG 0.58 0 -eN 0.58 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_7
ms ${nsam} ${nreps} -t 9.73 -G 9.3 -eG 0.55 0 -eN 0.55 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_8
ms ${nsam} ${nreps} -t 10.31 -G 9.85 -eG 0.52 0 -eN 0.52 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_9
ms ${nsam} ${nreps} -t 10.88 -G 10.4 -eG 0.49 0 -eN 0.49 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_10
ms ${nsam} ${nreps} -t 11.45 -G 10.94 -eG 0.47 0 -eN 0.47 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_11
ms ${nsam} ${nreps} -t 12.02 -G 11.49 -eG 0.45 0 -eN 0.45 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_12
ms ${nsam} ${nreps} -t 12.60 -G 12.04 -eG 0.43 0 -eN 0.43 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_13
ms ${nsam} ${nreps} -t 13.17 -G 12.58 -eG 0.41 0 -eN 0.41 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_14
ms ${nsam} ${nreps} -t 13.74 -G 13.13 -eG 0.39 0 -eN 0.39 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_15
ms ${nsam} ${nreps} -t 14.31 -G 13.68 -eG 0.37 0 -eN 0.37 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_16
ms ${nsam} ${nreps} -t 14.89 -G 14.23 -eG 0.36 0 -eN 0.36 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_17
ms ${nsam} ${nreps} -t 15.46 -G 14.77 -eG 0.35 0 -eN 0.35 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_18
ms ${nsam} ${nreps} -t 16.03 -G 15.32 -eG 0.33 0 -eN 0.33 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_19
ms ${nsam} ${nreps} -t 16.60 -G 15.87 -eG 0.32 0 -eN 0.32 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_20
ms ${nsam} ${nreps} -t 17.18 -G 16.41 -eG 0.31 0 -eN 0.31 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_21
ms ${nsam} ${nreps} -t 17.75 -G 16.96 -eG 0.30 0 -eN 0.30 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_22
ms ${nsam} ${nreps} -t 18.32 -G 17.51 -eG 0.29 0 -eN 0.29 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_23
ms ${nsam} ${nreps} -t 18.89 -G 18.06 -eG 0.28 0 -eN 0.28 0.006 | sample_stats >1popAnalysis/ExpGrow/outfile_24

#remove labels from sample_stats output to facilitate import and processing in r
END=24
for i in $(seq 1 $END)
do
	cat ./1popAnalysis/ExpGrow/outfile_$i | sed -E 's/[A-z]+\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)/\1	\2	\3	\4	\5/g' >./1popAnalysis/ExpGrow/outfile_finalout_$i
	rm ./1popAnalysis/ExpGrow/outfile_$i
done


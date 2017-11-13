#!/usr/local/bin/bash
nsam='163'
nreps='100000'
mkdir 1popAnalysis/BottleGrow

#ms commands based on the range of population sizes from 500,000 to 1,650,00 and best parameter estimates form ∂a∂i
ms ${nsam} ${nreps} -t 5.73 -G 3.49 -eG 0.714 0 -eN 0.714 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_1
ms ${nsam} ${nreps} -t 6.30 -G 3.84 -eG 0.649 0 -eN 0.649 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_2
ms ${nsam} ${nreps} -t 6.87 -G 4.18 -eG 0.595 0 -eN 0.595 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_3
ms ${nsam} ${nreps} -t 7.44 -G 4.53 -eG 0.549 0 -eN 0.549 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_4
ms ${nsam} ${nreps} -t 8.02 -G 4.88 -eG 0.510 0 -eN 0.510 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_5
ms ${nsam} ${nreps} -t 8.59 -G 5.23 -eG 0.476 0 -eN 0.476 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_6
ms ${nsam} ${nreps} -t 9.16 -G 5.58 -eG 0.446 0 -eN 0.446 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_7
ms ${nsam} ${nreps} -t 9.73 -G 5.93 -eG 0.420 0 -eN 0.420 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_8
ms ${nsam} ${nreps} -t 10.31 -G 6.28 -eG 0.397 0 -eN 0.397 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_9
ms ${nsam} ${nreps} -t 10.88 -G 6.62 -eG 0.376 0 -eN 0.376 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_10
ms ${nsam} ${nreps} -t 11.45 -G 6.97 -eG 0.357 0 -eN 0.357 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_11
ms ${nsam} ${nreps} -t 12.02 -G 7.32 -eG 0.340 0 -eN 0.340 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_12
ms ${nsam} ${nreps} -t 12.60 -G 7.67 -eG 0.324 0 -eN 0.324 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_13
ms ${nsam} ${nreps} -t 13.17 -G 8.02 -eG 0.310 0 -eN 0.310 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_14
ms ${nsam} ${nreps} -t 13.74 -G 8.37 -eG 0.297 0 -eN 0.297 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_15
ms ${nsam} ${nreps} -t 14.31 -G 8.72 -eG 0.286 0 -eN 0.286 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_16
ms ${nsam} ${nreps} -t 14.89 -G 9.06 -eG 0.275 0 -eN 0.275 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_17
ms ${nsam} ${nreps} -t 15.46 -G 9.41 -eG 0.264 0 -eN 0.264 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_18
ms ${nsam} ${nreps} -t 16.03 -G 9.76 -eG 0.255 0 -eN 0.255 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_19
ms ${nsam} ${nreps} -t 16.60 -G 10.11 -eG 0.246 0 -eN 0.246 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_20
ms ${nsam} ${nreps} -t 17.18 -G 10.46 -eG 0.238 0 -eN 0.238 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_21
ms ${nsam} ${nreps} -t 17.75 -G 10.81 -eG 0.230 0 -eN 0.230 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_22
ms ${nsam} ${nreps} -t 18.32 -G 11.16 -eG 0.223 0 -eN 0.223 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_23
ms ${nsam} ${nreps} -t 18.89 -G 11.51 -eG 0.216 0 -eN 0.216 0.007 | sample_stats >1popAnalysis/BottleGrow/outfile_24

#remove labels from sample_stats output to facilitate import and processing in r
END=24
for i in $(seq 1 $END)
do
	cat ./1popAnalysis/BottleGrow/outfile_$i | sed -E 's/[A-z]+\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)/\1	\2	\3	\4	\5/g' >./1popAnalysis/BottleGrow/outfile_finalout_$i
	rm ./1popAnalysis/BottleGrow/outfile_$i
done


#!/usr/local/bin/bash
nsam='163'
nreps='10000'
mkdir 1popAnalysis/AdmixConstantC

#ms commands based on the range of population sizes from 500,000 to 1,650,00 and best parameter estimates form ∂a∂i
ms ${nsam} ${nreps} -t 5.73	-es 0.156 1 0.6 -en 0.156 1 0.124 -en 0.156 2 0.044	-ej 0.699 2 1 -eN 0.699 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_1
ms ${nsam} ${nreps} -t 6.30	-es 0.141 1 0.6	-en 0.141 1 0.124 -en 0.141 2 0.044	-ej 0.636 2 1 -eN 0.636 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_2
ms ${nsam} ${nreps} -t 6.87	-es 0.130 1 0.6	-en 0.130 1 0.124 -en 0.130 2 0.044 -ej 0.583 2 1 -eN 0.583 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_3
ms ${nsam} ${nreps} -t 7.44	-es 0.120 1 0.6	-en 0.120 1 0.124 -en 0.120 2 0.044 -ej 0.538 2 1 -eN 0.538 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_4
ms ${nsam} ${nreps} -t 8.02	-es 0.111 1 0.6	-en 0.111 1 0.124 -en 0.111 2 0.044 -ej 0.499 2 1 -eN 0.499 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_5
ms ${nsam} ${nreps} -t 8.59	-es 0.104 1 0.6	-en 0.104 1 0.124 -en 0.104 2 0.044 -ej 0.466 2 1 -eN 0.466 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_6
ms ${nsam} ${nreps} -t 9.16	-es 0.097 1 0.6	-en 0.097 1 0.124 -en 0.097 2 0.044 -ej 0.437 2 1 -eN 0.437 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_7
ms ${nsam} ${nreps} -t 9.73	-es 0.092 1 0.6	-en 0.092 1 0.124 -en 0.092 2 0.044 -ej 0.411 2 1 -eN 0.411 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_8
ms ${nsam} ${nreps} -t 10.31 -es 0.086 1 0.6 -en 0.086 1 0.124 -en 0.086 2 0.044 -ej 0.388 2 1 -eN 0.388 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_9
ms ${nsam} ${nreps} -t 10.88 -es 0.082 1 0.6 -en 0.082 1 0.124 -en 0.082 2 0.044 -ej 0.368 2 1 -eN 0.368 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_10
ms ${nsam} ${nreps} -t 11.45 -es 0.078 1 0.6 -en 0.078 1 0.124 -en 0.078 2 0.044 -ej 0.350 2 1 -eN 0.350 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_11
ms ${nsam} ${nreps} -t 12.02 -es 0.074 1 0.6 -en 0.074 1 0.124 -en 0.074 2 0.044 -ej 0.333 2 1 -eN 0.333 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_12
ms ${nsam} ${nreps} -t 12.60 -es 0.071 1 0.6 -en 0.071 1 0.124 -en 0.071 2 0.044 -ej 0.318 2 1 -eN 0.318 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_13
ms ${nsam} ${nreps} -t 13.17 -es 0.068 1 0.6 -en 0.068 1 0.124 -en 0.068 2 0.044 -ej 0.304 2 1 -eN 0.304 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_14
ms ${nsam} ${nreps} -t 13.74 -es 0.065 1 0.6 -en 0.065 1 0.124 -en 0.065 2 0.044 -ej 0.291 2 1 -eN 0.291 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_15
ms ${nsam} ${nreps} -t 14.31 -es 0.062 1 0.6 -en 0.062 1 0.124 -en 0.062 2 0.044 -ej 0.280 2 1 -eN 0.280 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_16
ms ${nsam} ${nreps} -t 14.89 -es 0.060 1 0.6 -en 0.060 1 0.124 -en 0.060 2 0.044 -ej 0.269 2 1 -eN 0.269 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_17
ms ${nsam} ${nreps} -t 15.46 -es 0.058 1 0.6 -en 0.058 1 0.124 -en 0.058 2 0.044 -ej 0.259 2 1 -eN 0.259 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_18
ms ${nsam} ${nreps} -t 16.03 -es 0.056 1 0.6 -en 0.056 1 0.124 -en 0.056 2 0.044 -ej 0.250 2 1 -eN 0.250 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_19
ms ${nsam} ${nreps} -t 16.60 -es 0.054 1 0.6 -en 0.054 1 0.124 -en 0.054 2 0.044 -ej 0.241 2 1 -eN 0.241 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_20
ms ${nsam} ${nreps} -t 17.18 -es 0.052 1 0.6 -en 0.052 1 0.124 -en 0.052 2 0.044 -ej 0.233 2 1 -eN 0.233 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_21
ms ${nsam} ${nreps} -t 17.75 -es 0.050 1 0.6 -en 0.050 1 0.124 -en 0.050 2 0.044 -ej 0.226 2 1 -eN 0.226 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_22
ms ${nsam} ${nreps} -t 18.32 -es 0.049 1 0.6 -en 0.049 1 0.124 -en 0.049 2 0.044 -ej 0.219 2 1 -eN 0.219 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_23
ms ${nsam} ${nreps} -t 18.89 -es 0.047 1 0.6 -en 0.047 1 0.124 -en 0.047 2 0.044 -ej 0.212 2 1 -eN 0.212 0.006 | sample_stats >1popAnalysis/AdmixConstantC/outfile_24

#remove labels from sample_stats output to facilitate import and processing in r
END=24
for i in $(seq 1 $END)
do
	cat ./1popAnalysis/AdmixConstantC/outfile_$i | sed -E 's/[A-z]+\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)/\1	\2	\3	\4	\5/g' >./1popAnalysis/AdmixConstantC/outfile_finalout_$i
	rm ./1popAnalysis/AdmixConstantC/outfile_$i
done
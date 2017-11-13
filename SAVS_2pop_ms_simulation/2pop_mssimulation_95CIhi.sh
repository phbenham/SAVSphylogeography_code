#!/usr/local/bin/bash
nsam='204'
nreps='100000'
mkdir 2popAnalysis/NomConstantHi

#ms commands based on the range of population sizes from 500,000 to 2 million and upper 95% confidence interval estimates form ∂a∂i
ms ${nsam} ${nreps} -t 5.73 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.295 2 0.006 -en 1.083 2 30.4 -ej 4.133 2 1 -eN 4.133 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_1
ms ${nsam} ${nreps} -t 6.30 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.268 2 0.006 -en 0.985 2 30.4 -ej 3.757 2 1 -eN 3.757 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_2
ms ${nsam} ${nreps} -t 6.87 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.246 2 0.006 -en 0.903 2 30.4 -ej 3.444 2 1 -eN 3.444 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_3
ms ${nsam} ${nreps} -t 7.44 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.227 2 0.006 -en 0.833 2 30.4 -ej 3.179 2 1 -eN 3.179 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_4
ms ${nsam} ${nreps} -t 8.02 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.211 2 0.006 -en 0.774 2 30.4 -ej 2.952 2 1 -eN 2.952 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_5
ms ${nsam} ${nreps} -t 8.59 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.197 2 0.006 -en 0.722 2 30.4 -ej 2.755 2 1 -eN 2.755 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_6
ms ${nsam} ${nreps} -t 9.16 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.185 2 0.006 -en 0.677 2 30.4 -ej 2.583 2 1 -eN 2.583 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_7
ms ${nsam} ${nreps} -t 9.73 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.174 2 0.006 -en 0.637 2 30.4 -ej 2.431 2 1 -eN 2.431 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_8
ms ${nsam} ${nreps} -t 10.31 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.164 2 0.006 -en 0.602 2 30.4 -ej 2.296 2 1 -eN 2.296 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_9
ms ${nsam} ${nreps} -t 10.88 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.155 2 0.006 -en 0.570 2 30.4 -ej 2.175 2 1 -eN 2.175 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_10
ms ${nsam} ${nreps} -t 11.45 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.148 2 0.006 -en 0.542 2 30.4 -ej 2.066 2 1 -eN 2.066 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_11
ms ${nsam} ${nreps} -t 12.02 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.141 2 0.006 -en 0.516 2 30.4 -ej 1.968 2 1 -eN 1.968 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_12
ms ${nsam} ${nreps} -t 12.60 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.134 2 0.006 -en 0.492 2 30.4 -ej 1.879 2 1 -eN 1.879 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_13
ms ${nsam} ${nreps} -t 13.17 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.128 2 0.006 -en 0.471 2 30.4 -ej 1.797 2 1 -eN 1.797 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_14
ms ${nsam} ${nreps} -t 13.74 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.123 2 0.006 -en 0.451 2 30.4 -ej 1.722 2 1 -eN 1.722 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_15
ms ${nsam} ${nreps} -t 14.31 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.118 2 0.006 -en 0.433 2 30.4 -ej 1.653 2 1 -eN 1.653 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_16
ms ${nsam} ${nreps} -t 14.89 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.114 2 0.006 -en 0.417 2 30.4 -ej 1.590 2 1 -eN 1.590 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_17
ms ${nsam} ${nreps} -t 15.46 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.109 2 0.006 -en 0.401 2 30.4 -ej 1.531 2 1 -eN 1.531 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_18
ms ${nsam} ${nreps} -t 16.03 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.105 2 0.006 -en 0.387 2 30.4 -ej 1.476 2 1 -eN 1.476 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_19
ms ${nsam} ${nreps} -t 16.60 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.102 2 0.006 -en 0.374 2 30.4 -ej 1.425 2 1 -eN 1.425 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_20
ms ${nsam} ${nreps} -t 17.18 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.098 2 0.006 -en 0.361 2 30.4 -ej 1.378 2 1 -eN 1.378 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_21
ms ${nsam} ${nreps} -t 17.75 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.095 2 0.006 -en 0.350 2 30.4 -ej 1.333 2 1 -eN 1.333 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_22
ms ${nsam} ${nreps} -t 18.32 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.092 2 0.006 -en 0.339 2 30.4 -ej 1.291 2 1 -eN 1.291 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_23
ms ${nsam} ${nreps} -t 18.89 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.089 2 0.006 -en 0.328 2 30.4 -ej 1.252 2 1 -eN 1.252 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_24
ms ${nsam} ${nreps} -t 19.47 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.087 2 0.006 -en 0.319 2 30.4 -ej 1.216 2 1 -eN 1.216 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_25
ms ${nsam} ${nreps} -t 20.04 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.084 2 0.006 -en 0.310 2 30.4 -ej 1.181 2 1 -eN 1.181 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_26
ms ${nsam} ${nreps} -t 20.61 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.082 2 0.006 -en 0.301 2 30.4 -ej 1.148 2 1 -eN 1.148 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_27
ms ${nsam} ${nreps} -t 21.18 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.080 2 0.006 -en 0.293 2 30.4 -ej 1.117 2 1 -eN 1.117 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_28
ms ${nsam} ${nreps} -t 21.76 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.078 2 0.006 -en 0.285 2 30.4 -ej 1.088 2 1 -eN 1.088 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_29
ms ${nsam} ${nreps} -t 22.33 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.076 2 0.006 -en 0.278 2 30.4 -ej 1.060 2 1 -eN 1.060 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_30
ms ${nsam} ${nreps} -t 22.90 -I 2 163 41 -n 2 0.08 -m 1 2 9.2 -m 2 1 2.2 -en 0.074 2 0.006 -en 0.271 2 30.4 -ej 1.033 2 1 -eN 1.033 0.09 | sample_stats >2popAnalysis/NomConstantHi/outfile_31

#remove labels from sample_stats output to facilitate import and processing in r
END=31
for i in $(seq 1 $END)
do
 cat ./2popAnalysis/NomConstantHi/outfile_$i | sed -E 's/[A-z]+\: (.+) [A-z]+\: (.+) [A-z]\: (.+) [A-z]+\: (.+) [A-z]\: (.+)/\1 \2 \3 \4 \5/g' >./2popAnalysis/NomConstantHi/outfile_finalout_$i
 rm ./2popAnalysis/NomConstantHi/outfile_$i
done
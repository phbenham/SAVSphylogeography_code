#!/usr/local/bin/bash
nsam='204'
nreps='100000'
mkdir 2popAnalysis/NomConstantLo

#ms commands based on the range of population sizes from 500,000 to 2 million and lower 95% confidence interval estimates form ∂a∂i
ms ${nsam} ${nreps} -t 5.73 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.119 2 0.00001 -en 0.482 2 0.00001 -ej 0.482 2 1 -eN 0.482 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_1
ms ${nsam} ${nreps} -t 6.30 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.108 2 0.00001 -en 0.438 2 0.00001 -ej 0.438 2 1 -eN 0.438 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_2
ms ${nsam} ${nreps} -t 6.87 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.099 2 0.00001 -en 0.401 2 0.00001 -ej 0.401 2 1 -eN 0.401 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_3
ms ${nsam} ${nreps} -t 7.44 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.091 2 0.00001 -en 0.371 2 0.00001 -ej 0.371 2 1 -eN 0.371 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_4
ms ${nsam} ${nreps} -t 8.02 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.085 2 0.00001 -en 0.344 2 0.00001 -ej 0.344 2 1 -eN 0.344 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_5
ms ${nsam} ${nreps} -t 8.59 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.079 2 0.00001 -en 0.321 2 0.00001 -ej 0.321 2 1 -eN 0.321 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_6
ms ${nsam} ${nreps} -t 9.16 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.074 2 0.00001 -en 0.301 2 0.00001 -ej 0.301 2 1 -eN 0.301 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_7
ms ${nsam} ${nreps} -t 9.73 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.070 2 0.00001 -en 0.283 2 0.00001 -ej 0.283 2 1 -eN 0.283 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_8
ms ${nsam} ${nreps} -t 10.31 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.066 2 0.00001 -en 0.268 2 0.00001 -ej 0.268 2 1 -eN 0.268 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_9
ms ${nsam} ${nreps} -t 10.88 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.063 2 0.00001 -en 0.254 2 0.00001 -ej 0.254 2 1 -eN 0.254 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_10
ms ${nsam} ${nreps} -t 11.45 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.059 2 0.00001 -en 0.241 2 0.00001 -ej 0.241 2 1 -eN 0.241 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_11
ms ${nsam} ${nreps} -t 12.02 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.057 2 0.00001 -en 0.229 2 0.00001 -ej 0.229 2 1 -eN 0.229 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_12
ms ${nsam} ${nreps} -t 12.60 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.054 2 0.00001 -en 0.219 2 0.00001 -ej 0.219 2 1 -eN 0.219 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_13
ms ${nsam} ${nreps} -t 13.17 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.052 2 0.00001 -en 0.209 2 0.00001 -ej 0.209 2 1 -eN 0.209 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_14
ms ${nsam} ${nreps} -t 13.74 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.050 2 0.00001 -en 0.201 2 0.00001 -ej 0.201 2 1 -eN 0.201 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_15
ms ${nsam} ${nreps} -t 14.31 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.048 2 0.00001 -en 0.193 2 0.00001 -ej 0.193 2 1 -eN 0.193 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_16
ms ${nsam} ${nreps} -t 14.89 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.046 2 0.00001 -en 0.185 2 0.00001 -ej 0.185 2 1 -eN 0.185 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_17
ms ${nsam} ${nreps} -t 15.46 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.044 2 0.00001 -en 0.178 2 0.00001 -ej 0.178 2 1 -eN 0.178 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_18
ms ${nsam} ${nreps} -t 16.03 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.042 2 0.00001 -en 0.172 2 0.00001 -ej 0.172 2 1 -eN 0.172 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_19
ms ${nsam} ${nreps} -t 16.60 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.041 2 0.00001 -en 0.166 2 0.00001 -ej 0.166 2 1 -eN 0.166 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_20
ms ${nsam} ${nreps} -t 17.18 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.040 2 0.00001 -en 0.161 2 0.00001 -ej 0.161 2 1 -eN 0.161 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_21
ms ${nsam} ${nreps} -t 17.75 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.038 2 0.00001 -en 0.155 2 0.00001 -ej 0.155 2 1 -eN 0.155 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_22
ms ${nsam} ${nreps} -t 18.32 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.037 2 0.00001 -en 0.151 2 0.00001 -ej 0.151 2 1 -eN 0.151 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_23
ms ${nsam} ${nreps} -t 18.89 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.036 2 0.00001 -en 0.146 2 0.00001 -ej 0.146 2 1 -eN 0.146 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_24
ms ${nsam} ${nreps} -t 19.47 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.035 2 0.00001 -en 0.142 2 0.00001 -ej 0.142 2 1 -eN 0.142 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_25
ms ${nsam} ${nreps} -t 20.04 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.034 2 0.00001 -en 0.138 2 0.00001 -ej 0.138 2 1 -eN 0.138 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_26
ms ${nsam} ${nreps} -t 20.61 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.033 2 0.00001 -en 0.134 2 0.00001 -ej 0.134 2 1 -eN 0.134 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_27
ms ${nsam} ${nreps} -t 21.18 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.032 2 0.00001 -en 0.130 2 0.00001 -ej 0.130 2 1 -eN 0.130 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_28
ms ${nsam} ${nreps} -t 21.76 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.031 2 0.00001 -en 0.127 2 0.00001 -ej 0.127 2 1 -eN 0.127 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_29
ms ${nsam} ${nreps} -t 22.33 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.030 2 0.00001 -en 0.124 2 0.00001 -ej 0.124 2 1 -eN 0.124 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_30
ms ${nsam} ${nreps} -t 22.90 -I 2 163 41 -n 2 0.07 -m 1 2 4 -m 2 1 0.6 -en 0.030 2 0.00001 -en 0.120 2 0.00001 -ej 0.120 2 1 -eN 0.120 0.231 | sample_stats >2popAnalysis/NomConstantLo/outfile_31

#remove labels from sample_stats output to facilitate import and processing in r
END=31
for i in $(seq 1 $END)
do
 cat ./2popAnalysis/NomConstantLo/outfile_$i | sed -E 's/[A-z]+\: (.+) [A-z]+\: (.+) [A-z]\: (.+) [A-z]+\: (.+) [A-z]\: (.+)/\1 \2 \3 \4 \5/g' >./2popAnalysis/NomConstantLo/outfile_finalout_$i
 rm ./2popAnalysis/NomConstantLo/outfile_$i
done
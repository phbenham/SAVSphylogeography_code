#!/usr/local/bin/bash
nsam='204'
nreps='100000'
mkdir 2popAnalysis/NomConstant

#ms commands based on the range of population sizes from 500,000 to 2 million and best parameter estimates form ∂a∂i
ms ${nsam} ${nreps} -t 5.73 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.200 2 0.004 -en 0.767 2 7.62 -ej 0.963 2 1 -eN 0.963 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_1
ms ${nsam} ${nreps} -t 6.30 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.182 2 0.004 -en 0.697 2 7.62 -ej 0.875 2 1 -eN 0.875 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_2
ms ${nsam} ${nreps} -t 6.87 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.166 2 0.004 -en 0.639 2 7.62 -ej 0.802 2 1 -eN 0.802 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_3
ms ${nsam} ${nreps} -t 7.44 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.154 2 0.004 -en 0.590 2 7.62 -ej 0.741 2 1 -eN 0.741 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_4
ms ${nsam} ${nreps} -t 8.02 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.143 2 0.004 -en 0.548 2 7.62 -ej 0.688 2 1 -eN 0.688 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_5
ms ${nsam} ${nreps} -t 8.59 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.133 2 0.004 -en 0.511 2 7.62 -ej 0.642 2 1 -eN 0.642 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_6
ms ${nsam} ${nreps} -t 9.16 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.125 2 0.004 -en 0.479 2 7.62 -ej 0.602 2 1 -eN 0.602 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_7
ms ${nsam} ${nreps} -t 9.73 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.118 2 0.004 -en 0.451 2 7.62 -ej 0.566 2 1 -eN 0.566 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_8
ms ${nsam} ${nreps} -t 10.31 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.111 2 0.004 -en 0.426 2 7.62 -ej 0.535 2 1 -eN 0.535 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_9
ms ${nsam} ${nreps} -t 10.88 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.105 2 0.004 -en 0.404 2 7.62 -ej 0.507 2 1 -eN 0.507 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_10
ms ${nsam} ${nreps} -t 11.45 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.100 2 0.004 -en 0.383 2 7.62 -ej 0.481 2 1 -eN 0.481 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_11
ms ${nsam} ${nreps} -t 12.02 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.095 2 0.004 -en 0.365 2 7.62 -ej 0.458 2 1 -eN 0.458 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_12
ms ${nsam} ${nreps} -t 12.60 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.091 2 0.004 -en 0.349 2 7.62 -ej 0.438 2 1 -eN 0.438 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_13
ms ${nsam} ${nreps} -t 13.17 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.087 2 0.004 -en 0.333 2 7.62 -ej 0.419 2 1 -eN 0.419 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_14
ms ${nsam} ${nreps} -t 13.74 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.083 2 0.004 -en 0.320 2 7.62 -ej 0.401 2 1 -eN 0.401 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_15
ms ${nsam} ${nreps} -t 14.31 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.080 2 0.004 -en 0.307 2 7.62 -ej 0.385 2 1 -eN 0.385 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_16
ms ${nsam} ${nreps} -t 14.89 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.077 2 0.004 -en 0.295 2 7.62 -ej 0.370 2 1 -eN 0.370 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_17
ms ${nsam} ${nreps} -t 15.46 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.074 2 0.004 -en 0.284 2 7.62 -ej 0.357 2 1 -eN 0.357 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_18
ms ${nsam} ${nreps} -t 16.03 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.071 2 0.004 -en 0.274 2 7.62 -ej 0.344 2 1 -eN 0.344 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_19
ms ${nsam} ${nreps} -t 16.60 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.069 2 0.004 -en 0.264 2 7.62 -ej 0.332 2 1 -eN 0.332 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_20
ms ${nsam} ${nreps} -t 17.18 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.067 2 0.004 -en 0.256 2 7.62 -ej 0.321 2 1 -eN 0.321 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_21
ms ${nsam} ${nreps} -t 17.75 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.064 2 0.004 -en 0.247 2 7.62 -ej 0.311 2 1 -eN 0.311 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_22
ms ${nsam} ${nreps} -t 18.32 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.062 2 0.004 -en 0.240 2 7.62 -ej 0.301 2 1 -eN 0.301 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_23
ms ${nsam} ${nreps} -t 18.89 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.061 2 0.004 -en 0.232 2 7.62 -ej 0.292 2 1 -eN 0.292 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_24
ms ${nsam} ${nreps} -t 19.47 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.059 2 0.004 -en 0.226 2 7.62 -ej 0.283 2 1 -eN 0.283 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_25
ms ${nsam} ${nreps} -t 20.04 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.057 2 0.004 -en 0.219 2 7.62 -ej 0.275 2 1 -eN 0.275 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_26
ms ${nsam} ${nreps} -t 20.61 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.055 2 0.004 -en 0.213 2 7.62 -ej 0.267 2 1 -eN 0.267 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_27
ms ${nsam} ${nreps} -t 21.18 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.054 2 0.004 -en 0.207 2 7.62 -ej 0.260 2 1 -eN 0.260 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_28
ms ${nsam} ${nreps} -t 21.76 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.053 2 0.004 -en 0.202 2 7.62 -ej 0.253 2 1 -eN 0.253 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_29
ms ${nsam} ${nreps} -t 22.33 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.051 2 0.004 -en 0.197 2 7.62 -ej 0.247 2 1 -eN 0.247 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_30
ms ${nsam} ${nreps} -t 22.90 -I 2 163 41 -n 2 0.08 -m 1 2 1.65 -m 2 1 0.35 -en 0.050 2 0.004 -en 0.192 2 7.62 -ej 0.241 2 1 -eN 0.241 0.134 | sample_stats >2popAnalysis/NomConstant/outfile_31


#remove labels from sample_stats output to facilitate import and processing in r
END=31
for i in $(seq 1 $END)
do
	cat ./2popAnalysis/NomConstant/outfile_$i | sed -E 's/[A-z]+\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)	[A-z]+\:	(.+)	[A-z]\:	(.+)/\1	\2	\3	\4	\5/g' >./2popAnalysis/NomConstant/outfile_finalout_$i
	rm ./2popAnalysis/NomConstant/outfile_$i
done
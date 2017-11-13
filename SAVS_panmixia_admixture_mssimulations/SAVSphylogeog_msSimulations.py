#!/usr/bin/env python 

import numpy
import os
import sys

#definitions set to generate mscommand for different models
##########################################################################################
def Constant_mscore((nsam, nreps, theta, T1, NEanc)):
    """
    ms core command corresponding to prior_onegrow_mig
    """
    ms_command = "ms %d %d -t %f -eN %f %f" % (nsam, nreps, theta, T1, NEanc)

    return ms_command
##########################################################################################
def Bottleneck_mscore((nsam, nreps, theta, Tendbot, NEbot, Tbot, NEprebot)):
    """
    ms core command corresponding to prior_onegrow_mig
    """
    
    ms_command = "ms %d %d -t %f -eN %f %f -eN %f %f " % (nsam, nreps, theta, Tendbot, NEbot, Tbot, NEprebot)

    return ms_command
##########################################################################################   
def AdmixCon_mscore((nsam, nreps, theta, Tmerge1, f, Tmerge2, NEsplit, Tsplit1, Tsplit2, NEanc)):
    """
    ms core command corresponding to prior_onegrow_mig
    """
     
    ms_command = "ms %d %d -t %f -es %f 1 %f -eN %f %f -ej %f 2 1 -eN %f %f " % (nsam, nreps, theta, Tmerge1, f, Tmerge2, NEsplit, Tsplit1, Tsplit2, NEanc)

    return ms_command
##########################################################################################     
def AdmixBot_mscore((nsam, nreps, theta, Tmerge1, f, Tmerge2, NE1, Tendbot, NE2, Tbot, NE3, Tsplit1, Tsplit2, NEanc)):
    """
    ms core command corresponding to prior_onegrow_mig
    """
    ms_command = "ms %d %d -t %f -es %f 1 %f -eN %f %f -eN %f %f -eN %f %f -ej %f 2 1 -eN %f %f " % (nsam, nreps, theta, Tmerge1, f, Tmerge2, NE1, Tendbot, NE2, Tbot, NE3, Tsplit1, Tsplit2, NEanc)

    return ms_command
########################################################################################## 

#parameter settings
nsam = 163
nreps = 25000
bp = 1041
MutRate = 1.1e-8 
fadmix = 0.5
Ne = range(100000,2050000,50000)

sed_com = "'s/[A-z]+\://g'"

########################################################################################## 
#####################--Model1 Constant Population Size--##################################    

path = "./Constant_out/"
os.mkdir(path)
dir = ["10k","50k","100k","200k"]
for g in range(4):
	os.mkdir(path+dir[g])


N1 = [0.1,0.25,0.5,0.75,1]
N2 = [0.1,0.25,0.5,0.75]
theta = [] 
T1 = [10000,50000,100000,200000]

popt = []
for j in T1:
	for l in N1:
		for i in Ne:		
			ThetaCalc = i*bp*MutRate
			theta.append(float(ThetaCalc))
			param = [nsam, nreps, float(ThetaCalc), (float(j)/float(i)), l]
			popt.append(param)

#perform simulations in ms.
for b in range(len(popt)):
	print b
	mscommands = Constant_mscore(popt[b])
	#print mscommands
	if b < 195:
		os.system("{0} |sample_stats | sed -E {1} >./Constant_out/10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 195 and b < 390:
		os.system("{0} |sample_stats | sed -E {1} >./Constant_out/50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 390 and b < 585:
		os.system("{0} |sample_stats | sed -E {1} >./Constant_out/100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 585 and b < 780:
		os.system("{0} |sample_stats | sed -E {1} >./Constant_out/200k/msout_{2}.txt".format(mscommands,sed_com,b))


########################################################################################## 
########################################################################################## 
#####################--Model2 Bottleneck--################################################
path = "./Bottleneck_out/"
os.mkdir(path)
dir_bot = ["1k-10k", "1k-50k", "1k-100k","1k-200k","10k-10k","10k-50k","10k-100k","10k-200k","50k-10k","50k-50k","50k-100k","50k-200k","100k-10k","100k-50k","100k-100k","100k-200k"]  

for g in range(16):
	os.mkdir(path+dir_bot[g])
  

N1_bot = [0.1,0.25,0.5,0.75]
N2_bot = [0.1,0.25,0.5,0.75]
theta_bot = [] 
T1_bot = [1000,10000,50000,100000]
T2_bot = [10000,50000,100000,200000]


popt_bot = []
for j in T1_bot:
	for k in T2_bot:
		for l in N1_bot:
			for m in N2_bot:	
				for i in Ne:		
					ThetaCalc = i*bp*MutRate
					theta_bot.append(float(ThetaCalc))
					param_bot = [nsam, nreps, float(ThetaCalc),(float(j)/float(i)), l, ((float(j)+float(k))/float(i)),m]
					popt_bot.append(param_bot)


#perform simulations in ms.
for b in range(len(popt_bot)):
	print b
	mscommands = Bottleneck_mscore(popt_bot[b])
	#print mscommands
	if b < 624:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/1k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 624 and b < 1248:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/1k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 1248 and b < 1872:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/1k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 1872 and b < 2496:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/1k-200k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 2496 and b < 3120:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/10k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 3120 and b < 3744:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/10k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 3744 and b < 4368:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/10k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 4368 and b < 4992:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/10k-200k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 4992 and b < 5616:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/50k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 5616 and b < 6240:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/50k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 6240 and b < 6864:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/50k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 6864 and b < 7488:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/50k-200k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 7488 and b < 8112:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/100k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 8112 and b < 8736:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/100k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 8736 and b < 9360:
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/100k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 9360:	
		os.system("{0} |sample_stats | sed -E {1} >./Bottleneck_out/100k-200k/msout_{2}.txt".format(mscommands,sed_com,b))
			

########################################################################################## 
########################################################################################## 
#####################--Model3 Admixture with constant pop. size--#########################
#create folders for different split, merger, and bottleneck histories

path = "./AdmixCon_out/"
os.mkdir(path)
dir_ad = ["1k-10k", "1k-50k", "1k-100k","1k-200k","10k-10k","10k-50k","10k-100k","10k-200k","50k-10k","50k-50k","50k-100k","50k-200k","100k-10k","100k-50k","100k-100k","100k-200k"]  

for g in range(16):
	os.mkdir(path+dir_ad[g])
  

N1_ad = [0.1,0.25,0.5,0.75]
N2_ad = [0.1,0.25,0.5,0.75]
theta_ad = [] 
T1_ad = [1000,10000,50000,100000]
T2_ad = [10000,50000,100000,200000]


popt_ad = []
for j in T1_ad:
	for k in T2_ad:
		for l in N1_ad:
			for m in N2_ad:	
				for i in Ne:		
					ThetaCalc = i*bp*MutRate
					theta_ad.append(float(ThetaCalc))
					param_ad = [nsam, nreps, float(ThetaCalc),(float(j)/float(i)),fadmix,(float(j)/float(i)), l, ((float(j)+float(k))/float(i)),((float(j)+float(k))/float(i)) ,m]
					popt_ad.append(param_ad)


#perform simulations in ms.
for b in range(len(popt_ad)):
	print b
	mscommands = AdmixCon_mscore(popt_ad[b])
	#print mscommands
	if b < 624:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/1k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 624 and b < 1248:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/1k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 1248 and b < 1872:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/1k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 1872 and b < 2496:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/1k-200k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 2496 and b < 3120:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/10k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 3120 and b < 3744:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/10k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 3744 and b < 4368:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/10k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 4368 and b < 4992:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/10k-200k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 4992 and b < 5616:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/50k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 5616 and b < 6240:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/50k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 6240 and b < 6864:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/50k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 6864 and b < 7488:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/50k-200k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 7488 and b < 8112:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/100k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 8112 and b < 8736:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/100k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 8736 and b < 9360:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/100k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 9360:	
		os.system("{0} |sample_stats | sed -E {1} >./AdmixCon_out/100k-200k/msout_{2}.txt".format(mscommands,sed_com,b))	
	
########################################################################################## 
########################################################################################## 
#####################--Model4 Admixture with bottleneck--#################################

#create folders for different split, merger, and bottleneck histories
path = "./AdmixBot_out/"
os.mkdir(path)
dir_adbot = ["1k-10k", "1k-50k", "1k-100k","1k-200k","10k-10k","10k-50k","10k-100k","10k-200k","50k-10k","50k-50k","50k-100k","50k-200k","100k-10k","100k-50k","100k-100k","100k-200k"]  

for g in range(16):
	os.mkdir(path+dir_adbot[g])


SplitNe = 0.75

N1_adbot = [0.1,0.25,0.5]
N2_adbot = [0.1,0.25,0.5,0.75]
theta_adbot = [] 
T1_adbot = [1000,10000,50000,100000]
T2_adbot = [10000,50000,100000,200000]
Tendbot = 10000
Tbot = 50000

popt_adbot = []
for j in T1_adbot:
	for k in T2_adbot:
		for l in N1_adbot:
			for m in N2_adbot:	
				for i in Ne:		
					ThetaCalc = i*bp*MutRate
					theta_adbot.append(float(ThetaCalc))
					param_adbot = [nsam, nreps, float(ThetaCalc),(float(j)/float(i)),fadmix,(float(j)/float(i)),SplitNe,((float(Tendbot)+float(j))/float(i)),l,((float(Tbot)+float(Tendbot)+float(j))/float(i)),SplitNe,((float(Tbot)+float(Tendbot)+float(k)+float(j))/float(i)),((float(Tbot)+float(Tendbot)+float(k)+float(j))/float(i)),m]
					popt_adbot.append(param_adbot)



#perform simulations in ms.
for b in range(len(popt_adbot)):
	print b
	mscommands = AdmixBot_mscore(popt_adbot[b])
	if b < 468:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/1k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 468 and b < 936:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/1k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 936 and b < 1404:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/1k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 1404 and b < 1872:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/1k-200k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 1872 and b < 2340:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/10k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 2340 and b < 2808:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/10k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 2808 and b < 3276:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/10k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 3276 and b < 3744:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/10k-200k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 3744 and b < 4212:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/50k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 4212 and b < 4680:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/50k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 4680 and b < 5148:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/50k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 5148 and b < 5616:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/50k-200k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 5616 and b < 6084:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/100k-10k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 6084 and b < 6552:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/100k-50k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 6552 and b < 7020:
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/100k-100k/msout_{2}.txt".format(mscommands,sed_com,b))
	elif b >= 7020:	
		os.system("{0} |sample_stats | sed -E {1} >./AdmixBot_out/100k-200k/msout_{2}.txt".format(mscommands,sed_com,b))	
		
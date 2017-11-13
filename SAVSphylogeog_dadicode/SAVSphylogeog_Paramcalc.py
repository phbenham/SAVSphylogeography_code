#!/usr/bin/env python 
import dadi
import numpy as np
from numpy import array
import pandas as pd
import sys, os
import pylab 
import SAVS2pop_DemographicModels

Usage="""Script to generate parameter values relative to Nref
from optimized parameter estimates for each model.
"""

#parse snps file
dd = dadi.Misc.make_data_dict("dadi_input_finaldataset_3Jan2017.tsv")
SAVSfoldedSpec = dadi.Spectrum.from_data_dict(dd, ['CON','MEX'], [25,16],
                                      polarized=False)
                                      
# model and data settings                                      
data = SAVSfoldedSpec
ns = data.sample_sizes
pts_l = [30,40,60]

#import file with optimized parameters from each model. Extract parameter values [popt]
#and likelihood [LL].
InFileName = "SAVSphylogeog_FinalModelRun.txt"
InFile = open(InFileName, 'r')
popt = []
LL = []
for line in InFile:
	line = line.strip('\n')
	line = line.split(',')
	popt.append(line[:-1])
	LL.append(line[-1])
InFile.close()

popt_float = []
for i in popt:
	item = []
	for j in i:
		item.append(float(j))
	popt_float.append(item)	

#Specify each model to be tested from SAVS2pop_DemographicModels file
Isoconstant = SAVS2pop_DemographicModels.split_Nomig
IsobottleneckMex = SAVS2pop_DemographicModels.split_bottleneckMex
IsobottleneckNom = SAVS2pop_DemographicModels.split_bottleneckNom
Isobottleneckboth = SAVS2pop_DemographicModels.split_bottleneckboth
IsogrowMex = SAVS2pop_DemographicModels.split_growMex
IsogrowNom = SAVS2pop_DemographicModels.split_growNom
Isogrowboth = SAVS2pop_DemographicModels.split_bothgrow
IMconstant = SAVS2pop_DemographicModels.split_mig
IMbottleneckMex = SAVS2pop_DemographicModels.split_bottleneckMex_mig
IMbottleneckNom = SAVS2pop_DemographicModels.split_bottleneckNom_mig
IMbottleneckboth = SAVS2pop_DemographicModels.split_bottleneckboth_mig
IMgrowMex = SAVS2pop_DemographicModels.split_growMex_mig
IMgrowNom = SAVS2pop_DemographicModels.split_growNom_mig
IMgrowboth = SAVS2pop_DemographicModels.split_bothgrow_mig
AdmixIMConstant = SAVS2pop_DemographicModels.threepop_admix
AdmixBottleneckMex = SAVS2pop_DemographicModels.threepop_admix_bottleneckMex
AdmixBottleneckboth = SAVS2pop_DemographicModels.threepop_admix_bottleneckboth
AdmixGrowNom = SAVS2pop_DemographicModels.threepop_admix_growNom

#include models in list, so script runs through each model 
models =[Isoconstant,  IsobottleneckMex, IsobottleneckNom, Isobottleneckboth,IsogrowMex, IsogrowNom, Isogrowboth,  IMconstant,IMbottleneckMex, IMbottleneckNom, IMbottleneckboth, IMgrowMex, IMgrowNom, IMgrowboth,AdmixIMConstant, AdmixBottleneckMex, AdmixBottleneckboth, AdmixGrowNom]
model_names =["Isoconstant_out.txt", "IsobottleneckMex_out.txt", "IsobottleneckNom_out.txt", "Isobottleneckboth_out.txt", "IsogrowMex_out.txt", "IsogrowNom_out.txt", "Isogrowboth_out.txt", "IMconstant_out.txt", "IMbottleneckMex_out.txt", "IMbottleneckNom_out.txt", "IMbottleneckboth_out.txt", "IMgrowMex_out.txt", "IMgrowNom_out.txt", "IMgrowboth_out.txt", "AdmixIMConstant", "AdmixBottleneckMex", "AdmixBottleneckboth", "AdmixGrowNom"]

theta = []
for t in range(18):
	func = models[t]
	func_ex = dadi.Numerics.make_extrap_log_func(func)
	model = func_ex(popt_float[t], ns, pts_l)
	theta_mod = dadi.Inference.optimal_sfs_scaling(model, data)
	print('Optimal value of theta: {0}'.format(theta_mod))
	theta.append(theta_mod)

#2pop params
ML1 = pd.Series(popt_float[0],  index = ['nu1', 'nu2', 'Tsp'])
ML2 = pd.Series(popt_float[1],  index = ['nu1', 'nu2', 'nuBot2', 'nuRec2', 'Tsp', 'Tbot2', 'Trec2'])
ML3 = pd.Series(popt_float[2],  index = ['nu1', 'nu2', 'nuBot1', 'nuRec1', 'Tsp', 'Tbot1', 'Trec1'])
ML4 = pd.Series(popt_float[3],  index = ['nu1', 'nu2', 'nuBot1', 'nuRec1', 'nuBot2', 'nuRec2', 'Tsp', 'Tbot1', 'Trec1', 'Tbot2', 'Trec2'])
ML5 = pd.Series(popt_float[4],  index = ['nu1', 'nu2O', 'nu2f', 'Tsp'])
ML6 = pd.Series(popt_float[5],  index = ['nu1O','nu1f', 'nu2', 'Tsp'])
ML7 = pd.Series(popt_float[6], index = ['nu1O', 'nu1f', 'nu2O', 'nu2f', 'Tsp'])
ML8 = pd.Series(popt_float[7], index = ['nu1', 'nu2', 'Tsp', 'm1','m2'])
ML9 = pd.Series(popt_float[8], index = ['nu1', 'nu2', 'nuBot2', 'nuRec2', 'Tsp', 'Tbot2', 'Trec2', 'm1','m2'])
ML10 = pd.Series(popt_float[9], index = ['nu1', 'nu2', 'nuBot1', 'nuRec1', 'Tsp', 'Tbot1', 'Trec1', 'm1', 'm2'])
ML11 = pd.Series(popt_float[10], index = ['nu1', 'nu2', 'nuBot1', 'nuRec1', 'nuBot2', 'nuRec2', 'Tsp', 'Tbot1', 'Trec1', 'Tbot2', 'Trec2', 'm1', 'm2'])
ML12 = pd.Series(popt_float[11],  index = ['nu1', 'nu2O', 'nu2f', 'Tsp', 'm1', 'm2'])
ML13 = pd.Series(popt_float[12], index = ['nu1O', 'nu1f', 'nu2', 'Tsp', 'm1', 'm2']) 
ML14 = pd.Series(popt_float[13], index = ['nu1O', 'nu1f', 'nu2O', 'nu2f', 'Tsp', 'm1', 'm2'])
ML15 = pd.Series(popt_float[14], index = ['nu1','nu2','nu3','Tsp1','Tsp2','f', 'm1','m2'])
ML16 = pd.Series(popt_float[15], index = ['nu1','nu2','nu3','nu3bot','nu3rec','Tsp1','Tsp2','Tbot2', 'Trec2','f', 'm1','m2'])
ML17 = pd.Series(popt_float[16], index = ['nu1','nu2','nu3','nu1bot','nu1rec','nu3bot','nu3rec','Tsp1','Tsp2','Tbot1','Trec1','Tbot2','Trec2','f', 'm1','m2'])
ML18 = pd.Series(popt_float[17], index = ['nu1','nu1O', 'nu1f', 'nu2','nu3', 'nu3bot', 'nu3rec', 'Tsp1','Tsp2', 'Tbot2', 'Trec2', 'f','m1','m2'])

#create table with parameter values for each model
raw_data = pd.DataFrame([ML1, ML2, ML3, ML4, ML5, ML6, ML7, ML8, ML9, ML10, ML11, ML12, ML13, ML14, ML15, ML16, ML17, ML18], index = ["ML1","ML2","ML3","ML4","ML5","ML6", "ML7", "ML8", "ML9", "ML10", "ML11", "ML12", "ML13","ML14", "ML15", "ML16", "ML17", "ML18"]).T
print raw_data

#print ML1.Index()
###### Fixed params####
mu = 3.3e-9         ## from Zhang et al. 2009 average passeriform mutation rate
gentime = 1.0  
L = 766646
Nloci = 8614

Mods = [ML1, ML2, ML3, ML4, ML5, ML6, ML7, ML8, ML9, ML10, ML11, ML12, ML13, ML14, ML15, ML16, ML17, ML18]
thetas = [theta[0],theta[1],theta[2],theta[3],theta[4],theta[5],theta[6], theta[7], theta[8], theta[9],theta[10], theta[11], theta[12],theta[13],theta[14],theta[15], theta[16], theta[17]]

#split different parameters into population, time, migration categories to calculate parameter values below 
PopSize = ['nu1','nu2','nu1O','nu3', 'nu1f', 'nu2O', 'nu2f','nu3O', 'nu3f', 'nuBot1' , 'nuBot2', 'nuRec1' , 'nuRec2','nu3bot','nu3rec',]
Time = ['Tsp','Tsp1','Tsp2','Tbot1', 'Trec1', 'Tbot2', 'Trec2']
Mig = ['m1','m2']
f = ['f']
n=0

#loop over each model to calculate estimates for each parameter based on Nref. Script can also be run
#with uncertainty values to estimate 95% bounds. 
OutFileName = "SAVSphylogeog_modelparams.txt"
OutFile = open(OutFileName, 'w')   
for model,theta in zip(Mods,thetas):
    OutFile.write("\n-----model %s-------\n" % model_names[n])
    ## Population sizes
    Nref = theta/(4*mu*L)
    params = model.keys()
    OutFile.write("Nref = %s\n" % round(Nref))
    OutFile.write("Theta = %s\n" % round(theta,2))
    for param in set(params) & set(PopSize):
    	OutFile.write("%s = %s\n" % (param, round(Nref*model[param])))
    for param in set(params) & set(Time):
    	OutFile.write("%s = %s\n" % (param, round(Nref*2*model[param]*gentime)))
    for param in set(params) & set(Mig):
    	OutFile.write("%s = %s\n" % (param, model[param]/(2*Nref)))
    for param in set(params) & set(f):
    	OutFile.write("%s = %s\n" % (param, model[param]))	
    n += 1
OutFile.close() 
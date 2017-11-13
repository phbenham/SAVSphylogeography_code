#!/usr/bin/env python 

import numpy
from numpy import array
import dadi
import sys
import pylab 
import SAVS2pop_DemographicModels

Usage="""This script performs initial optimization for each model. Each of the different models is fit
to the observed SFS to determine parameter values that optimize the likelihood for each model. 
10 different runs are performed for each model to find the parameter set with highest likelihood.
The model is then run a second, longer time starting from parameter estimates for the most likely model 
with max_iters=50 to ensure that a global optimum has been reached. 
Note AdmixmtDNA models are note included in this script as they are based on a different SFS
where the "CON" population is divided based on mtDNA haplogroup. Optimization code developed from 
example files distributed with ∂a∂i package (Gutenkunst et al. 2009) 
"""

#parse snps file
dd = dadi.Misc.make_data_dict("dadi_input_finaldataset_3Jan2017.tsv")
SAVSfoldedSpec = dadi.Spectrum.from_data_dict(dd, ['CON','MEX'], [25,16],
                                      polarized=False)
                                      
# model and data settings                                      
data = SAVSfoldedSpec
ns = data.sample_sizes
pts_l = [30,40,60]
                                      
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

#assign starting values for each parameter.  
nu1 = 5.0
nu2 = 5.0
nu3 = 5.0
nu1O = 1.0
nu1f = 1.0
nu2O = 1.0
nu2f = 1.0
nu3O = 1.0
nu3f = 1.0
nuBot1 = 5.0
nuBot2 = 5.0
nuRec1 = 5.0
nuRec2 = 5.0
nu3bot = 1.0
nu3rec = 1.0
Tsp = 3.0
Tsp1 = 3.0
Tsp2 = 3.0
Tbot1 = 1.0
Trec1 = 1.0
Tbot2 = 1.0
Trec2 = 1.0
m1 = 0.5
m2 = 0.5
f = 0.1

#specify parameter sets for each model
params = [[nu1, nu2, Tsp],
[nu1, nu2, nuBot2, nuRec2, Tsp, Tbot2, Trec2],
[nu1, nu2, nuBot1, nuRec1, Tsp, Tbot1, Trec1],
[nu1, nu2, nuBot1, nuRec1, nuBot2, nuRec2, Tsp, Tbot1, Trec1, Tbot2, Trec2],
[nu1, nu2O, nu2f, Tsp],
[nu1O, nu1f, nu2, Tsp],
[nu1O, nu1f, nu2O, nu2f, Tsp],
[nu1, nu2, Tsp, m1,m2],
[nu1, nu2, nuBot2, nuRec2, Tsp, Tbot2, Trec2, m1,m2],
[nu1, nu2, nuBot1, nuRec1, Tsp, Tbot1, Trec1, m1, m2],
[nu1, nu2, nuBot1, nuRec1, nuBot2, nuRec2, Tsp, Tbot1, Trec1, Tbot2, Trec2, m1, m2],
[nu1, nu2O, nu2f, Tsp, m1, m2],
[nu1O, nu1f, nu2, Tsp, m1, m2],
[nu1O, nu1f, nu2O, nu2f, Tsp, m1, m2],
[nu1,nu2,nu3,Tsp1,Tsp2,f, m1,m2],
[nu1,nu2,nu3,nu3bot,nu3rec,Tsp1,Tsp2,Tbot2, Trec2,f, m1,m2],
[nu1,nu2,nu3,nu1bot,nu1rec,nu3bot,nu3rec,Tsp1,Tsp2,Tbot1,Trec1,Tbot2,Trec2,f, m1,m2],
[nu1,nu1O, nu1f, nu2,nu3, nu3bot, nu3rec, Tsp1,Tsp2, Tbot2, Trec2, f, m1,m2]]

#specify upper and lower bounds for each parameter set for all models
upper_bounds = [[100, 100, 10],
[100, 100, 100, 100, 10, 10, 10],
[100, 100, 100, 100, 10, 10, 10],
[100, 100, 100, 100, 100, 100, 10, 10, 10, 10, 10],
[100, 100, 100, 10],
[100, 100, 100, 10],
[100, 100, 100, 100, 10],
[100, 100, 10, 10,10],
[100, 100, 100, 100, 10, 10, 10, 10,10],
[100, 100, 100, 100, 10, 10, 10, 10, 10],
[100, 100, 100, 100, 100, 100, 10, 10, 10, 10, 10, 10, 10],
[100, 100, 100, 10, 10, 10],
[100, 100, 100, 10, 10, 10],
[100, 100, 100, 100, 10, 10, 10],
[100,100,100,10,10,1, 10,10],
[100,100,100,100,100,10,10,10, 10,1, 10,10]
[100,100,100,100,100,100,100,10,10,10,10,10,10,1, 10,10],
[100,100, 100,100,100,100,100,10,10,10,10,1, 10,10]]

lower_bounds = [[1e-2, 1e-2, 1e-3],
[1e-2, 1e-2, 1e-2, 1e-2, 1e-3, 1e-3, 1e-3],
[1e-2, 1e-2, 1e-2, 1e-2, 1e-3, 1e-3, 1e-3],
[1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-3, 1e-3, 1e-3, 1e-3, 1e-3],
[1e-2, 1e-2, 1e-2, 1e-3],
[1e-2, 1e-2, 1e-2, 1e-3],
[1e-2, 1e-2, 1e-2, 1e-2, 1e-3],
[1e-2, 1e-2, 1e-3, 0,0],
[1e-2, 1e-2, 1e-2, 1e-2, 1e-3, 1e-3, 1e-3, 0,0],
[1e-2, 1e-2, 1e-2, 1e-2, 1e-3, 1e-3, 1e-3, 0, 0],
[1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-3, 1e-3, 1e-3, 1e-3, 1e-3, 0, 0],
[1e-2, 1e-2, 1e-2, 1e-3, 0, 0],
[1e-2, 1e-2, 1e-2, 1e-3, 0, 0],
[1e-2, 1e-2, 1e-2, 1e-2, 1e-3, 0, 0],
[1e-2,1e-2,1e-2,1e-3,1e-3,0, 0,0],
[1e-2,1e-2,1e-2,1e-2,1e-2,1e-3,1e-3,1e-3, 1e-3,0, 0,0],
[1e-2,1e-2,1e-2,1e-2,1e-2,1e-2,1e-2,1e-3,1e-3,1e-3,1e-3,1e-3,1e-3,0, 0,0],
[1e-2,1e-2, 1e-2,1e-2,1e-2,1e-2,1e-2,1e-3,1e-3,1e-3,1e-3,0, 0,0]]

#perform optimization for all models. For each model 10 optimizations are run and printed to file from model_names. For each 
#model longer runs are then performed (max_iters=50) with the optimized parameters from the run with the highest likelihood
for i in range(18):
	params1 =numpy.array(params[i])
	upper_bound= upper_bounds[i]
	lower_bound= lower_bounds[i]

	func = models[i]
	func_ex = dadi.Numerics.make_extrap_log_func(func)
	maxiters=10
	OutFileName = "ModelOutput/%" % model_names[i]
	OutFile = open(OutFileName, 'w')   
	for j in range(10):
		print j
		# Perturb  parameters before optimization. This does so by taking each
		# parameter up to a factor of two up or down.
		p0 = dadi.Misc.perturb_params(params1, fold=2, upper_bound=upper_bound,
									  lower_bound=lower_bound)
						  
		# Do the optimization. By default we assume that theta is a free parameter,
		# since it's trivial to find given the other parameters. If you want to fix
		# theta, add a multinom=False to the call.
		print('Beginning optimization ************************************************')
		popt = dadi.Inference.optimize_log(p0, data, func_ex, pts_l, 
										   lower_bound=lower_bound,
										   upper_bound=upper_bound,
										   verbose=len(p0), maxiter=maxiters)
		# The verbose argument controls how often progress of the optimizer should be
		# printed. It's useful to keep track of optimization process.
		print('Finshed optimization **************************************************')

		model = func_ex(popt, ns, pts_l)
		# Likelihood of the data given the model AFS.
		ll_opt = dadi.Inference.ll_multinom(model, data)
		param_out = list(popt) + [ll_opt]
		print param_out
		writeparam = str(param_out) + "\n"
		OutFile.write(writeparam)
OutFile.close()	
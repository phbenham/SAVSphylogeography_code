#!/usr/bin/env python 

import numpy
from numpy import array
import dadi
import sys
import pylab 
import SAVS2pop_DemographicModels

Usage="""Script to use Godambe information matrix methods (Coffmann et al. 2016) to
estimate parameter uncertainties based on bootstrap sfs generated 
using script: SAVSphylogeog_bootstrap.py
"""

#parse snps file
dd = dadi.Misc.make_data_dict("dadi_input_finaldataset_3Jan2017.tsv")
SAVSfoldedSpec = dadi.Spectrum.from_data_dict(dd, ['fresh','salt'], [10,10],
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

OutFile = open('Uncerts_output_10October2017.txt', 'w')  
for n in range(18):
	func = models[n]
	func_ex = dadi.Numerics.make_extrap_log_func(func)

	all_boot = [dadi.Spectrum.from_file('bootstrap/fsboot_{0:02d}'.format(ii)) 
				for ii in range(100)]
	uncerts = dadi.Godambe.GIM_uncert(func_ex, pts_l, all_boot, popt_float[n], data, 
									  multinom=True, return_GIM=True)                       
	OutFile.write('{0} estimated sd GIM uncerts: {1}'.format(model_names[n],uncerts[0]))                            
	inverseMat = numpy.linalg.inv(uncerts[1])

OutFile.close()

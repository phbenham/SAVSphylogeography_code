#!/usr/bin/env python 

import numpy
from numpy import array
import dadi
import sys
import pylab 

############################### model1: no mig constant size #############################
def split_Nomig(params, ns, pts):
	nu1, nu2, Tsp = params
	""""
	split with no migration model
	params = 
	nu1: pop size nominate
	nu2: pop size continent
	T: time of split
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	#allow migration and drift to occur along the two brances
	phi = dadi.Integration.two_pops(phi, xx, Tsp, nu1, nu2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
############################### model2: no mig, bottleneck mex ###########################
def split_bottleneckMex(params, ns, pts):
	nu1, nu2, nuBot2, nuRec2, Tsp, Tbot2, Trec2 = params
	""""
	split with no migration model, followed by bottleneck population 2
	params = nu1F, nu1B nu2F, T
	nu1: pop 1 size following split
	nu2: pop 2 constant size
    nuBot: The bottleneck size for pop1
    nuRec: The final size for pop1
    Tsp: time of split
    Tbot: duration of bottleneck (start of bottle neck = Tbot + Trec)
    Trec: end of bottleneck
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	phi = dadi.Integration.two_pops(phi,xx, Tsp, nu1=nu1, nu2=nu2)

	#bottleneck along both branches
	#phi = dadi.Integration.two_pops(phi, xx, Tbot1, nu1=nuBot1, nu2=nu2)
	#phi = dadi.Integration.two_pops(phi, xx, Trec1, nu1=nuRec1, nu2=nu2)
	
	phi = dadi.Integration.two_pops(phi, xx, Tbot2, nu1=nu1, nu2=nuBot2)
	phi = dadi.Integration.two_pops(phi, xx, Trec2, nu1=nu1, nu2=nuRec2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
############################### model3: no mig, bottleneck nom ###########################
def split_bottleneckNom(params, ns, pts):
	nu1, nu2, nuBot1, nuRec1, Tsp, Tbot1, Trec1 = params
	""""
	split with no migration model, followed by bottleneck in population 1
	params = nu1F, nu1B nu2F, T
	nu1: pop 1 size following split
	nu2: pop 2 constant size
    nuBot: The bottleneck size for pop1
    nuRec: The final size for pop1
    Tsp: time of split
    Tbot: duration of bottleneck (start of bottle neck = Tbot + Trec)
    Trec: end of bottleneck
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	phi = dadi.Integration.two_pops(phi,xx, Tsp, nu1=nu1, nu2=nu2)

	#bottleneck along both branches
	phi = dadi.Integration.two_pops(phi, xx, Tbot1, nu1=nuBot1, nu2=nu2)
	phi = dadi.Integration.two_pops(phi, xx, Trec1, nu1=nuRec1, nu2=nu2)
	
	#phi = dadi.Integration.two_pops(phi, xx, Tbot2, nu1=nu1, nu2=nuBot2)
	#phi = dadi.Integration.two_pops(phi, xx, Trec2, nu1=nu1, nu2=nuRec2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
		
############################### model4: no mig, bottleneck both ##########################
def split_bottleneckboth(params, ns, pts):
	nu1, nu2, nuBot1, nuRec1, nuBot2, nuRec2, Tsp, Tbot1, Trec1, Tbot2, Trec2 = params
	""""
	split with no migration model, followed by bottleneck in both populations
	params = nu1F, nu1B nu2F, T
	nu1: pop 1 size following split
	nu2: pop 2 constant size
    nuBot: The bottleneck size for pop1
    nuRec: The final size for pop1
    Tsp: time of split
    Tbot: duration of bottleneck (start of bottle neck = Tbot + Trec)
    Trec: end of bottleneck
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	phi = dadi.Integration.two_pops(phi,xx, Tsp, nu1=nu1, nu2=nu2)

	#bottleneck along both branches
	phi = dadi.Integration.two_pops(phi, xx, Tbot1, nu1=nuBot1, nu2=nu2)
	phi = dadi.Integration.two_pops(phi, xx, Trec1, nu1=nuRec1, nu2=nu2)
	
	phi = dadi.Integration.two_pops(phi, xx, Tbot2, nu1=nuRec1, nu2=nuBot2)
	phi = dadi.Integration.two_pops(phi, xx, Trec2, nu1=nuRec1, nu2=nuRec2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
############################### model5: no mig, exp grow mex  ############################	
def split_growMex(params, ns, pts):
	nu1, nu2O, nu2f, Tsp = params
	""""
	exponential population growth population2 only, no migration
	params = s,nu1, nu2, T
	s: proportion of ancestral assigned to pop1
	nu1: pop1 population size
	nu2: pop2 population size
	T: time of population split
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	#allow drift and exponential growth to occur along the two branches
	nu2_func = lambda t: nu2O*(nu2f/nu2O)**(t/Tsp)
	phi = dadi.Integration.two_pops(phi, xx, Tsp, nu1=nu1, nu2=nu2_func)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
############################### model6: no mig, exp grow nom  ############################
def split_growNom(params, ns, pts):
	nu1O, nu1f, nu2, Tsp = params
	""""
	exponential population growth in population_nominate only, no migration
	params = s,nu1, nu2, T
	s: proportion of ancestral assigned to pop1
	nu1: pop1 population size
	nu2: pop2 population size
	T: time of population split
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	#allow drift and exponential growth to occur along the two branches
	nu1_func = lambda t: nu1O*(nu1f/nu1O)**(t/Tsp)
	phi = dadi.Integration.two_pops(phi, xx, Tsp, nu1=nu1_func, nu2=nu2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
############################### model7: no mig, exp grow both ############################
def split_bothgrow(params, ns, pts):
	nu1O, nu1f, nu2O, nu2f, Tsp = params
	""""
	exponential population growth in both populations, no migration
	params = s,nu1, nu2, T
	s: proportion of ancestral assigned to pop1
	nu1: pop1 population size
	nu2: pop2 population size
	T: time of population split
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	#allow drift and exponential growth to occur along the two branches
	nu1_func = lambda t: nu1O*(nu1f/nu1O)**(t/Tsp)
	nu2_func = lambda t: nu2O*(nu2f/nu2O)**(t/Tsp)
	phi = dadi.Integration.two_pops(phi, xx, Tsp, nu1=nu1_func, nu2=nu2_func)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
############################### model8: mig, constant size both ##########################
def split_mig(params, ns, pts):
	nu1, nu2, Tsp, m1,m2 = params
	"""
	isolation with migration model
	params = nu1, nu2, T, m1, m2
	nu1 = ratio of pop size 1 to ancestral
	nu2 = ratio of pop size 2 to ancestral
	T = time of population split
	m1 = migration rate from 1 to 2
	m2 = migration rate from 2 to 1
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	#allow migration and drift to occur along the two brances
	phi = dadi.Integration.two_pops(phi, xx, Tsp, nu1, nu2, m12=m1, m21=m2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
	
############################### model9: mig, bottleneck mex ##############################
def split_bottleneckMex_mig(params, ns, pts):
	nu1, nu2, nuBot2, nuRec2, Tsp, Tbot2, Trec2, m1,m2 = params
	""""
	split with no migration model, followed by bottleneck population 2
	params = nu1F, nu1B nu2F, T
	nu1: pop 1 size following split
	nu2: pop 2 constant size
    nuBot: The bottleneck size for pop1
    nuRec: The final size for pop1
    Tsp: time of split
    Tbot: duration of bottleneck (start of bottle neck = Tbot + Trec)
    Trec: end of bottleneck
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	phi = dadi.Integration.two_pops(phi,xx, Tsp, nu1=nu1, nu2=nu2)

	#bottleneck along both branches
	#phi = dadi.Integration.two_pops(phi, xx, Tbot1, nu1=nuBot1, nu2=nu2)
	#phi = dadi.Integration.two_pops(phi, xx, Trec1, nu1=nuRec1, nu2=nu2)
	
	phi = dadi.Integration.two_pops(phi, xx, Tbot2, nu1=nu1, nu2=nuBot2, m12=m1, m21=m2)
	phi = dadi.Integration.two_pops(phi, xx, Trec2, nu1=nu1, nu2=nuRec2, m12=m1, m21=m2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs	
############################### model10: mig, bottleneck nom #############################
def split_bottleneckNom_mig(params, ns, pts):
	nu1, nu2, nuBot1, nuRec1, Tsp, Tbot1, Trec1, m1, m2 = params
	""""
	split with no migration model, followed by bottleneck in population 1
	params = nu1F, nu1B nu2F, T
	nu1: pop 1 size following split
	nu2: pop 2 constant size
    nuBot: The bottleneck size for pop1
    nuRec: The final size for pop1
    Tsp: time of split
    Tbot: duration of bottleneck (start of bottle neck = Tbot + Trec)
    Trec: end of bottleneck
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	phi = dadi.Integration.two_pops(phi,xx, Tsp, nu1=nu1, nu2=nu2)

	#bottleneck along both branches
	phi = dadi.Integration.two_pops(phi, xx, Tbot1, nu1=nuBot1, nu2=nu2, m12=m1, m21=m2)
	phi = dadi.Integration.two_pops(phi, xx, Trec1, nu1=nuRec1, nu2=nu2, m12=m1, m21=m2)
	
	#phi = dadi.Integration.two_pops(phi, xx, Tbot2, nu1=nu1, nu2=nuBot2)
	#phi = dadi.Integration.two_pops(phi, xx, Trec2, nu1=nu1, nu2=nuRec2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
############################### model11: mig, bottleneck both ############################
def split_bottleneckboth_mig(params, ns, pts):
	nu1, nu2, nuBot1, nuRec1, nuBot2, nuRec2, Tsp, Tbot1, Trec1, Tbot2, Trec2, m1, m2 = params
	""""
	split with no migration model, followed by bottleneck in both populations
	params = nu1F, nu1B nu2F, T
	nu1: pop 1 size following split
	nu2: pop 2 constant size
    nuBot: The bottleneck size for pop1
    nuRec: The final size for pop1
    Tsp: time of split
    Tbot: duration of bottleneck (start of bottle neck = Tbot + Trec)
    Trec: end of bottleneck
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	phi = dadi.Integration.two_pops(phi,xx, Tsp, nu1=nu1, nu2=nu2)

	#bottleneck along both branches
	phi = dadi.Integration.two_pops(phi, xx, Tbot1, nu1=nuBot1, nu2=nu2, m12=m1, m21=m2)
	phi = dadi.Integration.two_pops(phi, xx, Trec1, nu1=nuRec1, nu2=nu2, m12=m1, m21=m2)
	
	phi = dadi.Integration.two_pops(phi, xx, Tbot2, nu1=nuRec1, nu2=nuBot2, m12=m1, m21=m2)
	phi = dadi.Integration.two_pops(phi, xx, Trec2, nu1=nuRec1, nu2=nuRec2, m12=m1, m21=m2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
############################### model12: mig, exp grow mex ###############################
def split_growMex_mig(params, ns, pts):
	nu1, nu2O, nu2f, Tsp, m1, m2 = params
	""""
	exponential population growth population2 only, asymmetrical migration
	params = s,nu1, nu2, T
	s: proportion of ancestral assigned to pop1
	nu1: pop1 population size
	nu2: pop2 population size
	T: time of population split
	m1: migration rate pop2 -> 1, i.e. proportion of individual sin pop1 from pop2
	m2: migration rate pop1-> 2, i.e. proportion of individuals in pop2 from pop1
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	#allow drift and exponential growth to occur along the two branches
	nu2_func = lambda t: nu2O*(nu2f/nu2O)**(t/Tsp)
	
	phi = dadi.Integration.two_pops(phi, xx, Tsp, nu1=nu1, nu2=nu2_func, m12=m1, m21=m2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs	
############################### model13: mig, exp grow nom ###############################
def split_growNom_mig(params, ns, pts):
	nu1O, nu1f, nu2, Tsp, m1, m2 = params
	""""
	exponential population growth population1 only, asymmetrical migration
	params = s,nu1, nu2, T
	s: proportion of ancestral assigned to pop1
	nu1: pop1 population size
	nu2: pop2 population size
	T: time of population split
	m1: migration rate pop2 -> 1, i.e. proportion of individual sin pop1 from pop2
	m2: migration rate pop1-> 2, i.e. proportion of individuals in pop2 from pop1
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	#allow drift and exponential growth to occur along the two branches
	nu1_func = lambda t: nu1O*(nu1f/nu1O)**(t/Tsp)

	phi = dadi.Integration.two_pops(phi, xx, Tsp, nu1=nu1_func, nu2=nu2, m12=m1, m21=m2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
############################### model14: mig, exp grow both ##############################
def split_bothgrow_mig(params, ns, pts):
	nu1O, nu1f, nu2O, nu2f, Tsp, m1, m2 = params
	""""
	exponential population growth both populations, asymmetrical migration
	params = s,nu1, nu2, T
	s: proportion of ancestral assigned to pop1
	nu1: pop1 population size
	nu2: pop2 population size
	T: time of population split
	m1: migration rate pop2 -> 1, i.e. proportion of individual sin pop1 from pop2
	m2: migration rate pop1-> 2, i.e. proportion of individuals in pop2 from pop1
	"""
	#creates the search grid
	xx = dadi.Numerics.default_grid(pts)
	
	# creates the ancestral population
	phi = dadi.PhiManip.phi_1D(xx)
	
	#splits ancestor into two populations
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	
	#allow drift and exponential growth to occur along the two branches
	nu1_func = lambda t: nu1O*(nu1f/nu1O)**(t/Tsp)
	nu2_func = lambda t: nu2O*(nu2f/nu2O)**(t/Tsp)
	phi = dadi.Integration.two_pops(phi, xx, Tsp, nu1=nu1_func, nu2=nu2_func, m12=m1, m21=m2)
	
	#simulates the sfs
	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx))
	return fs
##########################################################################################
##########################################################################################		
########################## model15: ghost pop, constant size both ########################
def threepop_admix(params, ns, pts): ## parse params
	nu1,nu2,nu3,Tsp1,Tsp2,f, m1,m2 = params
	
	## create a search grid
	xx = dadi.Numerics.default_grid(pts)

	## make ancestral pop that splits into two
	phi = dadi.PhiManip.phi_1D(xx)
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)

	## allow drift to occur along each of these branches
	phi = dadi.Integration.two_pops(phi, xx, Tsp1, nu1=nu1, nu2=nu2)

	## mexican pop diverges from population 1
	phi = dadi.PhiManip.phi_2D_to_3D_split_1(xx,phi)
	
	## allow drift and migration to occur along all three lineages
	phi = dadi.Integration.three_pops(phi, xx, Tsp2, nu1=nu1, nu2=nu2, nu3=nu3, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)

	## admixture of pop 2 into pop 1
	phi = dadi.PhiManip.phi_3D_admix_2_and_3_into_1(phi, f, 0, xx, xx, xx)

	##remove other continental population following admixture, leaving just two lineages
	phi = dadi.PhiManip.remove_pop(phi,xx,2)

	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx,))
	return fs

########################## model16: ghost pop, bottleneck mex ############################
def threepop_admix_bottleneckMex(params, ns, pts): ## parse params
	nu1,nu2,nu3,nu3bot,nu3rec,Tsp1,Tsp2,Tbot2, Trec2,f, m1,m2 = params
		
	## create a search grid
	xx = dadi.Numerics.default_grid(pts)

	## make ancestral pop that splits into two
	phi = dadi.PhiManip.phi_1D(xx)
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)

	## allow drift to occur along each of these branches
	phi = dadi.Integration.two_pops(phi, xx, Tsp1, nu1=nu1, nu2=nu2)

	## mexican pop diverges from population 1
	phi = dadi.PhiManip.phi_2D_to_3D_split_1(xx,phi)
	
	## allow drift and migration to occur along all three lineages
	phi = dadi.Integration.three_pops(phi, xx, Tsp2, nu1=nu1, nu2=nu2, nu3=nu3, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)

	## bottleneck occurs along mexico lineage
	phi = dadi.Integration.three_pops(phi, xx, Tbot2, nu1=nu1, nu2=nu2, nu3=nu3bot, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)
	phi = dadi.Integration.three_pops(phi, xx, Trec2, nu1=nu1, nu2=nu2, nu3=nu3rec, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)
	
	## admixture of pop 2 into pop 1
	phi = dadi.PhiManip.phi_3D_admix_2_and_3_into_1(phi, f, 0, xx, xx, xx)

	##remove other continental population following admixture, leaving just two lineages
	phi = dadi.PhiManip.remove_pop(phi,xx,2)

	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx,))
	return fs
########################## model17: ghost pop, bottleneck nom ############################
def threepop_admix_bottleneckNom(params, ns, pts): ## parse params
	nu1,nu2,nu3,nu1bot,nu1rec,Tsp1,Tsp2,Tbot1, Trec1, f, m1,m2 = params	
	
	## create a search grid
	xx = dadi.Numerics.default_grid(pts)

	## make ancestral pop that splits into two
	phi = dadi.PhiManip.phi_1D(xx)
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)

	## allow drift to occur along each of these branches
	phi = dadi.Integration.two_pops(phi, xx, Tsp1, nu1=nu1, nu2=nu2)

	## mexican pop diverges from population 1
	phi = dadi.PhiManip.phi_2D_to_3D_split_1(xx,phi)
	
	## allow drift and migration to occur along all three lineages
	phi = dadi.Integration.three_pops(phi, xx, Tsp2, nu1=nu1, nu2=nu2, nu3=nu3, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)

	## bottleneck occurs within one of nominate lineages
	phi = dadi.Integration.three_pops(phi, xx, Tbot1, nu1=nu1bot, nu2=nu2, nu3=nu3, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)
	phi = dadi.Integration.three_pops(phi, xx, Trec1, nu1=nu1rec, nu2=nu2, nu3=nu3, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)
	
	## admixture of pop 2 into pop 1
	phi = dadi.PhiManip.phi_3D_admix_2_and_3_into_1(phi, f, 0, xx, xx, xx)

	##remove other continental population following admixture, leaving just two lineages
	phi = dadi.PhiManip.remove_pop(phi,xx,2)

	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx,))
	return fs

########################## model18: ghost pop, bottleneck both ###########################
def threepop_admix_bottleneckboth(params, ns, pts): ## parse params
	nu1,nu2,nu3,nu1bot,nu1rec,nu3bot,nu3rec,Tsp1,Tsp2,Tbot1,Trec1,Tbot2,Trec2,f, m1,m2 = params	
	
	## create a search grid
	xx = dadi.Numerics.default_grid(pts)

	## make ancestral pop that splits into two
	phi = dadi.PhiManip.phi_1D(xx)
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)

	## allow drift to occur along each of these branches
	phi = dadi.Integration.two_pops(phi, xx, Tsp1, nu1=nu1, nu2=nu2)

	## mexican pop diverges from population 1
	phi = dadi.PhiManip.phi_2D_to_3D_split_1(xx,phi)
	
	## allow drift and migration to occur along all three lineages
	phi = dadi.Integration.three_pops(phi, xx, Tsp2, nu1=nu1, nu2=nu2, nu3=nu3, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)
	
	##bottleneck1
	phi = dadi.Integration.three_pops(phi, xx, Tbot1, nu1=nu1bot, nu2=nu2, nu3=nu3, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)
	phi = dadi.Integration.three_pops(phi, xx, Trec1, nu1=nu1rec, nu2=nu2, nu3=nu3, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)
	##bottleneck2
	phi = dadi.Integration.three_pops(phi, xx, Tbot2, nu1=nu1rec, nu2=nu2, nu3=nu3bot, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)
	phi = dadi.Integration.three_pops(phi, xx, Trec2, nu1=nu1rec, nu2=nu2, nu3=nu3rec, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)
	
	## admixture of pop 2 into pop 1
	phi = dadi.PhiManip.phi_3D_admix_2_and_3_into_1(phi, f, 0, xx, xx, xx)

	##remove other continental population following admixture, leaving just two lineages
	phi = dadi.PhiManip.remove_pop(phi,xx,2)

	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx,))
	return fs
	
########################## model19: ghost pop, exp grow mex ##############################
def threepop_admix_growMex(params, ns, pts): ## parse params	
	nu1,nu2,nu3O,nu3f,Tsp1,Tsp2,f, m1,m2 = params
	
	## create a search grid
	xx = dadi.Numerics.default_grid(pts)

	## make ancestral pop that splits into two
	phi = dadi.PhiManip.phi_1D(xx)
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)

	## allow drift to occur along each of these branches
	phi = dadi.Integration.two_pops(phi, xx, Tsp1, nu1=nu1, nu2=nu2)

	## mexican pop diverges from population 1
	phi = dadi.PhiManip.phi_2D_to_3D_split_1(xx,phi)
	
	#allow drift and exponential growth to occur along the two branches
	nu3_func = lambda t: nu3O*(nu3f/nu3O)**(t/Tsp2)	
	
	## allow drift and migration to occur along all three lineages
	phi = dadi.Integration.three_pops(phi, xx, Tsp2, nu1=nu1, nu2=nu2, nu3=nu3_func, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)

	## admixture of pop 2 into pop 1
	phi = dadi.PhiManip.phi_3D_admix_2_and_3_into_1(phi, f, 0, xx, xx, xx)

	##remove other continental population following admixture, leaving just two lineages
	phi = dadi.PhiManip.remove_pop(phi,xx,2)

	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx,))
	return fs	
########################## model20: ghost pop, exp grow nom ##############################
def threepop_admix_growNom(params, ns, pts): ## parse params	
	nu1,nu1O, nu1f, nu2,nu3, nu3bot, nu3rec, Tsp1,Tsp2, Tbot2, Trec2, f, m1,m2 = params
	
	## create a search grid
	xx = dadi.Numerics.default_grid(pts)

	## make ancestral pop that splits into two
	phi = dadi.PhiManip.phi_1D(xx)
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)

	## allow drift to occur along each of these branches
	phi = dadi.Integration.two_pops(phi, xx, Tsp1, nu1=nu1, nu2=nu2)

	## mexican pop diverges from population 1
	phi = dadi.PhiManip.phi_2D_to_3D_split_1(xx,phi)
	
	#allow drift and exponential growth to occur along the two branches
	nu1_func = lambda t: nu1O*(nu1f/nu1O)**(t/Tsp2)	
	
	## allow drift and migration to occur along all three lineages
	phi = dadi.Integration.three_pops(phi, xx, Tsp2, nu1=nu1_func, nu2=nu2, nu3=nu3, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)

	## mexico bottleneck
	phi = dadi.Integration.three_pops(phi, xx, Tbot2, nu1=nu1_func, nu2=nu2, nu3=nu3bot, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)
	phi = dadi.Integration.three_pops(phi, xx, Trec2, nu1=nu1_func, nu2=nu2, nu3=nu3rec, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)
	
	## admixture of pop 2 into pop 1
	phi = dadi.PhiManip.phi_3D_admix_2_and_3_into_1(phi, f, 0, xx, xx, xx)

	##remove other continental population following admixture, leaving just two lineages
	phi = dadi.PhiManip.remove_pop(phi,xx,2)

	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx,))
	return fs
########################## model21: ghost pop, exp grow both ##############################
def threepop_admix_growboth(params, ns, pts): ## parse params	
	nu1, nu1O, nu1f,nu2,nu3O, nu3f,Tsp1,Tsp2,f, m1,m2 = params
	
	## create a search grid
	xx = dadi.Numerics.default_grid(pts)

	## make ancestral pop that splits into two
	phi = dadi.PhiManip.phi_1D(xx)
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)

	## allow drift to occur along each of these branches
	phi = dadi.Integration.two_pops(phi, xx, Tsp1, nu1=nu1, nu2=nu2)

	## mexican pop diverges from population 1
	phi = dadi.PhiManip.phi_2D_to_3D_split_1(xx,phi)
	
	#allow drift and exponential growth to occur along the two branches
	nu1_func = lambda t: nu1O*(nu1f/nu1O)**(t/Tsp2)	
	nu3_func = lambda t: nu3O*(nu3f/nu3O)**(t/Tsp2)
	
	## allow drift and migration to occur along all three lineages
	phi = dadi.Integration.three_pops(phi, xx, Tsp2, nu1=nu1_func, nu2=nu2, nu3=nu3_func, m12=0.0, m21=0.0, m13=m1, m31=m2, m23=0.0, m32=0.0)

	## admixture of pop 2 into pop 1
	phi = dadi.PhiManip.phi_3D_admix_2_and_3_into_1(phi, f, 0, xx, xx, xx)

	##remove other continental population following admixture, leaving just two lineages
	phi = dadi.PhiManip.remove_pop(phi,xx,2)

	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx,))
	return fs	
########################## model22: ghost pop, constant size both nomig ##################
def threepop_admix_iso(params, ns, pts): ## parse params
	nu1,nu2,nu3,Tsp1,Tsp2,f = params
	
	## create a search grid
	xx = dadi.Numerics.default_grid(pts)

	## make ancestral pop that splits into two
	phi = dadi.PhiManip.phi_1D(xx)
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)

	## allow drift to occur along each of these branches
	phi = dadi.Integration.two_pops(phi, xx, Tsp1, nu1=nu1, nu2=nu2)

	## mexican pop diverges from population 1
	phi = dadi.PhiManip.phi_2D_to_3D_split_1(xx,phi)
	
	## allow drift and migration to occur along all three lineages
	phi = dadi.Integration.three_pops(phi, xx, Tsp2, nu1=nu1, nu2=nu2, nu3=nu3)

	## admixture of pop 2 into pop 1
	phi = dadi.PhiManip.phi_3D_admix_2_and_3_into_1(phi, f, 0, xx, xx, xx)

	##remove other continental population following admixture, leaving just two lineages
	phi = dadi.PhiManip.remove_pop(phi,xx,2)

	fs = dadi.Spectrum.from_phi(phi, ns, (xx,xx,))
	return fs										
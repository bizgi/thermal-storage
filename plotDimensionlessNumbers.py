# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:50:05 2018

@author: bizgi
"""

import render


# --- < Stratification Number >  ----------------------------------------------

# plot Str Number for different velocity cases
StVel = {
	'trace': 'caseVel',
	'caseTemp': '333',
	'caseVel': ['0.1', '0.2', '0.4', '0.6', '0.8'],
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
	'numberOfNodes' : 16,
	'tankHigh' : 1, # meter
	'xLabel' : 't* [-]',
	'yLabel': 'Str [-]',
	'legend' : ['v1', 'v2', 'v3', 'v4', 'v5'],
	'savePlot' : 'False',
	'saveDpi' : 300,
	'compareCase1' : 'data-1',
	'compareCase2' : 'data-2'
	}

# plot Str Number for different temperature cases
StTemp = {
	'trace': 'caseTemp',
	'caseTemp': ['318', '323', '328', '333', '338'],
	'caseVel': '0.6',
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],	
	'numberOfNodes' : 16,
	'tankHigh' : 1, # meter
	'xLabel' : 't* [-]',
	'yLabel': 'Str [-]',
	'legend' : ['T1', 'T2', 'T3', 'T4', 'T5'],
	'savePlot' : 'True',
	'saveDpi' : 300,
	'compareCase1' : 'data-1',
	'compareCase2' : 'data-2'
	}

# --- </ Stratification Number > ----------------------------------------------


# --- < Richardson Number >  --------------------------------------------------

# plot Ri Number for different velocity cases
RiVel = {
	'trace': 'caseVel',
	'caseTemp': '318',
	'caseVel': ['0.1', '0.2', '0.4', '0.6', '0.8'],
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
	'tankHigh' : 1, # meter
	'xLabel' : 't* [-]',
	'yLabel': 'Ri [-]',
	'legend' :  ['v1', 'v2', 'v3', 'v4', 'v5'],
	'savePlot' : 'False',
	'saveDpi' : 300,
	'compareCase1' : 'data-1',
	'compareCase2' : 'data-2'
	}

# plot Ri Number for different temperature cases
RiTemp = {
	'trace': 'caseTemp',
	'caseTemp': ['318', '323', '328', '333', '338'],
	'caseVel': '0.8',
	'caseTime': [ 'd5', 'd10','d15', 'd20', 'd25', 'd30'],
	'tankHigh' : 1, # meter
	'xLabel' : 't* [-]',
	'yLabel': 'Ri [-]',
	'legend' :  ['T1', 'T2', 'T3', 'T4', 'T5'],
	'savePlot' : 'False',
	'saveDpi' : 300,
	'compareCase1' : 'data-1',
	'compareCase2' : 'data-2'
	}

# --- </ Richardson Number > --------------------------------------------------


# --- < Mix Number >  ---------------------------------------------------------

# plot Mix Number for different velocity cases
MixVel = {
	'trace': 'caseVel',
	'caseTemp': '333',
	'caseVel': ['0.1', '0.2', '0.4', '0.6', '0.8'],
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
	'tankHigh' : 1, # meter
	'tankD' : 0.45, # meter
	'numberOfVolume' : 15,
	'xLabel' : 't* [-]',
	'yLabel': 'MIX [-]',
#	'yLabel' : '$\eta_{Str}$',
	'legend' :  ['v1', 'v2', 'v3', 'v4', 'v5'],
	'savePlot' : 'False',
	'saveDpi' : 300,
	'compareCase1' : 'data-1',
	'compareCase2' : 'data-2'
	}

# plot Mix Number for different temperature cases
MixTemp = {
	'name' : 't-MIX',
	'trace': 'caseTemp',
	'caseTemp': ['318', '323', '328', '333', '338'],
	'caseVel': '0.6',
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
	'tankHigh' : 1, # meter
	'tankD' : 0.45, # meter
	'numberOfVolume' : 15,
	'xLabel' : 't* [-]',
	'yLabel': 'MIX [-]',
#	'yLabel' : '$\eta_{Str}$',
	'legend' : ['T1', 'T2', 'T3', 'T4', 'T5'],
	'savePlot' : 'False',
	'saveDpi' : 300,
	'compareCase1' : 'data-1',
	'compareCase2' : 'data-2'
	}

# --- </ Mix Number > --------------------------------------------------


#-- <data files> --------------------------------------------------------------
path = './data/engelli-volAve.csv'
path2= './data/engelsiz-volAve.csv'
#-- </data files> --------------------------------------------------------------


# -- <plot> -------------------------------------------------------------------
# -- uncomment to plot

# -- Stratification Number
#render.St(path, StVel)
#render.St(path, StTemp)

# -- Richardson Number
#render.Ri(path, RiVel)
#render.Ri(path, RiTemp)

# -- Mix Number
#render.Mix(path, MixVel)
#render.Mix(path, MixTemp)

#--- </plot> ------------------------------------------------------------------



# -- <compare plot> -----------------------------------------------------------
# -- uncomment to plot

# -- Stratification Number
#render.compare(render.St, StVel, path, path2)
#render.compare(render.St, StTemp, path, path2)

# -- Richardson Number
#render.compare(render.Ri, RiVel, path, path2)
#render.compare(render.Ri, RiTemp, path, path2)

# -- Mix Number
#render.compare(render.Mix, MixVel, path, path2)
#render.compare(render.Mix, MixTemp, path, path2)

# -- </compare plot> ----------------------------------------------------------

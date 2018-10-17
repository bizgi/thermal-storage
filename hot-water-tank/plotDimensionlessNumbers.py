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
	'legend' : ['Re=210', 'Re=335', 'Re=625', 'Re=1000', 'Re=1270'],
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
	'legend' : ['Gr=3.1E10', 'Gr=3.7E10', 'Gr=4.2E10', 'Gr=4.7E10', 'Gr=5.2E10'],
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
	'xLabel' : 't* [-]',
	'yLabel': 'Ri [-]',
	'legend' :  ['Re=210', 'Re=335', 'Re=625', 'Re=1000', 'Re=1270']
	}

# plot Ri Number for different temperature cases
RiTemp = {
	'trace': 'caseTemp',
	'caseTemp': ['318', '323', '328', '333', '338'],
	'caseVel': '0.8',
	'caseTime': [ 'd5', 'd10','d15', 'd20', 'd25', 'd30'],
	'xLabel' : 't* [-]',
	'yLabel': 'Ri [-]',
	'legend' :  ['Gr=3.1E10', 'Gr=3.7E10', 'Gr=4.2E10', 'Gr=4.7E10', 'Gr=5.2E10']
	}

# --- </ Richardson Number > --------------------------------------------------




#-- <data files> --------------------------------------------------------------
path = './data/engelli-volAve.csv'
path2= './data/engelsiz-volAve.csv'
#-- </data files> --------------------------------------------------------------


# -- <plot> -------------------------------------------------------------------
# -- uncomment to plot

# --- --- --- --- --- Stratification Number
#render.St(path, StVel)
#render.St(path, StTemp)



#render.plot(path, ZTRe)
#render.plot(path, ZTt)
#render.plot(path, tToutGr)
#render.plot(path, tToutRe)

#--- </plot> ------------------------------------------------------------------



# -- <compare plot> -----------------------------------------------------------
# -- uncomment to plot

# --- --- --- --- --- --- --- --- Stratification Number
#render.compare(St, StVel, path, path2)
#render.compare(St, StTemp, path, path2)




# -- </compare plot> ----------------------------------------------------------

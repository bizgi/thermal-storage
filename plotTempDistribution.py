# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:50:05 2018

@author: bizgi
"""

import render


# --- <cases for plot> --------------------------------------------------------

# plot temperature distibution for different temperature cases
ZTGr = {
		'trace': 'caseTemp',
		'caseTemp': ['318', '323', '328', '333', '338'],
		'caseVel': '0.1', 
		'caseTime': 'd30',
		'xVal': 'Z',
		'yVal': 'T',
		'legend' : ['Gr=3.1E10', 'Gr=3.7E10', 'Gr=4.2E10', 'Gr=4.7E10', 'Gr=5.2E10'],
		'non-dimensional' : 'True',
		'xLabel' : 'Z* [-]',
		'yLabel': 'T* [-]',
		'savePlot' : 'False',
		'saveDpi' : 300,
		'compareCase1' : 'data-1',
		'compareCase2' : 'data-2'
		}

# plot temperature distibution for different velocity cases
ZTRe = {
		'trace': 'caseVel',
		'caseTemp': '328',
		'caseVel': ['0.1', '0.2', '0.4', '0.6', '0.8'],
		'caseTime': 'd30',
		'xVal': 'Z',
		'yVal': 'T',
		'legend' : ['Re=210', 'Re=335', 'Re=625', 'Re=1000', 'Re=1270'],
		'non-dimensional' : 'True',
		'xLabel' : 'Z* [-]',
		'yLabel': 'T* [-]',
		'savePlot' : 'False',
		'saveDpi' : 300,
		'compareCase1' : 'data-1',
		'compareCase2' : 'data-2'
		}

# plot temperature distibution for different time cases
ZTt = {
		'trace': 'caseTime',
		'caseTemp': '328',
		'caseVel': '0.2',
		'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
		'xVal': 'Z',
		'yVal': 'T',
		'legend' : ['t*=0.167', 't*=0.333', 't*=0.500', 't*=0.667', 't*=0.833', 't*=1.000'],
		'non-dimensional' : 'True',
		'xLabel' : 'Z* [-]',
		'yLabel': 'T* [-]',
		'savePlot' : 'False',
		'saveDpi' : 300,
		'compareCase1' : 'data-1',
		'compareCase2' : 'data-2'
		}

# plot tank outlet temperature for different temperature cases
tToutGr = {
		'trace': 'caseTemp',
		'caseTemp': ['318', '323', '328', '333', '338'],
		'caseVel': '0.4', 
		'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
		'xVal': 'caseTime',
		'yVal': 'Tout',
		'legend' : ['Gr=3.1E10', 'Gr=3.7E10', 'Gr=4.2E10', 'Gr=4.7E10', 'Gr=5.2E10'],
		'non-dimensional' : 'True',
		'xLabel' : 't* [-]',
		'yLabel': 'Tout* [-]',
		'savePlot' : 'False',
		'saveDpi' : 300,
		'compareCase1' : 'data-1',
		'compareCase2' : 'data-2'
		}

# plot tank outlet temperature for different temperature cases
tToutRe = {
		'trace': 'caseVel',
		'caseTemp': '333',
		'caseVel': ['0.1', '0.2', '0.4', '0.6', '0.8'], 
		'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
		'xVal': 'caseTime',
		'yVal': 'Tout',
		'legend' : ['Re=210', 'Re=335', 'Re=625', 'Re=1000', 'Re=1270'],
		'non-dimensional' : 'True',
		'xLabel' : 't* [-]',
		'yLabel': 'Tout* [-]',
		'savePlot' : 'False',
		'saveDpi' : 300,
		'compareCase1' : 'data-1',
		'compareCase2' : 'data-2'
		}

#--- </cases for plot> --------------------------------------------------------


#-- <data files> --------------------------------------------------------------
path = './data/engelli-volAve.csv'
path2= './data/engelsiz-volAve.csv'
#-- </data files> --------------------------------------------------------------


# -- <plot> -------------------------------------------------------------------
# -- uncomment to plot

#render.plot(path, ZTGr)
#render.plot(path, ZTRe)
#render.plot(path, ZTt)
#render.plot(path, tToutGr)
#render.plot(path, tToutRe)

#--- </plot> ------------------------------------------------------------------


# -- <compare plot> -----------------------------------------------------------
# -- uncomment to plot

#render.compare(plot, ZTGr, path, path2)
#render.compare(plot, ZTRe, path, path2)
#render.compare(plot, ZTt, path, path2)
#render.compare(plot, tToutGr, path, path2)
#render.compare(plot, tToutRe, path, path2)

# -- </compare plot> ----------------------------------------------------------





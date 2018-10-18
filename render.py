# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:50:05 2018

@author: bizgi
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
import csv
import pandas as pd
import matplotlib.lines as mlines

def getCase(path, caseTemp, caseVel, caseTime):
	
	
	#read csv file and stroe values	
	df = pd.read_csv(path).astype(str)
	delta = pd.DataFrame.from_records(df)
	
	
	# Case velosity
	qVel = delta['caseVel'].str.contains(caseVel)
	velFiltered = delta[qVel]

	# Case Temperature
	qTemp = velFiltered ['caseTemp'].str.contains(caseTemp)
	tempFiltered = velFiltered[qTemp]
	
	# Case time
	qTime = tempFiltered ['caseTime'].str.contains(caseTime)
	timeFiltered = tempFiltered[qTime]
	
#	print (timeFiltered['T'])
	
	head = list(timeFiltered)
		
#	data = np.array(timeFiltered).astype(float)
	
	return head, timeFiltered



def plot(path, plotThis):
	
#	path = plotThis['path']
	trace = plotThis['trace']
	caseVel= ['0.1', '0.2', '0.4', '0.6', '0.8']
	caseTemp = ['318', '323', '328', '333', '338']
	caseTime = ['d5', 'd10','d15', 'd20', 'd25', 'd30']
	label = plotThis['legend']
	time = [0, 0.166666667, 0.333333333, 0.5, 0.666666667, 0.833333333, 1]
	
	marker = ['D', '<', '+', '>', 'o', '*', '1', '2', '3', 'v', '^', 'h', 'd']
	
	xLabel = plotThis['xLabel']
	yLabel = plotThis['yLabel']
	plt.figure()
	xData = []
	yData = []
	
	if (plotThis['yVal'] == 'Tout'):
		if (plotThis['trace'] == 'caseTemp'):
			yData = []
			xData = []
			for i in range (len(plotThis[trace])):
				yd = [float(caseTemp[i])]
				for j in range(len(plotThis['caseTime'])):
					pdata = getCase(path, plotThis['caseTemp'][i], plotThis['caseVel'], plotThis['caseTime'][j])
					x = time[j]
					y = np.array(pdata[1][plotThis['yVal']]).astype(float)[0]
					yd.append(y)
				
				ydD = np.interp(yd, (288, 338), (0 ,1))
				yData.append(ydD)
				
	#			xData.append([5, 10, 15, 20, 25, 30])
	#			print (x, y)
	
			print('vel = ', plotThis['caseVel'])
			saveName = 'tToutGr'
			for n in range(len(yData)):
				x = makeSpline(time, yData[n])[0]
				y = makeSpline(time, yData[n])[1]
				plt.plot(x, y, marker = marker[n], label = label[n], markevery=40)
				xData.append(time)

		elif (plotThis['trace'] == 'caseVel'):
			yData = []
			xData = []
			for i in range (len(plotThis[trace])):
				yd = [float(plotThis['caseTemp'])]
				for j in range(len(plotThis['caseTime'])):
					pdata = getCase(path, plotThis['caseTemp'], plotThis[trace][i], plotThis['caseTime'][j])
					x = time[j]
					y = np.array(pdata[1][plotThis['yVal']]).astype(float)[0]
					yd.append(y)
				
				ydD = np.interp(yd, (288, float(plotThis['caseTemp'])), (0 ,1))
				yData.append(ydD)
				
	#			xData.append([5, 10, 15, 20, 25, 30])
	#			print (x, y)
				
	#			xData.append([5, 10, 15, 20, 25, 30])
	#			print (x, y)	
	
			print('Temp = ', plotThis['caseTemp'])
			saveName = 'tToutRe'
			for n in range(len(yData)):
				x = makeSpline(time, yData[n])[0]
				y = makeSpline(time, yData[n])[1]
#				print(y)
				plt.plot(x, y, marker = marker[n], label = label[n], markevery=40)
				xData.append(time)

	else:

		for i in range(len(plotThis[trace])):
			if (trace == 'caseVel'):
				pdata = getCase(path, plotThis['caseTemp'], plotThis['caseVel'][i],  plotThis['caseTime'])
				saveName = 'T=' + plotThis['caseTemp'] + ' t=' + plotThis['caseTime']
	#			print(pdata)
	
			elif (trace == 'caseTemp'):		
				pdata = getCase(path, plotThis[trace][i], plotThis['caseVel'], plotThis['caseTime'])
				saveName = 'v=' + plotThis['caseVel'] + ' t=' + plotThis['caseTime']
#				print(pdata)
	
			elif (trace == 'caseTime'):
				pdata = getCase(path, plotThis['caseTemp'], plotThis['caseVel'], plotThis[trace][i])
				saveName = 'T=' + plotThis['caseTemp'] + ' v=' + plotThis['caseVel']
	#			print(pdata)
	
	
			x = np.array(pdata[1][plotThis['xVal']]).astype(float)
			y = np.array(pdata[1][plotThis['yVal']]).astype(float)
#			print(x,y)
		
			if (plotThis['non-dimensional'] == 'True'):
				
				# make data non-dimensional
				xx = np.interp(x, (x.min(), x.max()), (0 ,1))
				
				if (trace == 'caseTemp'):
					flTrace = np.array([float(j) for j in plotThis[trace]])
					yy = np.interp(y, (y.min(), flTrace.max() ), (0 ,1))
					
				else:
					yy = np.interp(y, (y.min(), (float(plotThis['caseTemp'])+0.15)), (0 ,1))				
		
			
				x1 = makeSpline(xx, yy)[0]
				y1 = makeSpline(xx, yy)[1]
				plt.plot(x1, y1, marker=marker[i], label = plotThis['legend'][i], markevery=40)
				
				xData.append(xx)
				yData.append(yy)
			
			else:
				x1 = makeSpline(x, y)[0]
				y1 = makeSpline(x, y)[1]
				plt.plot(x1, y1, marker=marker[i], label = plotThis['legend'][i], markevery=40)
				xData.append(x)
				yData.append(y)
				
	#			t, c, k = interpolate.splrep(x , y, s=0, k=2)
	#			xSmooth = np.linspace(min(x), max(x), 200)
	#			spline = interpolate.BSpline(t, c, k, extrapolate=False)
	#			plt.plot(xSmooth, spline(xSmooth), label = plotThis['legend'][i], marker=marker[i], markevery=20)
	
	plt.legend(loc=0)
	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	plt.tight_layout()
	if (plotThis['savePlot'] == 'True'):
		plt.savefig('.\savedPlots\\' + trace + '-' + saveName+'.png', format='png', dpi=plotThis['saveDpi'])
	return xData, yData, xLabel, yLabel, label



# -------------- Plot All Cases -----------------------------------------------
def plotAll():
	caseTemp= ['318', '323', '328', '333', '338']
	caseVel = ['0.1', '0.2', '0.4', '0.6', '0.8']
	caseTime = ['d5', 'd10','d15', 'd20', 'd25', 'd30']
	
	for i in range(len(caseTemp)):
		for j in range(len(caseTime)):
			
			plotZTRe = {
			'path': 'engelli.csv',
			'trace': 'caseVel',
			'caseTemp': caseTemp[i],
			'caseVel': ['0.1', '0.2', '0.4', '0.6', '0.8'],
			'caseTime': caseTime[j],
			'xVal': 'Z',
			'yVal': 'T',
			'legend' : ['Re=210', 'Re=335', 'Re=625', 'Re=1000', 'Re=1270'],
			'non-dimensional' : 'True',
			'xLabel' : 'Z* [-]',
			'yLabel': 'T* [-]'
			}
			
			plotZTGR = {
			'path': 'engelli.csv',
			'trace': 'caseTemp',
			'caseTemp': ['318', '323', '328', '333', '338'],
			'caseVel': caseVel[i], 
			'caseTime': caseTime[j],
			'xVal': 'Z',
			'yVal': 'T',
			'legend' : ['Gr=3.1E10', 'Gr=3.7E10', 'Gr=4.2E10', 'Gr=4.7E10', 'Gr=5.2E10'],
			'non-dimensional' : 'True',
			'xLabel' : 'Z* [-]',
			'yLabel': 'T* [-]'
			}
		
			plot(plotZTRe)
			plot(plotZTGR)
			
	for i in range(len(caseTemp)):
		for j in range(len(caseVel)):
			
			plotZTt = {
				'path': 'engelli.csv',
				'trace': 'caseTime',
				'caseTemp':  caseTemp[i],
				'caseVel': caseVel[j], 
				'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
				'xVal': 'Z',
				'yVal': 'T',
				'legend' : ['t=5 m', 't=10 m', 't=15 m', 't=20 m', 't=25 m', 't=30 m'],
				'non-dimensional' : 'True',
				'xLabel' : 'Z* [-]',
				'yLabel': 'T* [-]'
				}
			
			plot(plotZTt)

#------------------------------------------------------------------------------

			
#-------------Calculate and Plot Stratification Number ------------------------
	
def St(path, sData):
	pth = path
	trace = sData['trace']
	caseTemp = sData['caseTemp']
	caseVel = sData['caseVel']
	caseTime = sData['caseTime']
	xLabel = sData['xLabel']
	yLabel = sData['yLabel']
	label = sData['legend']
	
	tankH = sData['tankHigh']
	nodes = sData['numberOfNodes']
	
	marker = ['D', '*', '+', 'v', 'o', '<', '1', '2', '3', 'v', '^', 'h', 'd']
	time = [0, 0.166666667, 0.333333333, 0.5, 0.666666667, 0.833333333, 1]
	
	plt.figure()
	
	if (trace == 'caseVel'):
		strNumber = []
		xData = []
		for i in range(len(caseVel)):
			strNo = [0]
			for j in range(len(caseTime)):
				pdata = getCase(pth, caseTemp, caseVel[i], caseTime[j])
				T = np.array(pdata[1]['T']).astype(float)
#				print('------------------')
				zg = []
				for k in range(len(T)-1):
#					print(k)
					zGrad = (T[k+1] - T[k]) / (tankH/(nodes-1))
					zg.append(zGrad)
#					print(zGrad)
				
				strat = ( np.sum(zg[0:]) / (nodes-1) ) / (float(caseTemp)- 288)
				strNo.append(strat)
#				print(strat)
			
			print(strNo)
			strNumber.append(strNo)
#			print('------------------')
#		print(strNumber)
			
		for n in range(len(strNumber)):	
			x = makeSpline(time, strNumber[n])[0]
			y = makeSpline(time, strNumber[n])[1]
			plt.plot(x, y, marker = marker[n], label = label[n], markevery=40)
			xData.append(time)
	
		plt.legend(loc=0)
		plt.xlabel(xLabel)
		plt.ylabel(yLabel)
		plt.tight_layout()

		yData = strNumber
		if (sData['savePlot'] == 'True'):
			plt.savefig('.\savedPlots\\' + trace + '- Str' +'.png', format='png', dpi=sData['saveDpi'])
		return xData, yData, xLabel, yLabel, label
		

	elif (trace == 'caseTemp'):
		strNumber = []
		xData = []
		for i in range(len(caseTemp)):
			strNo = [0]
			for j in range(len(caseTime)):
				pdata = getCase(pth, caseTemp[i], caseVel, caseTime[j])
				T = np.array(pdata[1]['T']).astype(float)
#				print(T)
				zg = []
				for k in range(len(T)-1):
					zGrad = (T[k+1] - T[k]) / (tankH/(nodes-1))
					zg.append(zGrad)
#					print(zGrad)
				
				strat = ( np.sum(zg[0:]) / (nodes-1)) / (float(caseTemp[i])- 288)
				strNo.append(strat)
#				print(strat)
			
			print(strNo)
			strNumber.append(strNo)
			
#		print(strNumber)
		for n in range(len(strNumber)):	
			x = makeSpline(time, strNumber[n])[0]
			y = makeSpline(time, strNumber[n])[1]
			plt.plot(x, y, marker = marker[n], label = label[n], markevery=40)
			xData.append(time)
		plt.legend(loc= 0)
		plt.xlabel(xLabel)
		plt.ylabel(yLabel)
		plt.tight_layout()
		yData = strNumber
		if (sData['savePlot'] == 'True'):
			plt.savefig('.\savedPlots\\' + trace + '- Str' +'.png', format='png', dpi=sData['saveDpi'])
		return xData, yData, xLabel, yLabel, label
#------------------------------------------------------------------------------
	
	
#-------------------- Calculate Richardson Number -----------------------------
def Ri(path, sData):
	pth = path
	trace = sData['trace']
	caseTemp = sData['caseTemp']
	caseVel = sData['caseVel']
	caseTime = sData['caseTime']
	xLabel = sData['xLabel']
	yLabel = sData['yLabel']
	label = sData['legend']
	marker = ['D', '*', '+', 'v', 'o', '<', '1', '2', '3', 'v', '^', 'h', 'd']
	time = [0, 0.166666667, 0.333333333, 0.5, 0.666666667, 0.833333333, 1]
	
	# Ri = g * Beta * H * (Ttop - Tbottom) / v^2
	g = 9.81
	H = sData['tankHigh']
	betas = {
			'318' : 2.86e-4,
			'323' : 3.07e-4,
			'328' : 3.26e-4,
			'333' : 3.46e-4,
			'338' : 3.64e-4
			}
	plt.figure()
	
	if (trace == 'caseVel'):
		RiNumber = []
		xData = []
		for i in range(len(caseVel)):
			RiN = [0]
			for j in range(len(caseTime)):
				pdata = getCase(pth, caseTemp, caseVel[i], caseTime[j])
				T = np.array(pdata[1]['T']).astype(float)
				
				Ttop = T[-1]
				Tbottom = T[0]
				
				print(Ttop)
				print(Tbottom)
				beta = betas[caseTemp]
				
				Ri = g * beta * H * (Ttop - Tbottom) / (float(caseVel[i])**2)
				
				print(Ri)
				RiN.append(Ri)

			RiNumber.append(RiN)
				
#		print (RiNumber)
    
		for n in range(len(RiNumber)):	
			x = makeSpline(time, RiNumber[n])[0]
			y = makeSpline(time, RiNumber[n])[1]
			plt.plot(x, y, marker = marker[n], label = label[n], markevery=40)
			xData.append(time)
		plt.legend(loc='upper right')
		plt.xlabel(xLabel)
		plt.ylabel(yLabel)
		plt.tight_layout()
		yData = RiNumber
		if (sData['savePlot'] == 'True'):
			plt.savefig('.\savedPlots\\' + trace + '- Ri' +'.png', format='png', dpi=sData['saveDpi'])		
		
		return xData, yData, xLabel, yLabel, label	

	if (trace == 'caseTemp'):
		RiNumber = []
#		print(RiNumber)
		xData = []
		for i in range(len(caseTemp)):
			RiN = [0]
			print('----' + caseTemp[i])
			for j in range(len(caseTime)):
				pdata = getCase(pth, caseTemp[i], caseVel, caseTime[j])
				T = np.array(pdata[1]['T']).astype(float)
				
				Ttop = T[-1]
				Tbottom = T[0]
				
#				print(Ttop)
#				print(Tbottom)
				beta = betas[caseTemp[i]]
				Ri = g * beta * H * (Ttop - Tbottom) / (float(caseVel)**2)
				
				print(Ri)
				RiN.append(Ri)

			RiNumber.append(RiN)
				
#		print (RiNumber)
    
		for n in range(len(RiNumber)):
			x = makeSpline(time, RiNumber[n])[0]
			y = makeSpline(time, RiNumber[n])[1]
			plt.plot(x, y, marker = marker[n], label = label[n], markevery=40)
			xData.append(time)
		plt.legend(loc='upper right')
		plt.xlabel(xLabel)
		plt.ylabel(yLabel)
		plt.tight_layout()
		yData = RiNumber
		if (sData['savePlot'] == 'True'):
			plt.savefig('.\savedPlots\\' + trace + '- Ri' +'.png', format='png', dpi=sData['saveDpi'])
		return xData, yData, xLabel, yLabel, label
#------------------------------------------------------------------------------

		
#-------------- Discharge Efficiency ------------------------------------------

# Olfa Abdelhak et all. 10.1007/s12273-015-0216-9
# etha = Q_out(t) / Q_st (t=0)
# Q_out (t) = (rho * V * Cp )_out * (Tout - Tin) 
# Q_st (t=0) = rho * V * Cp * (Tini - Tin)
		

def disEff(path, sData):
	pth = path
	trace = sData['trace']
	caseTemp = sData['caseTemp']
	caseVel = sData['caseVel']
	caseTime = sData['caseTime']
	xLabel = sData['xLabel']
	yLabel = sData['yLabel']
	label = sData['legend']
	marker = ['D', '*', '+', 'v', 'o', '<', '1', '2', '3', 'v', '^', 'h', 'd']
	times = [300, 600, 900, 1200, 1500, 1800]
	time = [ 0.166666667, 0.333333333, 0.5, 0.666666667, 0.833333333, 1]	
	rhos = {
			'318' : 995.2,
			'323' : 994.3,
			'328' : 993.3,
			'333' : 992.3,
			'338' : 991.2
			}
	rho = rhos[caseTemp]
	
	Cps = {
			'318' : 4180,
			'323' : 4180,
			'328' : 4181,
			'333' : 4181,
			'338' : 4182
			}
	Cp = Cps[caseTemp]
	plt.figure()
	
	if (trace == 'caseTime'):
		DisEff = []
		xData = []
		for i in range(len(caseTime)):
			print('-------' + caseTime[i])
			Deff = []
			for j in range(len(caseVel)):
				pdata = getCase(pth, caseTemp, caseVel[j], caseTime[i])
				T = np.array(pdata[1]['Tout']).astype(float)
				Tm = np.array(pdata[1]['ToutManto']).astype(float)
				
				Tin = 288.15
				Tout = T[0]
				ToutManto = Tm[0]
				
				H = 1 # m
				D = 0.45 # m
				volTank = (np.pi * D**2 / 4 ) * H				 
				
				volOut = float(caseVel[j]) * (np.pi * 0.02**2 / 4) * float(times[i])
				volOutManto = 0.02 * (np.pi * 0.02**2 / 4)  * float(times[i])
				
				
				print(Tout)
		
				Qout = volOut * rho * Cp * (Tout - Tin)	
				Qst =volTank * rho * Cp * (float(caseTemp) + 0.15 - Tin) + (volOutManto*rho * Cp * (float(caseTemp) + 0.15 - ToutManto))
				etha = Qout / Qst
				
				print (etha)

				Deff.append(etha)

			DisEff.append(Deff)
				
#		print (DisEff)
    
		for n in range(len(DisEff)):	
			plt.plot([210, 335, 625, 1000, 1270], DisEff[n], marker = marker[n], label = label[n])
			xData.append([210, 335, 625, 1000, 1270])
		plt.legend(loc='lower left')
		plt.xlabel(xLabel)
		plt.ylabel(yLabel)
		
		yData = DisEff
		return xData, yData, xLabel, yLabel, label
	
	if (trace == 'caseVel'):
		DisEff = []
		xData=[]
		for i in range(len(caseVel)):
			Deff = []
			print('-------' + caseVel[i])
			for j in range(len(caseTime)):
				pdata = getCase(pth, caseTemp, caseVel[i], caseTime[j])
				T = np.array(pdata[1]['Tout']).astype(float)
				Tm = np.array(pdata[1]['ToutManto']).astype(float)
				
				Tin = 288.15
				Tout = T[0]
				ToutManto = Tm[0]
				Tini = float(caseTemp)
				
				H = 1 # m
				D = 0.45 # m
				volTank = (np.pi * D**2 / 4 ) * H				 
				
				volOut = float(caseVel[i]) * (np.pi * 0.02**2 / 4) * float(times[j])
				volOutManto = 0.02 * (np.pi * 0.02**2 / 4)  * float(times[j])
				
#				Qmanto = volOutManto * rho * Cp * (Tini +0.15 - ToutManto)
#		
#				Qout = volOut * rho * Cp * (Tout - Tin)
#				Qst = volTank * rho * Cp * (Tini + 0.15 - Tin) 
				
				Qmanto = volOutManto * rho * Cp * (Tini +0.15 - ToutManto)		
				Qout = volOut * rho * Cp * (Tout - Tin)
				Qst = volTank * rho * Cp * (Tini + 0.15 - Tin) 				
				
				print (Qmanto, Qout, Qst)
				etha = Qout / (Qst + Qmanto)
				
				print (etha)

				Deff.append(etha)

			DisEff.append(Deff)
				
#		print (DisEff)
    
		for n in range(len(DisEff)):
			x = makeSpline(time, DisEff[n])[0]
			y = makeSpline(time, DisEff[n])[1]
			plt.plot(x, y, marker = marker[n], label = label[n], markevery=40)
			xData.append(time)
		plt.legend(loc='lower left')
		plt.xlabel(xLabel)
		plt.ylabel(yLabel)
		
		yData = DisEff
		return xData, yData, xLabel, yLabel, label
#------------------------------------------------------------------------------


###############################################################################
# ---- MIX Number -------------------------------------------------------------
###############################################################################

# MIX = (M_str - M_act) / (M_str - M_fullMix)
# Rho = -0.0039*T^2+2.087*T+721.2   -- 288.15 - 338.15
# Cp = 0.0118*T^2-7.3162*T+5313.1--  288.15 - 338.15
		
def rho(T):
	Rho = -0.0039 * T**2 + 2.087 * T + 721.2
	return Rho

def cp(T):
	Cp = 0.0118 * T**2 - 7.3162 * T + 5313.1
	return Cp 


def Mix(path, sData):
	pth = path
	trace = sData['trace']
	caseTemp = sData['caseTemp']
	caseVel = sData['caseVel']
	caseTime = sData['caseTime']
	xLabel = sData['xLabel']
	yLabel = sData['yLabel']
	label = sData['legend']
	marker = ['D', '*', '+', 'v', 'o', '<', '1', '2', '3', 'v', '^', 'h', 'd']
	time = [ 0.166666667, 0.333333333, 0.5, 0.666666667, 0.833333333, 1]
	# Number of volumes : 15
	# each volume
	pi = np.pi
	H = sData['tankHigh'] # m
	D = sData['tankD'] # m
	nVol = sData['numberOfVolume']
	vol_i = (pi * D**2 / 4 ) * (1/15)
	vol = (pi * D**2 / 4 ) * H
#	print (vol_i) 
	
	if (trace == 'caseVel'):
		MixNumber = []
		xData = []
		for i in range(len(caseVel)):
			MixN = []
			print('-----', caseVel[i])
			for j in range(len(caseTime)):
				pdata = getCase(pth, caseTemp, caseVel[i], caseTime[j])
				T = np.array(pdata[1]['T']).astype(float)
				
				#-- E_act - M_act --------------------------------------------
				TvolAve = []
				yi = H/(2*nVol)
				yii = [0.016666667, 0.066666667, 0.133333333, 0.2, 0.266666667, 0.333333333, 0.4, 0.466666667, 0.533333333, 0.6, 0.666666667, 0.733333333, 0.8, 0.866666667, 0.9, 0.983333333 ]
				E_acti = []
				M_acti = []
				for k in range(len(T)-1):
#					print('kk-------------------', k)
					if ( k == 0 ):
						vol_i2 = vol_i / 2
						Tv = (T[k+1]*vol_i + T[k]*vol_i2) / (vol_i + vol_i2)
						Tv=T[k]
					elif (k==14):
						vol_i2 = vol_i / 2
#						Tv = (T[k+1]*vol_i2 + T[k]*vol_i) / (vol_i + vol_i2)
						Tv = (T[k+1] + T[k]) / 2
#						Tv=T[k+1]
					else:
						Tv = (T[k+1] + T[k]) / 2
						vol_i2 = vol_i
#						Tv=T[k+1]
					
#					Tv = (T[k+2] + T[k+1] + T[k]) / 3
					
					
					TvolAve.append(Tv)
#					print('-----')
#					print('----------------------', vol_i2)
#					E_act = vol_i * rho(Tv) * cp(Tv) * Tv
#					M_act = M_act + vol_i * rho(Tv) * cp(Tv) * Tv * yi
					E_acti.append(vol_i * rho(Tv) * cp(Tv) * Tv)
					M_acti.append(vol_i * rho(Tv) * cp(Tv) * Tv * yi)

					yi = yi + H/nVol
#					print ('yi ------------------------------ ', yi)
				
				E_act = sum(E_acti)
				M_act = sum(M_acti)
#				print(TvolAve)
#				print('-------' , E_act, '--' , M_act)
				
				# -- E_fullMix - M_fullMix----------------------------------------
				Tave_full_mix = np.average(TvolAve)
				E_fullMix = vol * rho(Tave_full_mix) * cp(Tave_full_mix) * Tave_full_mix
				M_fullMix = 0.5 * E_fullMix
				
#				print(M_fullMix, '--', E_fullMix)
				
				# -- E_str -- M_str -----------------------------------------------
				Tcold = np.min(TvolAve)
				Thot = np.max(TvolAve)
				
				# E_str = Vcold * rho(Tcold) * cp(Tcold) * Tcold + Vhot * rho(Thot) * cp(Thot) * Thot
				# vol = Vcold + Vhot
				# two linear eq. solve for Vcold and Vhot
				
				E_str = E_act
				A = np.array([[rho(Tcold) * cp(Tcold) * Tcold, rho(Thot) * cp(Thot) * Thot], [1, 1]])
				B = np.array([E_str, vol])
				sol = np.linalg.solve(A,B)
				
				Vcold = sol[0]
				Vhot = sol[1]
				
				ycold = ((Vcold/vol) * H )/ 2
				yhot = (Vcold/vol) * H + ((Vhot/vol) * H) / 2
				
				M_str = ycold * Vcold * rho(Tcold) * cp(Tcold) * Tcold + yhot * Vhot * rho(Thot) * cp(Thot) * Thot
				
				Mix = (M_str - M_act) / (M_str - M_fullMix)
#				Mix =100*  (1 -( (M_str - M_act) / (M_str - M_fullMix) ))
				
				print(Mix)

				MixN.append(Mix)

			MixNumber.append(MixN)				
				
		plt.figure()
		for n in range(len(MixNumber)):
			x = makeSpline(time, MixNumber[n])[0]
			y = makeSpline(time, MixNumber[n])[1]
			plt.plot(x, y, marker = marker[n], label = label[n], markevery=40)
			xData.append(time)
		plt.legend(loc='upper left')
		plt.xlabel(xLabel)
		plt.ylabel(yLabel)
		plt.tight_layout()
		yData = MixNumber
		if (sData['savePlot'] == 'True'):
			plt.savefig('.\savedPlots\\' + trace + '- Mix' +'.png', format='png', dpi=sData['saveDpi'])
		return xData, yData, xLabel, yLabel, label
				
	if (trace == 'caseTemp'):
		MixNumber = []
		xData = []
		for i in range(len(caseTemp)):
			MixN = []
			print('-----', caseTemp[i])
			for j in range(len(caseTime)):
				pdata = getCase(pth, caseTemp[i], caseVel, caseTime[j])
				T = np.array(pdata[1]['T']).astype(float)
				
				#-- E_act - M_act --------------------------------------------
				TvolAve = []
				yi = H/(2*nVol)
				yii = [0.016666667, 0.066666667, 0.133333333, 0.2, 0.266666667, 0.333333333, 0.4, 0.466666667, 0.533333333, 0.6, 0.666666667, 0.733333333, 0.8, 0.866666667, 0.9, 0.983333333 ]
				E_act = 0
				M_act = 0
				for k in range(len(T)-1):
					Tv = (T[k+1] + T[k]) / 2
#					Tv = T[k]
#					if (k == 0):
#						vol_i = vol_i/ 2
#						
#					if (k==15):
#						vol_i = vol_i / 2
#					print (vol_i)
					TvolAve.append(Tv)
			
#					print('-----')
#					print(yi)
					
					E_act = E_act + vol_i * rho(Tv) * cp(Tv) * Tv
					M_act = M_act + vol_i * rho(Tv) * cp(Tv) * Tv * yi

					yi = yi + H/nVol
#					print (yi)
				
#				print(TvolAve)
#				print('-------' , E_act, '--' , M_act)
				
				# -- E_fullMix - M_fullMix----------------------------------------
				Tave_full_mix = np.average(TvolAve)
				E_fullMix = vol * rho(Tave_full_mix) * cp(Tave_full_mix) * Tave_full_mix
				M_fullMix = 0.5 * E_fullMix
				
#				print(M_fullMix, '--', E_fullMix)
				
				# -- E_str -- M_str -----------------------------------------------
				Tcold = np.min(TvolAve)
				Thot = np.max(TvolAve)
				
				# E_str = Vcold * rho(Tcold) * cp(Tcold) * Tcold + Vhot * rho(Thot) * cp(Thot) * Thot
				# vol = Vcold + Vhot
				# two linear eq. solve for Vcold and Vhot
				
				E_str = E_act
				A = np.array([[rho(Tcold) * cp(Tcold) * Tcold, rho(Thot) * cp(Thot) * Thot], [1, 1]])
				B = np.array([E_str, vol])
				sol = np.linalg.solve(A,B)
				
				Vcold = sol[0]
				Vhot = sol[1]
				
				ycold = ((Vcold/vol) * H )/ 2
				yhot = (Vcold/vol) * H + ((Vhot/vol) * H) / 2
				
				M_str = ycold * Vcold * rho(Tcold) * cp(Tcold) * Tcold + yhot * Vhot * rho(Thot) * cp(Thot) * Thot
				Mix = (M_str - M_act) / (M_str - M_fullMix)
#				Mix =100*  (1 -( (M_str - M_act) / (M_str - M_fullMix) ))
				
				print(Mix)

				MixN.append(Mix)

			MixNumber.append(MixN)				
				
		plt.figure()	
		for n in range(len(MixNumber)):
			x = makeSpline(time, MixNumber[n])[0]
			y = makeSpline(time, MixNumber[n])[1]
			plt.plot(x, y, marker = marker[n], label = label[n], markevery=40)
			xData.append(time)
		plt.legend(loc='upper left')
		plt.xlabel(xLabel)
		plt.ylabel(yLabel)	
		plt.tight_layout()

		yData = MixNumber
		if (sData['savePlot'] == 'True'):
			plt.savefig('.\savedPlots\\' + trace + '- Mix' +'.png', format='png', dpi=sData['saveDpi'])
		return xData, yData, xLabel, yLabel, label
#------------------------------------------------------------------------------



def makeSpline(x, y):
		t, c, k = interpolate.splrep(x , y, s=0, k=2)
		xSmooth = np.linspace(min(x), max(x), 200)
#		spline = interpolate.BSpline(t, c, k, extrapolate=False)
		spline = interpolate.CubicSpline(x , y, bc_type='natural')
		ySmooth = spline(xSmooth)
#		print(ySmooth)
		ys2 = []
#		for i in range(len(ySmooth)) :
#			if (ySmooth[i] < 0):
#				yy = 0
##				yy = 0.9999
#			else:
#				yy = ySmooth[i]
#			
##			print(yy)
#			ys2.append(yy)
		
		
		return xSmooth, ySmooth
	
	
	
def validate():
#	path = 'knutsen-val.csv'
	path = 'zachar-val.csv'
	
		
	df = pd.read_csv(path).astype(str)
	delta = pd.DataFrame.from_records(df)
	
	q1 = delta['C'].str.contains('CFD')
	case1 = delta[q1]
	
	q2 = delta['C'].str.contains('Exp')
	case2 = delta[q2]

#	print(case1X, case1Y)
	
	x1 = np.array(case1['T']).astype(float)
	y1 = np.array(case1['Z']).astype(float)
#	print(y1)
	
	x2 = np.array(case2['T']).astype(float)
	y2 = np.array(case2['Z']).astype(float)

#	plt.figure(figsize=(5,8))
	
	fig, ax1 = plt.subplots(figsize=(5,8))
#	plt.tight_layout()
	plt.rcParams.update({'font.size': 12})
#	SMALL_SIZE = 13
#	plt.rc('font', size=12)
#	plt.rc('axes', titlesize=14)
#	plt.rc('axes', labelsize=14)
#	plt.rc('xtick', labelsize=14)
#	plt.rc('ytick', labelsize=14)
#	ax2 = ax1.twinx()
	
	ax1.plot(x1, y1, label='CFD Model', color = 'C0')
	ax1.scatter(x2, y2, color = 'C2', label = 'Experiment (Knudsen, S., 2004)')
	
#	ax2.scatter(x2, yy, color='C8', label='Mesh')
	
#	ax2.set_ylabel('s')
	ax1.legend(loc=0)
	ax1.set_xlabel('T* [-]')
	ax1.set_ylabel('Z* [-]')
#	plot.legend(loc=0)
	sName = 'validate-kun'
#	plt.savefig('.\img\\'+ sName + '.png', format='png', dpi=300)
	
	
#validate()	


def meshInd():
#	path = 'knutsen-val.csv'
	path = 'zachar-mesh-ind.csv'
	
		
	df = pd.read_csv(path).astype(str)
	delta = pd.DataFrame.from_records(df)
	
	q1 = delta['C'].str.contains('m1')
	case1 = delta[q1]
	
	q2 = delta['C'].str.contains('m2')
	case2 = delta[q2]
	
	q3 = delta['C'].str.contains('m3')
	case3 = delta[q3]
	
	q4 = delta['C'].str.contains('m4')
	case4 = delta[q4]
	
	q5 = delta['C'].str.contains('m5')
	case5 = delta[q5]
	
	q6 = delta['C'].str.contains('Exp')
	case6 = delta[q6]
	
	q7 = delta['C'].str.contains('Num')
	case7 = delta[q7]
#	print(case1X, case1Y)
	
	y = np.array(case1['Z']).astype(float)	
	x1 = np.array(case1['T']).astype(float)
	x2 = np.array(case2['T']).astype(float)
	x3 = np.array(case3['T']).astype(float)
	x4 = np.array(case4['T']).astype(float)
	x5 = np.array(case5['T']).astype(float)
	
	y0 = np.array(case6['Z']).astype(float)	
	x0 = np.array(case6['T']).astype(float)
	
	y01 = np.array(case7['Z']).astype(float)	
	x01 = np.array(case7['T']).astype(float)
#	print(y0, x0)
	plt.figure(figsize=(5,8))
	
#	fig, ax1 = plt.subplots(figsize=(5,8))

	plt.rcParams.update({'font.size': 12})
#	SMALL_SIZE = 13
#	plt.rc('font', size=12)
	plt.rc('axes', titlesize=12)
	plt.rc('axes', labelsize=12)
	plt.rc('xtick', labelsize=14)
	plt.rc('ytick', labelsize=14)
#	ax2 = ax1.twinx()
	plt.scatter(x0, y0, label='Experiment (Zachar, A., 2003)', color = 'C2')
	
	plt.plot(x1, y, label='CFD - 43768 Mesh', color = 'C0', dashes=[1,1])
	plt.plot(x2, y, label='CFD - 101557 Mesh', color = 'C1', dashes=[2,2])	
	plt.plot(x3, y, label='CFD - 208067 Mesh', color = 'C3')	
	plt.plot(x4, y, label='CFD - 441111 Mesh', color = 'C5', dashes=[5,1])
	plt.plot(x5, y, label='CFD - 686656 Mesh', color = 'C7', dashes=[9,4])
	
	plt.plot(x01, y01, label='Numerical (Zachar, A., 2003)', color = 'C9')
	
	plt.text(0.7 , 0.05, ' $T_{ini}$ = 41 $^oC$ \n $T_{in}$ = 20 $^oC$ \n Q = 1.6 L/min \n t = 1500 s')
	
	

#	plt.scatter(x0, y0, label='Experiment (Knudsen, S., 2004)', color = 'C0')
#	
#	plt.plot(x1, y, label='CFD - 70171 Mesh', color = 'C2', dashes=[1,1])
#	plt.plot(x2, y, label='CFD - 101507 Mesh', color = 'C1', dashes=[2,2])	
#	plt.plot(x3, y, label='CFD - 132071 Mesh', color = 'C3')	
#	plt.plot(x4, y, label='CFD - 154933 Mesh', color = 'C5', dashes=[5,1])


#	ax2.scatter(x2, yy, color='C8', label='Mesh')
	
#	ax2.set_ylabel('s')
	plt.legend(loc=0)
	
	plt.xlabel('T* [-]')
	plt.ylabel('Z* [-]')
	plt.tight_layout()
#	plot.legend(loc=0)
	sName = 'validate-mesh-zac'
#	plt.savefig('.\img\\'+ sName + '.png', format='png', dpi=300)
	
	
	


#------ MIX Number Cases ------------------------------------------------------

MixVel = {
	'trace': 'caseVel',
	'caseTemp': '333',
	'caseVel': ['0.1', '0.2', '0.4', '0.6', '0.8'],
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
	'xLabel' : 't* [-]',
#	'yLabel': 'MIX [-]',
	'yLabel' : '$\eta_{Str}$',
	'legend' : ['Re=210', 'Re=335', 'Re=625', 'Re=1000', 'Re=1270']
	}

#calcMix(cMixVel)

MixTemp = {
	'name' : 't-MIX',
	'trace': 'caseTemp',
	'caseTemp': ['318', '323', '328', '333', '338'],
	'caseVel': '0.6',
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
	'xLabel' : 't* [-]',
	'yLabel': 'MIX [-]',
#	'yLabel' : '$\eta_{Str}$',
	'legend' : ['Gr=3.1E10', 'Gr=3.7E10', 'Gr=4.2E10', 'Gr=4.7E10', 'Gr=5.2E10']
	}

#calcMix(cMixTemp)
					
					
#------------------------------------------------------------------------------




# ------------- Discharge Efficiency Cases ------------------------------------
	
disEffTime = {
	'trace': 'caseTime',
	'caseTemp': '328',
	'caseVel': ['0.1', '0.2', '0.4', '0.6', '0.8'],
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
	'xLabel' : 'Re [-]',
	'yLabel': 'Ethe [-]',
	'legend' :  ['t=5', 't=10', 't=15', 't=20', 't=25', 't=30']
	}

	
#calcDisEff(EffDataTime)

disEffVel = {
	'trace': 'caseVel',
	'caseTemp': '328',
	'caseVel': ['0.1', '0.2', '0.4', '0.6', '0.8'],
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
	'xLabel' : 't [-]',
	'yLabel': '$\eta_{discharge}$ [-]',
	'legend' :  ['Re=210', 'Re=335', 'Re=625', 'Re=1000', 'Re=1270']
	}


#calcDisEff('engelli-volAve.csv',EffDataVel)


#------------------------------------------------------------------------------


#---------- Richardson Number Cases -------------------------------------------

RiVel = {
	'trace': 'caseVel',
	'caseTemp': '318',
	'caseVel': ['0.1', '0.2', '0.4', '0.6', '0.8'],
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
	'xLabel' : 't* [-]',
	'yLabel': 'Ri [-]',
	'legend' :  ['Re=210', 'Re=335', 'Re=625', 'Re=1000', 'Re=1270']
	}

#calcRichardson(RiDataVel)

RiTemp = {
	'trace': 'caseTemp',
	'caseTemp': ['318', '323', '328', '333', '338'],
	'caseVel': '0.8',
	'caseTime': [ 'd5', 'd10','d15', 'd20', 'd25', 'd30'],
	'xLabel' : 't* [-]',
	'yLabel': 'Ri [-]',
	'legend' :  ['Gr=3.1E10', 'Gr=3.7E10', 'Gr=4.2E10', 'Gr=4.7E10', 'Gr=5.2E10']
	}

#calcRichardson(RiDataTemp)


#------------------------------------------------------------------------------
	
#--------Stratification Number Cases ------------------------------------------
		
StVel = {
	'trace': 'caseVel',
	'caseTemp': '323',
	'caseVel': ['0.1', '0.2', '0.4', '0.6', '0.8'],
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
	'xLabel' : 't* [-]',
	'yLabel': 'Str [-]',
	'legend' : ['Re=210', 'Re=335', 'Re=625', 'Re=1000', 'Re=1270']
	}

#calcStratification(cStratVel)

StTemp = {
	'trace': 'caseTemp',
	'caseTemp': ['318', '323', '328', '333', '338'],
	'caseVel': '0.6',
	'caseTime': ['d5', 'd10','d15', 'd20', 'd25', 'd30'],
	'xLabel' : 't* [-]',
	'yLabel': 'Str [-]',
	'legend' : ['Gr=3.1E10', 'Gr=3.7E10', 'Gr=4.2E10', 'Gr=4.7E10', 'Gr=5.2E10']
	}


#calcStratification(cStratTemp)

#------------------------------------------------------------------------------




#------------------------------------------------------------------------------
def compare(compareFor, case, path, path2 ):
	cf = compareFor
	cas = case
	
#	path= 'engelli-lineSample.csv'
#	path2= 'engelsiz-lineSample.csv'
	
#	path= 'engelsiz-volAve.csv'
#	path2= 'engelsiz-lineSample.csv'
#	
	pp = cf(path, cas)
	pp2 = cf(path2,cas)
#	print(pp[0])
#	print(pp[1])
	print ('__________________________________')
	print ('_______', path, '_______')
	for k in range(len(pp[0])):
		print('##------------', k)
		for t in range(len(pp[0][0])):
			print(pp[1][k][t])	
	
	print ('_______', path2, '_______')
	for k in range(len(pp2[0])):
		print('##------------', k)
		for t in range(len(pp2[0][0])):
			print(pp2[1][k][t])	
	
	plt.figure()
	plt.plot([], [],  color='black', label=cas['compareCase1'])
	plt.plot([], [], dashes=[2, 2],  color='black', label=cas['compareCase2'])
	
	
	for i in range(len(pp[0])):
		color = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6']
		marker = ['.', '1', '+', '2', '3', '4', '1', '2', '3', 'v', '^', 'h', 'd']
		x1 = pp[0][i]
		y1 = pp[1][i]
		
		x2 = pp2[0][i]
		y2 = pp2[1][i]
		
		xSpline1 = makeSpline(x1, y1)[0]
		ySpline1 = makeSpline(x1, y1)[1]
		
		xSpline2 = makeSpline(x2, y2)[0]
		ySpline2 = makeSpline(x2, y2)[1]
		
		plt.plot(xSpline1, ySpline1, color=color[i], marker=marker[i], markevery=40)
		plt.plot(xSpline2, ySpline2, dashes=[2, 2], color=color[i], marker=marker[i], markevery=40)

		plt.scatter([], [], marker=marker[i], label=pp[4][i])		
		
#		plt.plot(pp[0][i], pp[1][i],  color=color[i], label = pp[4][i] + ' Engelli' )		
#		plt.plot(pp2[0][i], pp2[1][i], dashes=[8, 2],color=color[i], label = pp[4][i] + ' Engelsiz')
		
#		plt.legend( loc=9, bbox_to_anchor=(1.25, 1))
		plt.legend(loc=0)
#		plt.legend(loc='lower left')
		plt.xlabel(pp[2])
		plt.ylabel(pp[3])
		plt.tight_layout()
#		plt.ylim(-0.05, 1.05)
		sName = cas['xLabel'].split('*')[0] + '-' + cas['yLabel'].split('*')[0]
#		sName = 't-StrEff-0.6'
		
	if (cas['savePlot'] == 'True'):
		plt.savefig('.\savedPlots\\' + cas['trace'] + '-' + sName+'.png', format='png', dpi=cas['saveDpi'])



#path1= './data/engelli-volAve.csv'
#path2= './data/engelsiz-volAve.csv'

#print(rho(18+273))

#compare(plot, ZTRe, path1, path2)
#compare(plot, tToutRe)
#compare(St, StTemp)
#compare(Ri, RiVel)
#compare(Mix, MixTemp)
#compare(disEff, disEffVel)
#
#meshInd()


# -----------------------------------------------------------------------------

#plotAll()

#------------------------------------------------------------------------------


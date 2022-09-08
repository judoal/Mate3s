#!/Users/allengordon/opt/miniconda3/bin/python3
#import numpy as np
#import matplotlib.pyplot as plt
import math
import http.client
import time
import json
from datetime import datetime
import sys
import os
import numpy as np
import math
import matplotlib.pyplot as plt


"""  
Sample output from MATE3S (dataJobj): 
http://192.168.1.7/Dev_status.cgi?&Port=0

{'devstatus': {'Gateway_Type': 'Mate3s', 'Sys_Time': 1600598366, 'Sys_Batt_V': 54.0, 'ports': [{'Port': 1, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 10, 'Chg_I': 0, 'Buy_I': 0, 'Sell_I': 4, 'VAC_in': 127, 'VAC_out': 126, 'Batt_V': 54.0, 'AC_mode': 'AC USE', 'INV_mode': 'Sell', 'Warn': ['Fan Failure'], 'Error': ['none'], 'AUX': 'enabled'}, {'Port': 2, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 0, 'Chg_I': 0, 'Buy_I': 5, 'Sell_I': 0, 'VAC_in': 121, 'VAC_out': 125, 'Batt_V': 53.6, 'AC_mode': 'AC USE', 'INV_mode': 'Comm Error', 'Warn': ['Fan Failure'], 'Error': ['Over Temp'], 'AUX': 'enabled'}, {'Port': 3, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 10, 'Chg_I': 0, 'Buy_I': 0, 'Sell_I': 10, 'VAC_in': 124, 'VAC_out': 126, 'Batt_V': 53.6, 'AC_mode': 'AC USE', 'INV_mode': 'Sell', 'Warn': ['none'], 'Error': ['none'], 'AUX': 'enabled'}, {'Port': 4, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 20.0, 'In_I': 16, 'Batt_V': 53.4, 'In_V': 70.0, 'Out_kWh': 3.8, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 5, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 15.0, 'In_I': 13, 'Batt_V': 53.2, 'In_V': 66.6, 'Out_kWh': 3.5, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 6, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 9.0, 'In_I': 6, 'Batt_V': 53.1, 'In_V': 91.6, 'Out_kWh': 4.0, 'CC_mode': ' ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 7, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 17.0, 'In_I': 15, 'Batt_V': 53.3, 'In_V': 64.4, 'Out_kWh': 4.6, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}]}}
"""
#Inverter inits
invCurrent=['1','1','1','1','1','1','1','1','1','1']
invChgCurrent=['1','1','1','1','1','1','1','1','1','1']
invBuyCurrent=['1','1','1','1','1','1','1','1','1','1']
invSellCurrent=['1','1','1','1','1','1','1','1','1','1']
invVACIn=['1','1','1','1','1','1','1','1','1','1']
invVACOut=['1','1','1','1','1','1','1','1','1','1']
invBattV=['1','1','1','1','1','1','1','1','1','1']
invACMode=['1','1','1','1','1','1','1','1','1','1']
invMode=['1','1','1','1','1','1','1','1','1','1']
invWarn=['1','1','1','1','1','1','1','1','1','1']
invErr=['1','1','1','1','1','1','1','1','1','1']
invAux=['1','1','1','1','1','1','1','1','1','1']

#Charge controller inits
ccOutCurrent=['1','1','1','1','1','1','1','1','1','1']
ccInCurrent=['1','1','1','1','1','1','1','1','1','1']
ccBattV=['1','1','1','1','1','1','1','1','1','1']
ccInV=['1','1','1','1','1','1','1','1','1',","]
ccKWH=['1','1','1','1','1','1','1','1','1','1']
ccMode=['1','1','1','1','1','1','1','1','1','1']
ccError=['1','1','1','1','1','1','1','1','1','1']
ccAuxMode=['1','1','1','1','1','1','1','1','1','1']
ccAux=['1','1','1','1','1','1','1','1','1','1']
ccCount=0
ofile=""
hourPrev=""
webPath=""
hourNow=""
conn=""
n=0

os.chdir("/Users/allengordon/Documents/workspace/pgsolar/pvlogs")
#os.chdir("/Users/allengordon/Documents/workspace/pgsolar/pvlogs")


plt.style.use('ggplot')
size = 10000
x_vec = np.linspace(1, 0, size)[0:size - 1]


a = np.empty([size-1])
print(a)
for i in range(size-1):
	a[i] = "0.0"

y_vec = a  #np.random.randn(len(x_vec))
#print (y_vec)
line1 = []
t0 = time.time()


def live_plotter(x_vec, y1_data, line1, identifier='', pause_time=0.1):
	if line1 == []:
# this is the call to matplotlib that allows dynamic plotting
		plt.ion()
		fig = plt.figure(figsize=(13, 6))
		ax = fig.add_subplot(111)
		# create a variable for the line so we can later update itr
		line1, = ax.plot(x_vec, y1_data, '-o', alpha=0.2)
		# update plot label/title
		plt.ylabel('Y Label')
		plt.title('Title: {}'.format(identifier))
		plt.show()

# after the figure, axis, and line are created, we only need to update the y-data
	line1.set_ydata(y1_data)
	# adjust limits if new data goes beyond bounds
	if np.min(y1_data) <= line1.axes.get_ylim()[0] or np.max(y1_data) >= line1.axes.get_ylim()[1]:
		plt.ylim([np.min(y1_data) - np.std(y1_data), np.max(y1_data) + np.std(y1_data)])
	# this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
	plt.pause(pause_time)
# return line so we can update it again in the next iteration
	return line1


inited = False
# the function below is for updating both x and y values (great for updating dates on the x-axis)
def live_plotter_xy(x_vec, y1_data, line1, identifier='', pause_time=0.01):
	if line1 == []:
		plt.ion()
		fig = plt.figure(figsize=(13, 3))
		ax = fig.add_subplot(111)
		line1, = ax.plot(x_vec, y1_data, 'b.', alpha=0.2)
		plt.ylabel('Y Label')
		plt.title('Title: {}'.format(identifier))
		plt.show()

	line1.set_data(x_vec, y1_data)
	plt.xlim(np.max(x_vec), np.min(x_vec))
	if np.min(y1_data) <= line1.axes.get_ylim()[0] or np.max(y1_data) >= line1.axes.get_ylim()[1]:
		plt.ylim([np.min(y1_data) - np.std(y1_data), np.max(y1_data) + np.std(y1_data)])

	plt.pause(pause_time)

	return line1


while 1:
	try:
		conn = http.client.HTTPConnection("192.168.1.7", timeout=300)
		conn.request("GET", "/Dev_status.cgi?&Port=0")
		r1 = conn.getresponse()
		data1 = r1.read()
		dataDecoded=data1.decode()
		dataJobj=json.loads(dataDecoded)
#		print(dataJobj)
#		print(dataJobj['devstatus']['Sys_Time'])
	except:
		print("\n" + "Exception", sys.exc_info()[0], "occurred", flush=True)
#		continue

	print (int(time.time()))

#	print (dataJobj['devstatus']['Sys_Time'])
	now = datetime.now()
	hourNow=now.today().hour
	minNow=now.today().minute
	secNow=now.today().second
	format="%Y_%m_%d"
	date1=now.strftime(format)
	dateTimeStr=str(hourNow) + "_" + str(minNow) + "_" + str(secNow)
	print (date1 + "\t" + dateTimeStr, flush=True)

	#write to files

	pathname = date1 + "_PV.log"
	ofile=open(pathname, "a+", 10)
	#webpath = "/Users/allengordon/tdmp"
	#wfile = open("/Users/allengordon/tmp/PV.log", "a+", 10)
	dataList = list(dataJobj['devstatus']['ports'])  #List
	for i in range (len(dataList)):
		dataList = list(dataJobj['devstatus']['ports'])  #List
		portnum = dataList[i]['Port']

		if dataList[i]['Dev'] == 'FX':
			invCurrent[i]=(str(float(dataList[i]['Inv_I'])))
			invChgCurrent[i]=(str(dataList[i]['Chg_I']))
			invBuyCurrent[i]=(str(dataList[i]['Buy_I']))
			invSellCurrent[i]=(str(dataList[i]['Sell_I']))
			invVACIn[i]=(str(dataList[i]['VAC_in']))
			invVACOut[i]=(str(dataList[i]['VAC_out']))
			invBattV[i]=(str(dataList[i]['Batt_V']))
			invACMode[i]=(str(dataList[i]['AC_mode']))
			invMode[i]=(str(dataList[i]['INV_mode']))
			invWarn[i]=(str(dataList[i]['Warn']))
			invErr[i]=(str(dataList[i]['Error']))
			invAux[i]=(str(dataList[i]['AUX']))
			
			if i == 0:
					ofile.write(date1 + ":" + dateTimeStr)
					#wfile.write(dateTimeStr)
					InvHeaderStr="INV\t" + "I\t" + "IChg\t" + "Ibuy\t" + "Isel\t" + "Vacin\t" + "VacOut\t" +  \
								 "Vbatt\t" + "ACmode\t" + "WARN\t\t" + "ERR\t\t" + "Aux"
					print (InvHeaderStr, flush=True)
					ccCount = 0

					invFileHeaderStr = InvHeaderStr
					ofile.write("\n"+ InvHeaderStr + "\n")
					#wfile.write("\n"+ InvHeaderStr + "\n")

			invStr = str(i) + "\t" + str(invCurrent[i]) + "\t" + str(invChgCurrent[i]) + "\t" + \
					 str(invBuyCurrent[i]) + "\t" + str(invSellCurrent[i]) \
					 + "\t" + str(invVACIn[i]) + "\t" + str(invVACOut[i]) + "\t" + str(invBattV[i]) + "\t" + \
					 str(invMode[i]) + "\t" + str(invWarn[i]) + "\t" + str(invErr[i]) + "\t" + str(invAux[i])

			print(invStr, flush=True)
			invFileStr=invStr
			ofile.write (invFileStr + "\n")

		if dataList[i]['Dev'] == 'CC':
			ccOutCurrent[i]=(str(dataList[i]['Out_I']))
			ccInCurrent[i]=(str(dataList[i]['In_I']))
			ccBattV[i]=(str(dataList[i]['Batt_V']))
			ccInV[i]=(str(dataList[i]['In_V']))
			ccKWH[i]=(str(dataList[i]['Out_kWh']))
			ccMode[i]=(str(dataList[i]['CC_mode']))
			ccError[i]=(str(dataList[i]['Error']))
			ccAuxMode[i]=(str(dataList[i]['Aux_mode']))
			ccAux[i]=(str(dataList[i]['AUX']))

			if ccCount == 0:
					ccHeaderStr ="\n" + "CC\t" + "Iout\t" + "Iin\t" + "Vb\t" + "Vin\t" + "KWH\t" + \
								 "Mode\t" + "Err\t\t" + str("AuxMode\t") + "Aux"
					print (ccHeaderStr, flush=True)
					ccCount=-1

					ccFileHeaderStr = ccHeaderStr
					ofile.write("\n" + ccHeaderStr + "\n")

			ccStr = str(i) + "\t" + str(ccOutCurrent[i]) + "\t" + str(ccInCurrent[i]) + "\t" + \
					str(ccBattV[i]) + "\t" + str(ccInV[i]) + "\t" + str(ccKWH[i]) + "\t" + ccMode[i] + \
					"\t" + str(ccError[i]) + "\t" + ccAuxMode[i] + "\t" + ccAux[i]
			print(ccStr)
			ccFileStr = ccStr
			ofile.write(ccFileStr + "\n")
			#wfile.write(ccFileStr + "\n")
			ofile.flush()
			#wfile.flush()åC



#	val1 = int(invBuyCurrent[0]) + int(invBuyCurrent[1])
	t = time.time() - t0
	val1 = int(invSellCurrent[0]) + int(invSellCurrent[1]) + int(invSellCurrent[2])
	print(t)
	y_vec[-1] = val1
	line1 = live_plotter_xy(x_vec, y_vec, line1)
	y_vec = np.append(y_vec[1:], 0.0)

	time.sleep(.9)
	print("\n", flush=True)
	dataList.clear()
	ofile.close()

#	time.sleep(0.9)
	conn.close()

#!/usr/local/bin/python
import http.client
import time
import json
from datetime import datetime



""" Sample output from MATE3S (dataJobj): 
http://192.168.1.7/Dev_status.cgi?&Port=0

{'devstatus': {'Gateway_Type': 'Mate3s', 'Sys_Time': 1600598366, 'Sys_Batt_V': 54.0, 'ports': [{'Port': 1, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 10, 'Chg_I': 0, 'Buy_I': 0, 'Sell_I': 4, 'VAC_in': 127, 'VAC_out': 126, 'Batt_V': 54.0, 'AC_mode': 'AC USE', 'INV_mode': 'Sell', 'Warn': ['Fan Failure'], 'Error': ['none'], 'AUX': 'enabled'}, {'Port': 2, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 0, 'Chg_I': 0, 'Buy_I': 5, 'Sell_I': 0, 'VAC_in': 121, 'VAC_out': 125, 'Batt_V': 53.6, 'AC_mode': 'AC USE', 'INV_mode': 'Comm Error', 'Warn': ['Fan Failure'], 'Error': ['Over Temp'], 'AUX': 'enabled'}, {'Port': 3, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 10, 'Chg_I': 0, 'Buy_I': 0, 'Sell_I': 10, 'VAC_in': 124, 'VAC_out': 126, 'Batt_V': 53.6, 'AC_mode': 'AC USE', 'INV_mode': 'Sell', 'Warn': ['none'], 'Error': ['none'], 'AUX': 'enabled'}, {'Port': 4, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 20.0, 'In_I': 16, 'Batt_V': 53.4, 'In_V': 70.0, 'Out_kWh': 3.8, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 5, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 15.0, 'In_I': 13, 'Batt_V': 53.2, 'In_V': 66.6, 'Out_kWh': 3.5, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 6, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 9.0, 'In_I': 6, 'Batt_V': 53.1, 'In_V': 91.6, 'Out_kWh': 4.0, 'CC_mode': ' ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 7, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 17.0, 'In_I': 15, 'Batt_V': 53.3, 'In_V': 64.4, 'Out_kWh': 4.6, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}]}}
"""

#Inverter inits
invCurrent=[]
invChgCurrent=[]
invBuyCurrent=[]
invSellCurrent=[]
invVACIn=[]
invVACOut=[]
invBattV=[]
invACMode=[]
invMode=[]
invWarn=[]
invErr=[]
invAux=[]

#Charge controller inits
ccOutCurrent=[]
ccInCurrent=[]
ccBattV=[]
ccInV=[]
ccKWH=[]
ccMode=[]
ccMode=[]
ccError=[]
ccAuxMode=[]
ccAux=[]

while (1):
	conn = http.client.HTTPConnection("192.168.1.7")
	conn.request("GET", "/Dev_status.cgi?&Port=0")

	r1 = conn.getresponse()
	
	data1 = r1.read()  # This will return entire content.
	
	dataDecoded=data1.decode()
	dataJobj=json.loads(dataDecoded)
	
	print (dataJobj['devstatus']['Sys_Time'])
	print(str(datetime.now()))
	dataList = list(dataJobj['devstatus']['ports'])  #List
	for i in range (len(dataList)):
		dataList = list(dataJobj['devstatus']['ports'])  #List
#		print (dataList[i])
#		print ("index: " + str(i))
		portnum = dataList[i]['Port']
#		print ("PORTNUM: " + str(portnum))

		if dataList[i]['Dev'] == 'FX':
			invCurrent.append (str(dataList[i]['Inv_I']))
			invChgCurrent.append(str(dataList[i]['Chg_I']))
			invBuyCurrent.append(str(dataList[i]['Buy_I']))
			invSellCurrent.append(str(dataList[i]['Sell_I']))
			invVACIn.append(str(dataList[i]['VAC_in']))
			invVACOut.append(str(dataList[i]['VAC_out']))
			invBattV.append(str(dataList[i]['Batt_V']))
			invACMode.append(str(dataList[i]['AC_mode']))
			invMode.append(str(dataList[i]['INV_mode']))
			invWarn.append(str(dataList[i]['Warn']))
			invErr.append(str(dataList[i]['Error']))
			invAux.append(str(dataList[i]['AUX']))
			ccOutCurrent.append('')   #padding
			ccInCurrent.append('')   #padding]
			ccBattV.append('')   #padding
			ccInV.append('')   #padding
			ccKWH.append('')   #padding
			ccMode.append('')   #padding
			ccError.append('')   #padding
			ccAuxMode.append('')   #padding
			ccAux.append('')   #padding]

			print ("INV #" +  str(i) + " CURRENT: " + invCurrent[i]+ " AMPS")
			print ("INV #" + str (i) + " CHARGER: "  + invChgCurrent[i] + " AMPS")
			print ("INV #" + str (i) + " BUY: "  + invBuyCurrent[i] + " AMPS")			
			print ("INV #" + str (i) + " SELL: "  + invSellCurrent[i] + " AMPS")
			print ("INV #" + str (i) + " VAC IN: "  + invVACIn[i] + " VOLTS")
			print ("INV #" + str (i) + " VAC OUT: "  + invVACOut[i] + " VOLTS")
			print ("INV #" + str (i) + " BATT VOLT: "  + invBattV[i] + " VOLTS")			
			print ("INV #" + str (i) + " AC MODE: "  + invACMode[i])
			print ("INV #" + str (i) + " INV MODE: " + invMode[i])
			print ("INV #" + str (i) + " INV WARN: "  + invWarn[i])
			print ("INV #" + str (i) + " INV ERROR: " + invErr[i])		
			print ("INV #" + str (i) + " INV AUX: "  + invAux[i])
			print ("\n")

		if dataList[i]['Dev'] == 'CC':
			ccOutCurrent.append(str(dataList[i]['Out_I']))
			ccInCurrent.append(str(dataList[i]['In_I']))
			ccBattV.append(str(dataList[i]['Batt_V']))
			ccInV.append(str(dataList[i]['In_V']))
			ccKWH.append(str(dataList[i]['Out_kWh']))
			ccMode.append(str(dataList[i]['CC_mode']))
			ccError.append(str(dataList[i]['Error']))
			ccAuxMode.append(str(dataList[i]['Aux_mode']))
			ccAux.append(str(dataList[i]['AUX']))
		
			print ("CC #" + str(i)  + " CC OUTPUT CURRENT: " + ccOutCurrent[i] + " AMPS") 
			print ("CC #" + str(i)  + " CC INPUT CURRENT: " + ccInCurrent[i] + " AMPS")
			print ("CC #" + str(i)  + " CC BATT VOLT: " + ccBattV[i]  + " VOLTS")
			print ("CC #" + str(i)  + " CC INPUT VOLT: " + ccInV[i] + " VOLTS")
			print ("CC #" + str(i)  + " CC KWH: " +  ccKWH[i] + " kWh")
			print ("CC #" + str(i)  + " CC MODE: " + ccMode[i])
			print ("CC #" + str(i)  + " CC ERROR: " + ccError[i])
			print ("CC #" + str(i)  + " CC AUX Mode: " + ccAuxMode[i])
			print ("CC #" + str(i)  + " CC AUX: " + ccAux[i])
			
			print("\n")

	time.sleep(1)
	conn.close()

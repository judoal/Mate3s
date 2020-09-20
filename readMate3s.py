#!/usr/local/bin/python
import http.client
import time
import json
from datetime import datetime



""" Sample output from MATE3S (dataJobj)
{'devstatus': {'Gateway_Type': 'Mate3s', 'Sys_Time': 1600598366, 'Sys_Batt_V': 54.0, 'ports': [{'Port': 1, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 10, 'Chg_I': 0, 'Buy_I': 0, 'Sell_I': 4, 'VAC_in': 127, 'VAC_out': 126, 'Batt_V': 54.0, 'AC_mode': 'AC USE', 'INV_mode': 'Sell', 'Warn': ['Fan Failure'], 'Error': ['none'], 'AUX': 'enabled'}, {'Port': 2, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 0, 'Chg_I': 0, 'Buy_I': 5, 'Sell_I': 0, 'VAC_in': 121, 'VAC_out': 125, 'Batt_V': 53.6, 'AC_mode': 'AC USE', 'INV_mode': 'Comm Error', 'Warn': ['Fan Failure'], 'Error': ['Over Temp'], 'AUX': 'enabled'}, {'Port': 3, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 10, 'Chg_I': 0, 'Buy_I': 0, 'Sell_I': 10, 'VAC_in': 124, 'VAC_out': 126, 'Batt_V': 53.6, 'AC_mode': 'AC USE', 'INV_mode': 'Sell', 'Warn': ['none'], 'Error': ['none'], 'AUX': 'enabled'}, {'Port': 4, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 20.0, 'In_I': 16, 'Batt_V': 53.4, 'In_V': 70.0, 'Out_kWh': 3.8, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 5, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 15.0, 'In_I': 13, 'Batt_V': 53.2, 'In_V': 66.6, 'Out_kWh': 3.5, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 6, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 9.0, 'In_I': 6, 'Batt_V': 53.1, 'In_V': 91.6, 'Out_kWh': 4.0, 'CC_mode': ' ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 7, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 17.0, 'In_I': 15, 'Batt_V': 53.3, 'In_V': 64.4, 'Out_kWh': 4.6, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}]}}
"""


while (1):
	conn = http.client.HTTPConnection("192.168.1.7")
	conn.request("GET", "/Dev_status.cgi?&Port=0")

	r1 = conn.getresponse()
	
	data1 = r1.read()  # This will return entire content.
	
	dataDecoded=data1.decode()
	dataJobj=json.loads(dataDecoded)
#	print (dataJobj)   #dictionary
#	print ("\n")	
	
	print (dataJobj['devstatus']['Sys_Time'])
	print(str(datetime.now()))
	dataList = list(dataJobj['devstatus']['ports'])  #List
	for i in range (len(dataList)):
		dataList = list(dataJobj['devstatus']['ports'])  #List
		print (dataList[i])		
		if dataList[i]['Dev'] == 'FX':
			print  ("INV CURRENT (amps)" + str(i) + ": " + str(dataList[i]['Inv_I']))
		#		print (dataList[i]['Port'])		#Dictionary
		print ("\n")
	
	conn.close()
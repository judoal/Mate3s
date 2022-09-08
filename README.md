After replacing my old Outback Power Mate2 with the Mate3s, I needed a new way of monitoring the output other than via the Outback OpticsRE web app.  I had been using Wattplot but for a variety of reasons, including my inability to configure it to read the MATE3s data, I decided I needed something new.  After looking on Github and elsewhere and not finding any existing code to my satisfaction, I decided to write my own.  The key was finding hidden cgi code  that extracts the data as a json object.  This output looks like this using a web browser:
            
            http://192.168.1.7/Dev_status.cgi?&Port=0
            
            {'devstatus': {'Gateway_Type': 'Mate3s', 'Sys_Time': 1600598366, 'Sys_Batt_V': 54.0, 'ports': [{'Port': 1, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 10, 'Chg_I': 0, 'Buy_I': 0, 'Sell_I': 4, 'VAC_in': 127, 'VAC_out': 126, 'Batt_V': 54.0, 'AC_mode': 'AC USE', 'INV_mode': 'Sell', 'Warn': ['Fan Failure'], 'Error': ['none'], 'AUX': 'enabled'}, {'Port': 2, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 0, 'Chg_I': 0, 'Buy_I': 5, 'Sell_I': 0, 'VAC_in': 121, 'VAC_out': 125, 'Batt_V': 53.6, 'AC_mode': 'AC USE', 'INV_mode': 'Comm Error', 'Warn': ['Fan Failure'], 'Error': ['Over Temp'], 'AUX': 'enabled'}, {'Port': 3, 'Dev': 'FX', 'Type': '120V', 'Inv_I': 10, 'Chg_I': 0, 'Buy_I': 0, 'Sell_I': 10, 'VAC_in': 124, 'VAC_out': 126, 'Batt_V': 53.6, 'AC_mode': 'AC USE', 'INV_mode': 'Sell', 'Warn': ['none'], 'Error': ['none'], 'AUX': 'enabled'}, {'Port': 4, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 20.0, 'In_I': 16, 'Batt_V': 53.4, 'In_V': 70.0, 'Out_kWh': 3.8, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 5, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 15.0, 'In_I': 13, 'Batt_V': 53.2, 'In_V': 66.6, 'Out_kWh': 3.5, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 6, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 9.0, 'In_I': 6, 'Batt_V': 53.1, 'In_V': 91.6, 'Out_kWh': 4.0, 'CC_mode': ' ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}, {'Port': 7, 'Dev': 'CC', 'Type': 'MX60', 'Out_I': 17.0, 'In_I': 15, 'Batt_V': 53.3, 'In_V': 64.4, 'Out_kWh': 4.6, 'CC_mode': '  ', 'Error': ['none'], 'Aux_mode': 'Disabled', 'AUX': 'disabled'}]}}
            
The first thing that was observed was the browser did not refresh the data requiring the web page to be reimplemented each time.  HOwever I found that by writing the code to keep the session to the MATE3s server, was sufficient to have the data refreshed.
          
          
The initial commit shows the initial code for developing an extraction program.  It is not complete, but is the POC for this project.  Graphing the data is a different animal, since I have not been very good at developing graphics routines in python.  I would like to create a stripchart recorder to display the periodic data, where current time is on the right axis.  However, I have experience with the opensource java charting program, JFreeChart, an amd thinking of piping the data to a java app for graphing.

This update modifies and incorporates a matplotlib script that did not have any licensing limitations. It is a work in progress since the plotting portion is not working yet.

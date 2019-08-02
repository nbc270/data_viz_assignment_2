# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os 
import sys
import numpy as np
import pandas as pd
import pylab as pl
import json
try: 
    import urllib2 as urllib
except ImportError: 
    import urllib.request as urllib  
    
key = str(sys.argv[1])
bus_line = str(sys.argv[2])
csv_filename = str(sys.argv[3])
    
print("Bus Line : " + bus_line)

url1 = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
url2 = "&VehicleMonitoringDetailLevel=calls&LineRef="

full_url = url1 + key + url2 + bus_line

response = urllib.urlopen(full_url)
data = response.read().decode('utf-8')
data = json.loads(data)
Bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print("Number of Active Buses: " + str(len(Bus_data)))


write_data = pd.DataFrame()
Bus_Info = 0
for i in Bus_data:
    empty_list = []
    print("Bus " + str(Bus_Info) + " is at lattitude " +  str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) + " and longitude " +  str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    empty_list.append(Bus_Info)
    empty_list.append(str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']))
    empty_list.append(str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    new_data = pd.DataFrame(data=[empty_list])
    write_data = pd.concat([write_data,new_data], axis =0)
    Bus_Info += 1

#Organize the dataframe with column titles and the index reset
write_data.columns = ['Bus Number','Latitude','Longitude']
write_data.reset_index()

#Write the dataframe to a csv
write_data.to_csv(csv_filename)

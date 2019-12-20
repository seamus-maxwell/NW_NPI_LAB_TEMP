###
# Program: plot_temp_data 
# Author:  Seamus Maxwell
# Date: 
# Description: This program is used in the weekly lab temperature and humidity collection. The four sensors in the Demo and Engineering lab export data to a csv file. 
# This program extracts the data, writes it to an excel sheet, and plots the data (temp and humidity vs time)
# The user must put the csv files in the Temperature Data directory (\\nofs1\hwtools\RF_DATA\RF32\Weekly_DCV\NW_LAB_TEMPERATURE_DATA) 
###
import matplotlib.pyplot as plt
import xlrd
import xlsxwriter
import datetime 
from zipfile import ZipFile
import csv


sensors = ['Demo Sensor 1', 'Demo Sensor 2', 'Engineering Sensor 1', 'Engineering Sensor 2']
file_name = ['DL1', 'DL2', 'EL1', 'EL2']

#record date to use in filenaming convention
date = datetime.date.today()
print(date)
loop through the four sensors to extract all zipped files
for sens in sensors:
    zipped_file = sens + '.zip'  
    with ZipFile(zipped_file, 'r') as zip:
        zip.printdir()
        
        print("Extracting Files:")
        zip.extractall()
        print('Done Extracting')

print('Pause:')
input()
#loop through the four sensors to extract the data, write it to an xlsx file and plot the data
for i in range(0, 3):
    csv_filename = sensors[i] + '.csv'
    xlsx_filename = str(date) + "_" + file_name[i] + '.xlsx'

    #read in data from the .csv file
    with open(csv_filename, newline='') as csvfile:
        sensor_data = csv.reader(csvfile, delimiter=',')
        for row in sensor_data:
            print(','.join(row))
        print("Data Read:")
        input()
        csvfile.close()

    # write to .xlsx file
    workbook = xlswriter.Workbook(xlsx_filename)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, sensor_data)











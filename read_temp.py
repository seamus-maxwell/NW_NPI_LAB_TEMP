import xml.etree.ElementTree as ET
import requests
# from openpyxl import Workbook 
import openpyxl
import datetime

def find_data(root, data_type):
    tempf = []
    humid = []
    for devices in root:
        for device in devices:
            for sensors in device:
                for sensor in sensors:
                    tempf.append(sensor.get('tempf'))
                    humid.append(sensor.get('humid'))
    if data_type == True:
        return(tempf[0:3])
        print(tempf[0:3])
    else:
        return(humid)[1:3]
        print(humid[1:3])
                    
                    
#url's of npi tempager and my tempager get data
npi_url = 'http://159.75.38.31:8080/api/getData/?type=0&mac=00-80-A3-B9-B4-22&__lzbc__=1565096350905'
my_url = 'http://159.75.38.31:8080/api/getData/?type=0&mac=00-20-4A-BD-64-5C&__lzbc__=1565096350905'

#make request to get data websites

try:
    npi_tempager_resp = requests.get(npi_url)
    my_tempager_resp = requests.get(my_url)
except:
    print("Request Failed")

#convert request to string
npi_xml = npi_tempager_resp.text
my_xml = my_tempager_resp.text

#get tree of xml 
npi_root = ET.fromstring(npi_xml)
my_root = ET.fromstring(my_xml)

#get temp and humid data of NPI tempager
npi_tempf = find_data(npi_root, True)


npi_humid = find_data(npi_root, False)


#get temp and humid data of MY tempager
my_tempf = find_data(my_root, True)


my_humid = find_data(my_root, False)


#get all other data
date = datetime.datetime.now().date()
time = datetime.datetime.now().time()


#Average Function: returns the average of the list, either temp or humid
def Avg(str_list):
    float_list = []
    for i in str_list:
        float_list.append(float(i))
    list_sum = sum(float_list)
    list_len = len(float_list)
    avg = list_sum / list_len
    return(avg)

#Find averages of npi temp and humid
npi_temp_avg = Avg(npi_tempf)
npi_humid_avg = Avg(npi_humid)

#Find averages of my temp and humid
my_temp_avg = Avg(my_tempf)
my_humid_avg = Avg(my_humid)

#Format data to append to file
data = [date, time, npi_temp_avg, npi_humid_avg, npi_tempf[0], npi_tempf[1], npi_tempf[2], npi_humid[0], npi_humid[1], None, my_temp_avg, my_humid_avg, my_tempf[0], my_tempf[1], my_tempf[2], my_humid[0], my_humid[1]]

try:
    #write data to workbook
    npi_book = openpyxl.load_workbook('NPI Temp.xlsx')
    npi_sheet = npi_book.active
    npi_sheet.append(data)
    npi_book.save('NPI Temp.xlsx')
    print(data)
    print("Data Recorded: Press any button to continue")
    input()

except:
    print("ERROR: Data not written to file")
    input()
import urllib.request
import requests
import urllib.parse
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

i=1
number = 0
page=1

#creating dictionary
dictionary = {}
dictionary["number"] = []
dictionary["name"] = []
dictionary["brand"] = []
dictionary["price"] = []
dictionary["numberofsim"] = []
dictionary["diagonal"] = []
dictionary["width"] = []
dictionary["length"] = []
dictionary["screentechnology"] = []
dictionary["os"] = []
dictionary["numberofcore"] = []
dictionary["memoryGB"] = []
dictionary["sensortype"] = []



while page<=16:
    my_url = 'https://alser.kz/c/vse-smartfony/page-'+str(page)
    response = requests.get(my_url)
    page_soup = soup(response.text, "html.parser")

    tainers = page_soup.find("div", {"class":"col-md-9"}) #finding the main class
    containers = tainers.findAll("div", {"class":"col-md-3"}) 
    
    page +=1
    


    for container in containers: #this FOR is for each smartphones
#-------------------------------------------------------------------------------------------
    	items = container.findAll("div", {"class":"product-item"})  

    	for item in items: #this FOR is for getting name and price from special type of class 

            names = item.findAll("a", {"product-item__info_title"})[0].text.strip()
            if 'Смартфон' in names:
            	name = names[9:] #getting name without the word 'Смартфон'
            else:
            	name = names 
            
            brand = name.split()[0]
            
    	    #prices
            prices = container.findAll("div", {"price"})[0].text.strip()
            prices = re.findall("\d+\.\d+|\d+", prices) #getting only numbers from string
            if len(prices)>1:
            	price = int(prices[0]+prices[1])
            else:
            	price = int(prices[0])
            

#-------------------------------------------------------------------------------------------
    	details = container.findAll("div", {"product-card-details"}) 

    	for detail in details: #this FOR is for getiing details thats class is different from the first one
        	rows = detail.findAll("div", {"row product-card-spec"})
        	for row in rows:
        		row = row.text.strip()
        		if 'Количество SIM-карт' in row:
        			row = re.findall("\d+\.\d+|\d+", row)[0] #getting only numbers
        			sim = int(row)

        		elif 'Диагональ' in row:
        			row = re.findall("\d+\.\d+|\d+", row)[0] #getting only intagers or floats from string
        			dgnl = float(row)

        		elif 'Разрешение экрана' in row:
        			row = re.findall("\d+", row)
        			wid = int(row[0])
        			leng = int(row[1])
        			
        		elif 'Технология изготовления экрана' in row:
        			scrtech = row[33:] #getting the word without 'Технология изготовления экрана'

        		elif 'Операционная система' in row:
        			os = row[23:]

        		elif 'Количество ядер' in row:
        			row = re.findall("\d+\.\d+|\d+", row)[0]
        			core = row

        		elif 'Объем встроенной памяти' in row:
        			row = re.findall("\d+\.\d+|\d+", row)[0]
        			memory = row

        		elif 'Датчики' in row:
        			sensor = row[10:]

        		else:
        			continue





        	#appending all parsed values to dictionary
        	number+=1
        	dictionary["number"].append(i)
        	dictionary["name"].append(name)
        	dictionary["brand"].append(brand)
        	dictionary["price"].append(price)
        	dictionary["numberofsim"].append(sim)
        	dictionary["diagonal"].append(dgnl)
        	dictionary["width"].append(wid)
        	dictionary["length"].append(leng)
        	dictionary["screentechnology"].append(scrtech)
        	dictionary["os"].append(os)
        	dictionary["numberofcore"].append(core)
        	dictionary["memoryGB"].append(memory)
        	dictionary["sensortype"].append(sensor)

        	print(str(number) + '. name:' + str(name) + ',  brand:' + str(brand) + ',  price:' + str(price) + ',  sim:' + str(sim) + ", dgnl: " + str(dgnl) + 
        		", width: " + str(wid) +", length: " + str(leng) + ", scrtech: " + scrtech + ", os: " + os + ", core: " + core + ", memory: " + memory + ", sensor: " + sensor)

        	i +=1
        	if i == 1000: 
        		break  



        	

        	





        
    	
#converting the dictionary to CSV file
    
import pandas as pd
df = pd.DataFrame(dictionary,columns =['number','name','brand','price', 'numberofsim','diagonal','width','length','screentechnology','os',
	'numberofcore','memoryGB','sensortype'])
df.to_csv('alser.csv',index=False,encoding = 'utf-8-sig', sep = ';')
print('')

print(df)


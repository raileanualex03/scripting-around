
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os


URL = 'https://www.emag.ro/laptopuri/resigilate/filter/tip-laptop-f7882,ultraportabil-v-4670916/tip-placa-video-f7895,dedicata-v-2754/c?ref=lst_leftbar_7895_-2754'


# opening the connection and grabbing the html data
client = urlopen(URL)
page_html = client.read()
client.close()

page_soup = BeautifulSoup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"page-container"})[0]
data = containers.findAll("div", {"class":"card-item js-product-data"})


file=open("laptops.csv", "w")
file.write("EMAG-> Lista laptop uri ultrabook placa video dedicata\n")
headers = "name, price\n"

file.write(headers)

for item in data:
	full_name = item["data-name"].split()[:4]
	finalName=""
	for name in full_name:
		finalName+=name
		finalName+=" "
	full_name=finalName
	priceData = item.findAll("", {"class":"product-new-price"})
	priceFrom = priceData[0].text
	finalPrice = priceFrom.split()[2].replace(".", "")[:-2]
	
	print("name: "+ full_name + " price: " + finalPrice)
	file.write(full_name + ","+ finalPrice+'\n')
file.close()
os.startfile("laptops.csv")
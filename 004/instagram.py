

# INSTAGRAM BOT wannabe


import os
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

class InstaBot:
	def __init__(self, username, pwd):
		self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="C:/Program Files/Selenium/chromedriver.exe")
		self.driver.get("https://instagram.com")
		self.username = username
		self.pwd = pwd
		time.sleep(2)
		#self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
		#time.sleep(5)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
			.send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
			.send_keys(pwd)
		self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
		time.sleep(2)

		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

		time.sleep(1)

	    # we've connected to Instagram Account

	def goToMyProfile(self):
		self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()


	def getFollowers(self):
		time.sleep(2)
		self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]").click()
		time.sleep(1)
		
	#	sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
		self.driver.execute_script('window.scrollTo(0,500)')
		time.sleep(1)
		scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
		last_ht,ht = 0,1
		while last_ht != ht:
			last_ht = ht
			time.sleep(1)
			ht = self.driver.execute_script("""
				window.scrollTo(0,500);
				return window.scrollHeight;
				""", scroll_box)



import requests
from multiprocessing import Queue
from readData import HandleAccounts
import os
import importlib
from selenium import webdriver
import time
from instagram import InstaBot
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

class Application:
	
	def __init__(self, accounts):
		self.accounts = accounts
	
	def openFacebook(self):
		self.accounts = HandleAccounts("accounts.txt").readAccounts()
		self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/Program Files/Selenium/chromedriver.exe")
		self.driver.get("https://facebook.com")

		account = self.accounts[0][0]
		password = self.accounts[0][1]
		self.driver.find_element_by_xpath("//input[@name=\"email\"]")\
			.send_keys(account)
		self.driver.find_element_by_xpath("//input[@name=\"pass\"]")\
			.send_keys(password)	
		self.driver.find_element_by_xpath("//input[@type=\"submit\"]").click()

	def openInstagram(self):
		self.accounts = HandleAccounts("accounts.txt").readAccounts()
		bot = InstaBot(self.accounts[1][0], self.accounts[1][1])
		bot.goToMyProfile()

	def openNetflix(self):
		self.accounts = HandleAccounts("accounts.txt").readAccounts()
		self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="C:/Program Files/Selenium/chromedriver.exe")
		self.driver.get("https://netflix.com")
		username = self.accounts[2][0]
		password = self.accounts[2][1]

		self.driver.find_element_by_xpath("//*[@id=\"appMountPoint\"]/div/div/div/div/div/div[1]/div").click()
		self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/a").click()
		print(username + '->' + password)

		self.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input")\
				.send_keys(username)
		self.driver.find_element_by_xpath("//*[@id=\"id_password\"]")\
				.send_keys(password)
		self.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/form/button")\
				.click()
		time.sleep(1)
		self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[5]/div/a/div/div")\
				.click()



import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import lxml

login_email = 'fatihboyar@gmail.com'
login_password = 'QLe5kiNsXzq@vdy'

# open chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(2)

# navigate to login page
driver.get('https://database.coffeeinstitute.org/login')
time.sleep(3)

# submit login credentials
form = driver.find_element('xpath', '//html/body/content[@class="scrollable"]/div[@class="container page"]/div[@class="form short"]/div[@class="login panel"]/form') # NOTE: find_element_by_* has been removed
username = driver.find_element('name', "username")
password = driver.find_element('name', "password")
time.sleep(2)

username.send_keys(login_email)
password.send_keys(login_password)
driver.find_element('class name', "submit").click()
time.sleep(2)


# navigate to coffees page, then to arabicas page containing links to all quality reports
coffees = driver.find_element('xpath', '//html/body/header/nav[@id="main"]/div[@class="container"]/div[@class="in"]/a[@href="/coffees"]').click()
time.sleep(10)
driver.find_element('link text', 'Arabica Coffees').click()
time.sleep(3)

# these values can be changed if this breaks midway through collecting data to pick up close to where you left off
page = 0
coffeenum = 0

while True:
	print('page {}'.format(page))

	# 50 rows in these tables * 7 columns per row = 350 cells. Every 7th cell clicks through to that coffee's data page
	for i in range(1, 400, 8):
		time.sleep(2)

		# paginate back to the desired page number
		# don't think there's a way around this - the back() option goes too far back
		# some page numbers aren't available in the ui, but 'next' always is unless you've reached the end
		for p_num in range(page):
			page_buttons = driver.find_elements('class name', 'paginate_button')
			page_buttons[-1].click() # the 'next' button
			time.sleep(1)
			page_buttons = driver.find_elements('class name', 'paginate_button')

		# select the cell to click through to the next coffee-data page
		time.sleep(2) # this next line errors out sometimes, maybe it needs more of a time buffer
		test_page = driver.find_elements('xpath', '//td')[i].click()
		time.sleep(2)
		print('rows: ')
		print(len(driver.find_elements('xpath', "//tr")))
		tables = driver.find_elements(By.TAG_NAME, "table")

		# loop over all coffee reports on the page, processing each one and writing to csv
		print('tables: ')
		print(len(tables))
		j = 0
		for tab in tables:
			try:
				t = BeautifulSoup(tab.get_attribute('outerHTML'), "html.parser")
				#print(t)
				df = pd.read_html(str(t))
				name = 'coffee_{}_table_{}.csv'.format(coffeenum, j)
				df[0].to_csv(name)
				print(name)
			except:
				# only one's needed but I want this to be obnoxious since it's the only way I'm logging this currently
				print('ERROR: {} failed'.format(name))
				print('ERROR: {} failed'.format(name))
				print('ERROR: {} failed'.format(name))
				print('ERROR: {} failed'.format(name))
			j += 1

		# go back to page with all other coffee results
		#driver.back() # note: this isn't working as expected, manually going back to pg 1 via url instead
		driver.get('https://database.coffeeinstitute.org/coffees/arabica')
		time.sleep(2)
		coffeenum += 1

	page += 1
	if page == 6:
		break


# close the driver
driver.close()
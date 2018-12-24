from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
os.chdir("F:\Intern - Noah_Indium")

#list of names from database
name = ['Mark Ruffalo','Mark Rafflo','Chris Pratt','Chris Patt','Jermy Renner','Jermy Rener','Ryan Reynolds','Rian Renolds','Tom Cruise','Tom Cruise','Robert Downey J','Robert D Jr','Dwayne Johnson','The Rock'] 

#list to store corrected names
namesCorrected = []

#Open Chrome and go to google
driver = webdriver.Chrome()
driver.get('http://www.google.com')

for i in name:
    driver.find_element_by_name('q').clear() #clear search bar
    searchBar = driver.find_element_by_name('q')
    key = i + " and imdb"
    searchBar.send_keys(key) #search for key
    searchBar.send_keys(Keys.RETURN) #hit RETURN
    test = driver.find_element_by_xpath('//h3')#find element by xpath
    text = (test.text).split('-',1)[0] #converting to text, splitting with '-' and taking first element
    namesCorrected.append(text) ##append to new list
    
print(namesCorrected) #print corrected names
driver.close() #close chrome   
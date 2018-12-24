import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#list of names from database
db = pd.read_csv('databseOfActors.csv') 
name = pd.Series(db['name'])

#list to store corrected names
namesCorrected = []

k = 0

while (k<(len(name))):       
    driver = webdriver.Chrome() #Open Chrome
    driver.get('http://www.google.com') #go to google
    while (k<(len(name))):
        try:
            driver.find_element_by_name('q').clear() #clear search bar
            searchBar = driver.find_element_by_name('q')
            #key = name[k] + " and imdb"
            key = k
            searchBar.send_keys(key) #search for key
            searchBar.send_keys(Keys.RETURN) #hit RETURN
            test = driver.find_element_by_xpath('//h3') #find element by xpath
            text = (test.text).split('-',1)[0] #converting to text, splitting with '-' and taking first element
            namesCorrected.append(text) ##append to new list
            k += 1
        except:
            driver.close() #close Chrome
            break    
        
print(namesCorrected) #print corrected names
driver.close() #close chrome   

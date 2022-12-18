from bs4 import BeautifulSoup
import requests
from csv import writer
#working with multiple links calling it as project-1
#Url
url = "https://opentender.eu/"
page = requests.get(url)
print(page) #Responce is 200 which is good according to http status codes

soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('li',class_="portal-link")
print(lists)
with open('Tenders.csv','w',newline='',encoding = 'utf8')as f:
    thewriter = writer(f)
    header = ['Place','Tenders']
    thewriter.writerow(header)
    for list in lists:
        place = list.find('a').text
        tenders = list.find('div').text
        info = [place,tenders]
        print(info)
        thewriter.writerow(info)
        

# creating the bar plot
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (10, 5))
plt.bar(place, color ='maroon',
        width = 0.4, height = 0.6)
plt.show()





 

#working with more links 
#project-2

url = "https://sam.gov/search/?index=_all&page=1&pageSize=25&sort=-modifiedDate&sfm%5BsimpleSearch%5D%5BkeywordRadio%5D=ALL&sfm%5BsimpleSearch%5D%5BkeywordTags%5D%5B0%5D%5Bkey%5D=tenders&sfm%5BsimpleSearch%5D%5BkeywordTags%5D%5B0%5D%5Bvalue%5D=tenders&sfm%5Bstatus%5D%5Bis_active%5D=true"
page = requests.get(url)

print(page) #Responce is 200 which is good according to http status codes

soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('div',class_="grid-row grid-gap")
for list in lists:
    tenderss = list.find('a').text
    #escription = list.find('p').text
    print(tenderss)
    
    
    
    
#working with  more links

import pandas as pd
# Create an URL object
url = 'https://apps3.txdot.gov/apps-cq/project_tracker/'
# Create object page
page = requests.get(url)

# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')
soup
# Obtain information from tag <table>
table1 = soup.find('table',class_="summaryTable table")
print(table1)

# Obtain every title of columns with tag <th>
headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)

# Convert wrapped text in column 3 into one line text
 #headers[3] = ‘Tests/1M pop’
# Create a dataframe
mydata = pd.DataFrame(columns = headers)
# Create a for loop to fill mydata
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

# Export to csv
mydata.to_csv('data.csv', index=False)
# Try to read csv
mydata2 = pd.read_csv('data.csv')

























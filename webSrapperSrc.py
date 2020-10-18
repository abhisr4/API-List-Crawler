# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:04:43 2020

@author: Abhinaba
"""
#importing necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

apiCount = 0
apiDictionary = {}
count=0 #debugging purposes
while True:
    url = 'https://www.programmableweb.com/category/all/apis'
    response  = requests.get(url)
    data = response.text
    #creating BeautifulSoup object with data
    ObjectData = BeautifulSoup(data,'html.parser')
    apis = ObjectData.find_all('tr',{'class':['odd','even']})
    for api in apis:
        name = api.find('td',{'class':'views-field views-field-pw-version-title'}).text
        link1 = api.find('a').get('href')
        link = 'https://www.programmableweb.com'+str(link1)
        category = api.find('td',{'class':'views-field views-field-field-article-primary-category'}).text
        #creating another request and BS object to get description of API
        apiResponse = requests.get(link)
        apiData = apiResponse.text
        apiObject = BeautifulSoup(apiData,'html.parser')
        apiDiv = apiObject.find('div',{'class':'intro'}).text
        apiDivIntro = apiDiv[apiDiv.find(']')+1:]
        #print('name:',name,'\nlink:',link,'\ncategory:',category,'\ndescription:',api_desp,'\n-----')
        apiCount += 1
        #updating dictionary
        apiDictionary[apiCount] = [name,link,category,apiDivIntro]
    #updating url to crawl to next pages
    url_tag = ObjectData.find('a',{'title':'Go to next page'})
    if url_tag.get('href'):
        url = 'https://www.programmableweb.com' + url_tag.get('href')
    else:
        break
    count+=1
    print("{} is done".format(count))
print(api_no)

apiDf = pd.DataFrame.from_dict(apiDictionary,orient = 'index',columns = ['API Name','API URL','API Category','API Decrription'])
apiDf.to_csv('api_list.csv')
        

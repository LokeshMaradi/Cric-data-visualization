from urllib.request import urlopen
import pandas as pd, time 
from bs4 import BeautifulSoup as bs1
#browser=webdriver.Chrome('C:\\Users\\chromedriver.exe')
#browser.get()
ps=urlopen('https://www.espncricinfo.com/rankings/content/page/211271.html')
soup=bs1(ps,'html.parser')
body=soup.find('div',{'class':'ciPhotoContainer'})
df=pd.DataFrame(columns=['Pos','Teams','Matches','Points','Rating'])
titles=[]
c=0
for i in body.findAll('h3'):
	titles.append(i.text)
tr_list=body.findAll('tr')
for i in tr_list:
	td_list=i.findAll('td')
	row=[]
	for j in td_list:
		row.append(j.text)
	data={}
	try:
		for k in range(len(df.columns)):
			data[df.columns[k]]=row[k]
		df=df.append(data,ignore_index=True)
	
	except:
		df=pd.DataFrame(columns=['Pos','Teams','Matches','Points','Rating'])
		name=titles[c]
		c=c+1
	path='C:\\Users\\'+ name +'.csv'	
	df.to_csv(path,index=False)
print('Done')
print(df)


	


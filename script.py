#import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
web_page=requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

soup=BeautifulSoup(web_page.text, "html.parser")
print(soup)

ratings=[]
for r in soup.select('.Rating'):
  if r.string != 'Rating':
    ratings.append(float(r.string))
#print(ratings)
company=[]
for c in soup.select('.Company'):
  company.append(c.string)
company.pop(0)
data_join={'Company':company, "Rating":ratings}
df=pd.DataFrame.from_dict(data_join)
print(len(ratings))
print(len(company))
print(company)
plt.hist(ratings)
plt.show()
mean_rating=df.groupby('Company').Rating.mean()
top_ten=mean_rating.nlargest(10)
print(top_ten)

# cocoa percent
cocoPercent=[]
for p in soup.select('.CocoaPercent')[1:]:
  cocoPercent.append(float(p.string.strip('%')))
#cocoPercent.pop(0)
print(cocoPercent)
data_join['CocoaPercentage']=cocoPercent
df=pd.DataFrame.from_dict(data_join)
print(df)
#plotting a scatter plot
plt.scatter(df.CocoaPercentage, df.Rating)
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()

#Countries
country=[]
for v in soup.select('.CompanyLocation')[1:]:
  country.append(v.string)
data_join['CompanyLocation']=country
df=pd.DataFrame.from_dict(data_join)
# finding the country top countries of cocoa
top_counties =df[df.Rating > 4]
print(top_counties)
# in Italy produces the best cocoa bean with a rating of 5.0
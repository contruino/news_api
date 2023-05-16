from newsapi import NewsApiClient
import datetime as dt
import pandas as pd
import xlsxwriter
newsapi = NewsApiClient(api_key='80b599fc0ce5485d81faed170a211c39')
data = newsapi.get_everything(q='tesla',language='en',page_size=20)

print(type(data))
print(data['status'])
print(data['totalResults'])
print(data['articles'][0])

article = data['articles']
for a,b in enumerate(article):
    print(f'{a}:     {b["title"]}')

for k,v in article[0].items():
    print(f'\n{k.just(15)}  {v}')

print(pd.DataFrame(article))

#write to csv
pd.DataFrame(article).to_csv('result.csv')

#write to excel
author = article['author']
title = article['title']
content = article['content']

authors = []
titles = []
contents = []

authors.append(author)
titles.append(title)
contents.append(content)

workbook = xlsxwriter.Workbook('results.xlsx')
worksheet = workbook.add_worksheet('first')

worksheet.write(0,0,'0')
worksheet.write(0,1,'author')
worksheet.write(0,2,'title')
worksheet.write(0,3,'content')

for j in range(len(authors)):
    worksheet.write(j+1,0,str(j))
    worksheet.write(j+1,1,authors[j])
    worksheet.write(j+1,2,titles[j])
    worksheet.write(j+1,3,contents[j])

workbook.close()


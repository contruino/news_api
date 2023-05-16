from newsapi import NewsApiClient
import datetime as dt
import pandas as pd

newsapi = NewsApiClient(api_key='your api key')
data = newsapi.get_everything(q='tesla',language='en',page_size=20)
print(type(data))
print(data['status'])
print(data['totalResults'])
print(data['articles'][0])
article = data['articles']
for a,b in enumerate(article):
    print(f'{a}:     {b["title"]}')

for k,v in article[0].items():
    print(f'\n{k.ljust(15)}  {v}')

print(pd.DataFrame(article))

info = newsapi.get_everything(q='cybertruck',from_param='2023-01-31')
print(info['totalResult '])
result = data['articles'].copy()


import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

questionlist = []

search = str(input("What are you looking for ?"))
linkk= "https://stackoverflow.com"
url = f'https://stackoverflow.com/questions/tagged/{search}'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
questions = soup.find('div', id= 'questions')
new = questions.find_all("div", class_="s-post-summary--content")
time.sleep(5)

questionlist= []
for item in new:
    
    question={
        "Title" : item.find('a').text,
        "link" :'https://stackoverflow.com' + item.find('a')["href"],
        'votes': item.find('span').text,
        'date': item.find('span', class_="relativetime")["title"],
         
    #     questionlist.append(question)
    # return

        
        }
    questionlist.append(question)

print(questionlist)
# getQuestions('python')
# print(questionlist)

df = pd.DataFrame(questionlist)
df.to_excel('stackquestio.xlsx', index=False)
print('Find.')
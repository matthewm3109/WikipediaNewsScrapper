from urllib.request import urlopen 
import bs4
from bs4 import BeautifulSoup 

#Retrive and parse HTML Code
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, 'html.parser')

#Filter based on HTML Tree 
parsedData = bs.find('td',{'id':'mp-right','class':'MainPageBG mp-bordered'})
parsedData2 = parsedData.div.ul
news = parsedData2.children
#Reduce to text and print 

for event in news: 
    eventString = ''
    for a in event: 
        if isinstance(a,bs4.element.Tag):
            a = a.get_text()
            eventString = eventString + a 
        elif not(a): 
            print("empty string")
        else: 
            eventString = eventString + a 
    print(eventString.strip())

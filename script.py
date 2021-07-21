#1. Import list of movies -- output table
#2. Get wikipedia pages - output pages (wikipedia object)
#3. Scrape film wiki page for cast -- output list of actors
#4. Find birthday of actors -- output birthday
#5. Find nationality of actors -- output nationality


import pandas as pd #for making dataframes
import urllib #for urls
from html.parser import HTMLParser #for reading html
from bs4 import BeautifulSoup #for manipulating web pages
import requests #not sure
import xlsxwriter #for writing to excel
import numpy as np
from urllib.request import urlopen
import urllib.request
import wikipedia as wk

#1. Import list of movies -- output table (Dataframe)

film_data = pd.read_csv('Documents/filmdata.csv', quotechar='"')

#2. Get wikipedia pages - output pages (wikipedia object)

movie_np = np.array([i for i in film_data["Movie Title"]])
year_np = np.array([i for i in film_data["Year"]])

for movie in film_data:

wikis1 = []

for x in enumerate(movie_np[0:600]):
    try:
        y = wk.page(x)
    except (KeyError, wk.exceptions.PageError, wk.exceptions.DisambiguationError):
        y = "error"
    wikis1.append(y)
   
#2.b. remove error 

film_wiki = df.loc[lambda df: df["Wiki"]!="error", :]
   
#3. Scrape film wiki page for cast -- output list of actors

def starring(movie_wiki):
    wikisoup = BeautifulSoup(movie_wiki.html(), 'html.parser')
    table = wikisoup.find('table',{"class": "infobox"})
    info_box_dictionary = {}
    for tr in table.find_all('tr'):
        if tr.find('th'):
            info_box_dictionary[tr.find('th').text] = tr.find('td')
    cast = []
    for line in info_box_dictionary["Starring"].find_all("a"):
        cast.append(line.string)
    return cast
    
test_set = [i for i in film_wiki["Wiki"][0:10]]   

def casting(i):    
    try:
        castlist = starring(testdf["Wiki"][i])
        size = len(castlist)
        films = pd.DataFrame({
       "Movie" : [testdf["Movie"][i] for n in range(size)],
        "Cast" : starring(testdf["Wiki"][i])
        })
    except KeyError:
        films = pd.DataFrame({
       "Movie" : ["error"],
        "Cast" : ["error"]
        })
    return films
    
#dictionary film

list_of_films = [i for i in film_wiki["Movie"]]
list_of_wikis = [i for i in film_wiki["Wiki"]]

dicts = []
wikinp = np.array(list_of_wikis)

for i in range(0,len(list_of_wikis): 
    try:
        alist = starring(wikinp[i])   
        filmdict = {list_of_films[i] : alist}
    except (AttributeError, KeyError):
        filmdict = {list_of_films[i] : "error"}
    dicts.append(filmdict)
    
pd.json_normalize(dicts)
  



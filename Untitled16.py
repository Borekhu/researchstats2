#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


import itertools 


# In[3]:



#1. Import list of movies -- output table (Dataframe)

film_data = pd.read_csv('filmdata.csv', quotechar='"')


# In[4]:


#2. Get wikipedia pages - output pages (wikipedia object)

movie_np = np.array([i for i in film_data["Movie Title"]])
year_np = np.array([i for i in film_data["Year"]])


# In[5]:


film_data


# In[6]:


def starring(m):
    cast = []
    if m == "error":
        cast = "error"
    else:
        wikisoup = BeautifulSoup(m.html(), 'html.parser')
        table = wikisoup.find('table',{"class": "infobox"})
        info_box_dictionary = {}
        for tr in table.find_all('tr'):
            b = tr.find('th')
            try:
                info_box_dictionary[b.text] = tr.find('td')
            except AttributeError:
                cast = "attribute error"
        try:
            b = info_box_dictionary["Starring"].find_all("a")
            cast = [line.string for line in b]
        except KeyError:
            cast= "keyerror"
    return cast


# In[360]:


testdf = film_data[0:10]


# In[361]:


testdf


# In[410]:


#isolating the errors
errors= []
for i in range(len(film_data)):
    if film_data["Wiki"][i]=="error":
        errorfilm={"Film" : film_data["Movie Title"][i], 
                   "Year": film_data["Year"][i]}
        errors.append(errorfilm)


# In[412]:


errordf = pd.DataFrame(errors)


# In[414]:


errordf


# In[431]:


results = []

for index, row in errordf.iterrows():
    f = row["Film"]
    t = wk.search(f, results=5)
    results.append(t)


# In[455]:


errordf["Results"] = results

e_year = errordf["Year"]


# In[482]:


hg = errordf.explode("Results")


# In[483]:


hg


# In[464]:


posts = []
for list_ in results:
    for row in list_:
        if "film" in row:
            p = row
        for i in e_year:
            if str(i) in row:
                p = row
            else:
                p = list_[0]
    posts.append(p)


# In[465]:


posi = []

for k in posts:
    try:
        w = wk.page(k)
    except (wk.exceptions.PageError, wk.exceptions.DisambiguationError):
        w = "error"
    dic = {
        "Film" : k,
        "Wiki" : w
    }
    posi.append(dic)


# In[507]:


posi[0:10]


# In[508]:


for value in posi[4].values():
    print(type(value))


# In[506]:


posi[7]


# In[470]:


films = film_data.filter(errordf)


# In[496]:


films


# In[492]:


for i in film_data["Wiki"]:
    if i != "error":
        ac = starring(i)
    else:
        ac = "error"


# In[515]:


fix_ = []


# In[521]:


wikiss = []

for i in film_data["Wiki"]:
    if i != "error":
        try:
            b = wk.page(i)
        except (wk.exceptions.PageError, wk.exceptions.DisambiguationError):
            b = "error"
    wikiss.append(b)


# In[540]:


errordf


# In[29]:


def findwiki(x):
    if x is None:
        d = "Empty"
    else:
        try:
            d = wk.page(x, auto_suggest=False)
        except (wk.exceptions.PageError, wk.exceptions.DisambiguationError, AttributeError):
            d = "error"
    return d


# In[26]:


def searchwiki(x):
    try:
        w = wk.search(x, results=1)
    except (wk.exceptions.PageError, wk.exceptions.DisambiguationError, AttributeError, KeyError):
        w = "error"
    return w


# In[556]:


test_


# In[565]:


test_ = film_data[0:10]


# In[616]:


wiki = []

for i in range(10):
    row = list(test_["Movie Title"])[i]
    try:
        m = findwiki(row)
    except wk.exceptions.PageError:
        m = "error"
    wiki.append(m)


# In[617]:


wiki


# In[628]:


test_.apply(lambda row: searchwiki(row["Movie Title"]), axis=1)


# In[12]:


film_data["Wiki Title"] = film_data.apply(lambda row: searchwiki(row["Movie Title"]), axis=1)


# In[39]:


testdf = film_data[0:10]


# In[44]:


testdf.apply(lambda row: findwiki(row["Wiki Title"]), axis=1)


# In[50]:


testdf.apply(lambda row: findwiki(row["Wiki Title"]) if len(row["Wiki Title"])!=0 else row , axis=1)


# In[78]:


moo1 = film_data[0:100].copy()
moo2 = film_data[100:200].copy()
moo3 = film_data[200:300].copy()
moo4 = film_data[300:400].copy()
moo5 = film_data[400:500].copy()
moo6 = film_data[500:600].copy()


# In[88]:


moo1["W2"] = moo1.apply(lambda row: findwiki(row["Wiki Title"]) if len(row["Wiki Title"])!=0 else row , axis=1)


# In[79]:


moo2["W2"] = moo2.apply(lambda row: findwiki(row["Wiki Title"]) if len(row["Wiki Title"])!=0 else row , axis=1)


# In[80]:


moo3["W2"] = moo3.apply(lambda row: findwiki(row["Wiki Title"]) if len(row["Wiki Title"])!=0 else row , axis=1)


# In[81]:


moo4["W2"] = moo4.apply(lambda row: findwiki(row["Wiki Title"]) if len(row["Wiki Title"])!=0 else row , axis=1)


# In[82]:


moo5["W2"] = moo5.apply(lambda row: findwiki(row["Wiki Title"]) if len(row["Wiki Title"])!=0 else row , axis=1)


# In[86]:


moo6["W2"] = moo6.apply(lambda row: findwiki(row["Wiki Title"]) if len(row["Wiki Title"])!=0 else row , axis=1)


# In[70]:


myframes = []

for i in range(1,7):
    c = str(i)
    n = "moo"+c
    myframes.append(n)


# In[89]:


moo1


# In[90]:


moo2


# In[92]:


myset = pd.concat([moo1, moo2, moo3, moo4, moo5, moo6], sort=False)


# In[94]:


v = myset.drop(columns=['Wiki','Wiki Title'])
#Drop columns from DataFrame


# In[96]:


v.to_csv("newfilm.csv", index=False)


# In[110]:


errors = []
eyears = []

for index, row in myset.iterrows():
    if "error" in str(row["W2"]):
        k = row["Movie Title"]
        p = row["Year"]
        errors.append(k)
        eyears.append(p)


# In[113]:


l = pd.DataFrame(errors, eyears)

l.to_csv("errorfilms.csv", index=False)


# In[114]:


l


# In[235]:


def trywiki(x, year):
    y = str(year)
    separator = " "
    try :
        a = separator.join([x, y])
        b = wk.search(a, results=1)
    except (wk.exceptions.DisambiguationError, wk.exceptions.PageError):
        c = separator.join([x, " film"])
        b = wk.page(c, auto_suggest=False)
        try:
            d = separator.join([x, "(", str(y), " film", ")"])
            b = wk.page(d, auto_suggest=False) 
        except (wk.exceptions.DisambiguationError, wk.exceptions.PageError):
            b = "error"
    return b


# In[272]:


def findpage(b):
    n = wk.page(b, auto_suggest=False)
    return n


# In[236]:


print(trywiki("Jumper", 2008))


# In[142]:


po = []

for index, row in l.iterrows():
    T = (index, row)
    po.append(T)


# In[150]:


m = l.reset_index()


# In[153]:


m


# In[164]:


oo = m.rename(columns = {'index': "year",
    "o":'film'})


# In[189]:


type(oo["year"][4])


# In[202]:


po=[]
for row in list(oo.iterrows()):
    x = row[0]
    y = row[1]
    try:
        b = trywiki(str(x), str(y))
    except KeyError:
        b = "error"
    po.append(b)


# In[246]:


years= [i for i in oo["year"]]
films= [i for i in oo[0]]


# In[262]:


po=[]
for i in range(len(years)):
    x = years[i]
    y = films[i]
    try:
        b = trywiki(str(x), str(y))
    except KeyError:
        b = "error"
    po.append(b)


# In[278]:


po


# In[275]:


wlist = []
for i in po:
    f = findpage(i)
    wlist.append(f)


# In[251]:


trywiki("Tenet", 2020)


# In[271]:


trywiki(po[o])


# In[281]:


frm = pd.DataFrame({
    "Y" : years,
    "F" : films
})


# In[287]:


frm


# In[284]:


frm["W"] = frm.apply(lambda row: trywiki(row["F"], row["Y"]), axis=1)


# In[290]:


frm["U"] = frm.apply(lambda row: findpage(row["W"]), axis=1)


# In[291]:


frm


# In[ ]:


frm.replace("F")


# In[293]:


v


# In[296]:


frm.to_csv("errorfilms.csv")


# In[300]:


wis = []

for j in v["W2"]:
    wis.append(j)

for i in frm["U"]:
    wis.append(i)


# In[310]:


w1 = wis[0:100]
w2 = wis[100:200]
w3 = wis[200:300]
w4 = wis[300:400]
w5 = wis[400:500]
w6 = wis[500:600]


# In[311]:


w1


# In[312]:


k = []

for i in w1:
    if i=="error":
        h = "error"
    else:
        try:
            h = starring(i)
        except AttributeError:
            h = "error"
    k.append(h)


# In[315]:


pd.DataFrame({
    "Wiki" : w1,
    "Cast" : k
})


# In[313]:


k = []

for i in w1:
    if i=="error":
        h = "error"
    else:
        try:
            h = starring(i)
        except AttributeError:
            h = "error"
    k.append(h)


# In[316]:


bn = [w1, w2, w3, w4, w5, w6]


# In[322]:


bn_df = pd.DataFrame(bn)


# In[324]:


wik = bn_df.melt()


# In[328]:


wik


# In[325]:


def casting(i):
    if i=="error":
        h = "error"
    else:
        try:
            h = starring(i)
        except AttributeError:
            h = "error"
    return h


# In[337]:


kk = wik[0:20]
kk1 = wik[20:100]
kk2 = wik[100:200]
kk3 = wik[200:300]
kk4 = wik[300:400]
kk5 = wik[400:500]
kk6 = wik[500:600]


# In[336]:





# In[338]:


kk["Actor"] = kk.apply(lambda row: casting(row["value"]) if "error" not in row else "error", axis=1)


# In[332]:


kk


# In[342]:


dflist = [i for i in [kk, kk1, kk2, kk3, kk4, kk5, kk6]]


# In[345]:


for i in dflist:
    i["Actor"] = i.apply(lambda row: casting(row["value"]) if "error" not in row else "error", axis=1)


# In[353]:


kk4["Actor"] = kk4.apply(lambda row: casting(row["value"]) if "error" not in row else "error", axis=1)


# In[350]:


kk5["Actor"] = kk5.apply(lambda row: casting(row["value"]) if "error" not in row else "error", axis=1)


# In[351]:


kk6["Actor"] = kk6.apply(lambda row: casting(row["value"]) if "error" not in row else "error", axis=1)


# In[352]:


kk4


# In[354]:


df_ = pd.concat(dflist)


# In[358]:


df_.to_csv("actorsmasterlist.csv")


# In[359]:


df_["Title"] = v["Movie Title"]


# In[361]:


df_.to_csv("actorsmasterlist.csv")


# In[362]:


df_


# In[370]:


for i in df_["Title"]:
    if i in df_["value"]:
        df_["Match"] = "yes"


# In[398]:


titles = []
wiki =[]

for i in range(600):
    for j in range(600):
        if df_["Title"][i] in str(df_["value"][j]):
            lol = {df_["Title"][i], i , j}
            titles.append(df_["Title"][i])
            wiki.append(j)
            


# In[399]:


jj = {
    "Title" : titles,
    "Wiki": wiki
}


# In[403]:


opo = pd.DataFrame(jj)


# In[407]:


opo


# In[411]:


opo["Correct"] = opo.apply(lambda row: wiki(row["Wiki"]), axis=1)


# In[ ]:





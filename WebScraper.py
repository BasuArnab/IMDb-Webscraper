
# coding: utf-8

# In[131]:


import requests
from bs4 import BeautifulSoup
r= requests.get("http://www.imdb.com/india/top-rated-indian-movies/")
c=r.content
soup= BeautifulSoup(c,"html.parser")
all=soup.find_all("td",{"class":"titleColumn"})
all2=soup.find_all("td",{"class":"ratingColumn imdbRating"})
l=[]
count=0
for i,j in zip(all,all2):
    d={}
    d["Name"]=i.find("a").text
    d["Year"]=i.find("span",{"class":"secondaryInfo"}).text.replace("(","").replace(")","")
    d["Rating"]=j.find("strong").text

    s=str(i.find("a"))[8:].split()

    #the following code will give the description, duration and genre of any imdb movie. just make s equal to the link of the movie.
    s="http://www.imdb.com"+ str(s[0])[1:][:-1]
    r2=requests.get(s)
    c2=r2.content
    soup2=BeautifulSoup(c2,"html.parser")
    all3=soup2.find("meta",{"name":"description"})
    desc=str(all3)[15:][:-22]
    all4=soup2.find("time",{"itemprop":"duration"})
    duration=all4.text
    rd=duration.replace("\n","").replace(" ","")
    genre=""
    for k in soup2.find_all("span",{"itemprop":"genre"}):
        genre+=k.text+","
    #till here

    d["Description"]=desc
    d["Duration"]=rd
    d["Genre"]=genre
    l.append(d)
    count+=1
    print("Page "+ str(count) + " Completed")

import pandas
df=pandas.DataFrame(l)
df.to_csv("IOutput.csv")


# In[130]:


l


# In[ ]:








# In[ ]:

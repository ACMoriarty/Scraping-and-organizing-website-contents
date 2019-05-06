#!/usr/bin/env python
# coding: utf-8

# In[17]:


from bs4 import BeautifulSoup
import requests
page = requests.get('http://www.enoughproject.org/take_action')
bs = BeautifulSoup(page.content, "lxml")
ta_divs = bs.find_all("div", class_="wpb_wrapper")



headings=bs.find_all("h6", class_="vc_custom_heading")


articles=[]
for ta in ta_divs:
    art=ta.p
    if art!=None:
        articles.append(art.get_text())


        
        
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

    
    
    
    
#print(len(ta_divs))
#print(len(headings))
#print(len(articles))
#print(ta_divs)
for art, heading in zip(reversed(articles), reversed(headings)):
    title = heading.get_text()
    link = ta.a.get_text()
    about = art
    #print( +'/n'+ about)

    print(color.BOLD + title + color.END +'\n'+ about)


all_data = []
for ta, heading in zip(ta_divs, headings):
    data_dict = {}
    data_dict['title'] = heading.get_text()
    #data_dict['link'] = ta.a.get('href')
    data_dict['about'] = [art for art in articles]
    all_data.append(data_dict)
#print(all_data)


# In[ ]:





# In[ ]:





# In[ ]:





import requests 
from bs4 import BeautifulSoup 
import re


url = 'your HTML_PAGE url'

# STEP1: Get The HTML
response = requests.get(url)
htmlcontent = response.content
print(htmlcontent)


#Step 2: parse the html
soup = BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify())

#step 3: HTML tree traversal
#commonly used types of object
# get the title for html page
title = soup.title
print(type(title))# 1.Tag
print(type(title.string))# 2. Navigable string
print(type(soup))# 3. Beautifulsoup


# # 4. Comment
markup = "<p><!-- this is a comment in HTML></P>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))


#get the paragraph from the html page
paras = soup.find_all('p')
print(paras)



#get the first element in html page
print(soup.find('p'))


#get the last element in html page
print(soup.find_all('p')['class'])

#find all elements with class lead
print(soup.find_all('p',class_='lead'))

#get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

#get the anchor tags from the html page
anchor_tags = soup.find_all('a')
all_links = set()

#get all the links on the page
for link in anchor_tags:
    if (link!='#'):
        linktext = "your HTML_PAGE url" +link.get('href')
        all_links.add(link)
        print(linktext)

#to find anchor tag using id
a_tag = soup.find('a',id='link3')
print(a_tag)

#to get all div tags
div = soup.find_all('div')
for div_tags in div:
    print(div_tags)

# to find div tag using id
navbarsupportedcontent = soup.find(id='imgpreview2')
print(navbarsupportedcontent)

#regular expression
for tag in soup.find_all(re.compile("^t")):
    print(tag.name())



# for ele in navbarsupportedcontent:
#     print(ele)

for item in navbarSupportedContent.stripped_strings:
     print(item)


#to navigate between page elements that are on the same level
# print(navbarSupportContent,next_sibling.next_sibling)
# print(navbarSupportContent,previous_sibling.previous_sibling)      

# print(navbarSupportedContent.parent)


# to find tags bycss selector
ele = soup.css.select('#loginModal')
print(ele)
 
import requests
from bs4 import BeautifulSoup


#file handling in python
# f = open("temp.txt","r")
# print(f.read())

# f1 = open("temp.txt","r")

# for each in f1:
#     print(each)

# # "w": is used to write information and previous information will be deleted
# fi = open('temp.txt','w')
# fi.write("focus on your goals")
# fi.write("rather than focusing somewhere else")
# fi.close()

# f3 = open('temp.txt','r')
# print(f3.read())
# # "a": is used to append/write information to existing file 

# f4 = open('temp.txt','a')
# f4.write('this is what happens when no one cares')
# f4.close()

# f5 = open('temp.txt','r')
# print(f5.read())

# with open('temp.txt','r') as file:
#     print(file.read())

# with open('temp.txt','w') as flow:
#     flow.write("gufran this side")
#     flow.write("coding something different")
#     flow.write("how to extract data from the web")
#     flow.close()

# with open("temp.txt","r") as f:
#     print(f.read())
# url = "https://codeforces.com/"
# r = requests.get(url)
# print(r)
# #printing the content of the given url

# print(r.content)

url = "https://www.geeksforgeeks.org/python-programming-language/"
r = requests.get(url)

# printing the content using beautifulsoup library and using parser

soup = BeautifulSoup(r.content,"lxml")
#print(soup)
#print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent.name)

#find all is used to search or find the specific information from the html page
# s = soup.find_all('div')
# print(s)

# s1 = soup.find_all('p')
# print(s1)

# val = soup.find('div')
# content = val.find_all('p')
# print(content)

#all text from the page

# val = soup.find('div',class_='entry-content')
# lines = val.find_all('p')
# for line in lines:
#     print(line.text)

#extracting links from the page

# const = soup.find_all('a')
# for links in const:
#     print(links.get('href'))

#extracting images from the page

image_list = []
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    image_list.append({"src":src,"alt":alt})
    
for image in image_list:
    print(image)

slt = soup.find('ul')
values = slt.find_all('li')

for li in values:
    print(li.text)






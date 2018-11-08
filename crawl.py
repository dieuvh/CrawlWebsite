import time
from selenium import webdriver
import os
import pandas as pd
driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.thailandstarterkit.com/articles/')
topic_name = []
h3 = driver.find_element_by_class_name('sitemap-grid').find_elements_by_tag_name('h3')
for i in range (0,len(h3)):
    topic_name.append(h3[i].text)
ul = driver.find_element_by_class_name('sitemap-grid').find_elements_by_tag_name('ul')
li=[]
def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0, size):
        list_of_objects.append(list())  # different object reference each time
    return list_of_objects
for i in ul:
    li.append(i.find_elements_by_tag_name('li'))
link_li = []
for i in ul:
    link_li.append(i.find_elements_by_tag_name('a'))

for i in range(0,len(link_li)):
    for j in range(0,len(link_li[i])):
        link_li[i][j]=link_li[i][j].get_attribute('href')
content = init_list_of_objects(len(ul))
for i in range(0,len(link_li)):
    content.append(link_li[i])
title = init_list_of_objects(len(ul))
for i in range(0,len(link_li)):
    for j in range(0, len(li[i])):
        title[i].append(li[i][j].text.replace(' ',''))


for i in range(0,len(link_li)):

    for j in range(0,len(link_li[i])):
        driver.get(link_li[i][j])
        content[i].append(driver.find_element_by_class_name('content').get_attribute('innerHTML'))

for i in range(0,len(link_li)):
    folder = topic_name[i].replace('[','').replace(',','').replace(']','')
    os.system('mkdir %s'%folder)
    for j in range(0,len(link_li[i])):

        f = open('%s\%s.html' % (folder,title[i][j]), 'w')
        f.writelines(str(content[i][j].encode("utf-8")))
f.close()


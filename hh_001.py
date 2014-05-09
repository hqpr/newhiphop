#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://www.hotnewhiphop.com/mixtapes/
"""

__author__ = "Alexey Dubnyak"
__version__ = "1.0.0"
__email__ = "adubnyak@gmail.com"

import urllib
import re
import lxml.html
import time
from selenium import webdriver
from os import getcwd, rename, listdir
import os
import zipfile

#url = 'http://www.hotnewhiphop.com/mixtapes/'

logfile = open('log.txt', 'rb+')
url = 'local.htm'
c = urllib.urlopen(url)

link_lst = []
doc = lxml.html.document_fromstring(c.read())
for link in doc.cssselect('div.list-item-title a'):
    links = link.get('href')
    link_lst.append(links)
    logfile.writelines(links + '\n')
logfile.close()

# Connecting to a single page
#c1 = urllib.urlopen(link_lst[0])  # release
c1 = urllib.urlopen('intpage.htm')

source = lxml.html.document_fromstring(c1.read())
for title in source.cssselect('h1.pull-left'):
    title = title.text
    title = title.replace('\n', '')
    title = title.replace('			', '')
    title = title.replace('  ', '')

    artist = title.split(' - ')
    album = artist[1]
#print title

#for download in source.cssselect('span.ctrl-download'):
#    print download.get('onclick')

directory = os.path.join("C:\Users\Oleksii\Dropbox\Public\WORK\hotnewhiphop")

dr = album.replace(' - ', '-').replace(' ', '-').replace('\t\t', '').replace('\r', '')
if dr[-1] == '-':
    dr = dr[:-1]
#  Unzip file
for root, dirs, files in os.walk(directory):
    for f in files:
        if f.endswith('zip'):
            zfile = zipfile.ZipFile(f)
            for name in zfile.namelist():
                zfile.extract(name, dr)
            zfile.close()
        os.remove(f)

tracklist = open('tracklist.meta', 'wb+')
for root, dirs, files in os.walk('%s\%s' % (directory, dr)):
    for file in files:
        file = os.path.join(root, file)
        if file.endswith('jpg'):
            os.rename(file, '%s\image.png' % root)
            pass
    for track in files:
        track = os.path.join(root, track)
        if not track.endswith('png'):
            tracklist.writelines(track[:-4] + '<br>')


# Selenium settings
#fp = webdriver.FirefoxProfile()
#fp.set_preference("browser.download.folderList", 2)
#fp.set_preference("browser.download.manager.showWhenStarting", False)
#fp.set_preference("browser.download.dir", getcwd())
#fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/Zip")
#fp.set_preference("browser.helperApps.alwaysAsk.force", False);
#browser = webdriver.Firefox(firefox_profile=fp)
#browser.get('http://www.hotnewhiphop.com/tha-joker-meanwhile-new-mixtape.112219.html')
#elem = browser.find_element_by_class_name("ctrl-download")
#elem.click()


#for line in logfile.readlines():
#    if link_lst[0] not in line:
#        print 'ok'



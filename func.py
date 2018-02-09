from bs4 import BeautifulSoup
import urllib2
import sys
import re

def url_extract(message):
    url = urllib2.urlopen(str(message))
    html = url.read()
    return html

def html_parser(extract):
    link_list = []
    html = BeautifulSoup(extract, 'html.parser')
    links = html.findAll('a', attrs={'href': re.compile("^http://")})
    for link in links:
        link_list.append(link.get('href'))

    return link_list

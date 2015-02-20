#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import urllib.request
import re

plugin_version = '0.1'
plugin_name = 'Adobe Flash'
#
#url = 'http://www.adobe.com/de/products/flashplayer/distribution3.html'
#site = urllib.request.urlopen(url)

def hello():
    print('Loaded plugin: ' + plugin_name + ' ' + plugin_version)


def run():
    site = open('test/adobeflash.html', 'r')
    content = site.read()
    regex = r'Flash Player\xa0([\d\.]+) \(Windows und Mac\)'
    match = re.search(regex, content)
#   linex = r'Flash Player\xa0([\d\.]+) \(Linux\)'
#   linux_match = re.search(linex, content)
#    if linux_match:
#       linux_version = linux_match.group(1)
    if match:
        return(match.group(1))
    return None



#!/usr/bin/env python
#
# @name:    Simple url2domain Converter Script
# @repo:    NA
# @author:  Shane Daniels (PBCT3CH)
# Notes:  url2domian.py will take in a file with URL strings and strip out the domain names.

import sys
import urllib.parse

inFilePath = input("Please enter path to Input File:")
outFilePath = input("Please enter path for Output File:")
inFile = open(inFilePath,'r')
outFile = open(outFilePath,'w+')

for url in inFile.readlines():
    domain = urllib.parse.urlsplit(url)[1].split(':')[0]
    domain = domain.replace("www.","")
    outFile.write(domain + "\n")
inFile.close()
outFile.close()


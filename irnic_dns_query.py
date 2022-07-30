import requests
import re
from nltk.corpus import words
import os

urlll = 'http://whois.nic.ir/?name='
word_list = words.words()
for i in range (0,5000000,13):
    if len(word_list[i]) == 5:
        dom = word_list[i] + '.ir'
        print(dom)
        try:
            os.system("nslookup -q=ns " + dom + ">> ttttt.txt 2>&1 ")
        except:
          print("An exception occurred")
        



    

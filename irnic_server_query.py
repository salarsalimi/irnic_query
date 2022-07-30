import requests
import re
from nltk.corpus import words

# Base Url 
urlll = 'http://whois.nic.ir/?name='
# Adding word list
word_list = words.words()
for i in range (0,5000000,6):  #  Go throw words - Step is 6 in this example
    if len(word_list[i]) == 4:  #  We look for 4 character words
        dom = urlll + word_list[i] + '.ir'
        print(dom)
        try :
            r = requests.get(dom,timeout=10)  #  Set a timeout cause irnic servers are too slow and fials most of times
            mytxt = r.text
        except:
            continue

        pattern = 'ERROR:101:'  #  Filed that apear if domain is available
        match_dom = re.findall(pattern, mytxt) 
        if  (len(match_dom))  ==  0:
            print ('Domain is not available')
        else:
            print ('Domain is available you can register')



    

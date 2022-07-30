# irnic_query

A simple python program to query domains with two methods     
1 ) Using IRNIC servers to query for available domains ( 100% works but too slow )      
2 ) Using DNS query to see if domain can answer ( not 100% accurate and we have too many flase positives )      

# How methods work

If you wnat to know how each method works it is rather simple      
1 ) In this method we should look for a field like  'ERROR:101:'  that indicates there is no recorde      
2 ) We should look for  'Non-existent domain'  in response of query which means either there is no domain registerd or there is no NS record set ( Flase Positive )

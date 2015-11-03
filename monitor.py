import json
import time
import random
import pycurl

#-------------------------------------------------------
# Specify api key
#-------------------------------------------------------

apikey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlLZXkuVElNRVNUQU1QIjoxNDQ1MzA4MDQ0ODI5LCJBcGlLZXkuQUNDT1VOVF9JRCI6IjU4ZTlhMjU4LWE1MTctNGQxOC1iYTgzLWQ4YmEzYWU4OTdjOCIsIkFwaUtleS5URU5BTlRfSUQiOiJlZDJmZGE5NC03NDZiLTQ4ZmMtYTUzNC03MDQzYTQ0YzhkMTgiLCJBcGlLZXkuVEVOQU5UX0NSRUFURURfVElNRSI6MTQ0NTMwODA0Mzc4MH0=.Gw0KG68a5FZzs4uxjxeMfIK98G2rYtoEAaxDnYq5aGU="

#-------------------------------------------------------
# Set up headers
#-------------------------------------------------------

headers = ['Expect:', 'Content-Type: application/json' ,  'X-API-KEY: ' + apikey]


while True:

    #-------------------------------------------------
    #  Gemerate fake numbers here.  Replace random 
    #  numbers with real data collection.
    #-------------------------------------------------
    timestamp = time.mktime(time.localtime())

    browse_time = random.randrange(1, 60, 1);
    bid_time = random.randrange(1, 60, 1);

    browse_count = random.randrange(25, 50, 2);
    bid_count = random.randrange(25, 50, 2);

    #--------------------------------------------------
    #  Create data structure for metrics posting
    #--------------------------------------------------
    myMetrics = [
        {
        "entity_type_id": "TRANSACTION",
        "entity_id": "oa-appserver-1.browse_catalog",
        "time_series": [
            {
                "metric_id": "number_of_requests",
                "values": [
                    { "v": browse_count, "t": timestamp }
                ]
            },
            {
                "metric_id": "request_response_time",
                "values": [
                    { "v": browse_time, "t": timestamp }
                ]
            }
        ]
       },
        {
        "entity_type_id": "TRANSACTION",
        "entity_id": "oa-appserver-1.bid_tx",
        "time_series": [
            {
                "metric_id": "number_of_requests",
                "values": [
                    { "v": bid_count, "t": timestamp }
                ]
            },
            {
                "metric_id": "request_response_time",
                "values": [
                    { "v": bid_time, "t": timestamp }
                ]
            }
        ]
       }
      ]

    #-------------------------------------------------------
    # Specify the uri
    #-------------------------------------------------------

    url = "https://truesight.bmc.com/api/v1/metrics?async=false"

    #-------------------------------------------------------
    # Issue the request
    #-------------------------------------------------------

    c= pycurl.Curl()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HTTPHEADER,headers )
    c.setopt(pycurl.CUSTOMREQUEST, "POST")
    data = json.dumps(myMetrics)
    c.setopt(pycurl.POSTFIELDS,data)        
    c.perform()
    print ("status code:=" +  str(c.getinfo(pycurl.HTTP_CODE)))
    c.close()
    
    #-------------------------------------------------------
    # Print the result
    #-------------------------------------------------------

    # print(response.status_coder)
    # printr(response.textr)
    time.sleep(60)

#----------------------------------------------------
# end while
#----------------------------------------------------


print("exiting....")


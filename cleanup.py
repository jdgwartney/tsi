import json
import pycurl
from requests.auth import HTTPDigestAuth



#-------------------------------------------------------
# define function to subit requests
#-------------------------------------------------------
def submitRequest( url  ):
    headers = ['Expect:', 'Content-Type: application/json' ,  'X-API-KEY: ' + apikey]
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HTTPHEADER,headers )
    c.setopt(pycurl.CUSTOMREQUEST, "DELETE")
    c.perform()
    print ("status code:=" +  str(c.getinfo(pycurl.HTTP_CODE)))
    c.close()
    return


#-------------------------------------------------------
# setup api key
#-------------------------------------------------------

apikey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlLZXkuVElNRVNUQU1QIjoxNDQ1MzA4MDQ0ODI5LCJBcGlLZXkuQUNDT1VOVF9JRCI6IjU4ZTlhMjU4LWE1MTctNGQxOC1iYTgzLWQ4YmEzYWU4OTdjOCIsIkFwaUtleS5URU5BTlRfSUQiOiJlZDJmZGE5NC03NDZiLTQ4ZmMtYTUzNC03MDQzYTQ0YzhkMTgiLCJBcGlLZXkuVEVOQU5UX0NSRUFURURfVElNRSI6MTQ0NTMwODA0Mzc4MH0=.Gw0KG68a5FZzs4uxjxeMfIK98G2rYtoEAaxDnYq5aGU="


submitRequest("https://truesight.bmc.com/api/v1/entities/APPLICATION/online_auc")
submitRequest("https://truesight.bmc.com/api/v1/entities/DEVICE/oa-appserver-1")
submitRequest("https://truesight.bmc.com/api/v1/entities/TRANSACTION/oa-appserver-1.bid-tx")
submitRequest("https://truesight.bmc.com/api/v1/entities/TRANSACTION/oa-appserver-1.browse-catalog")

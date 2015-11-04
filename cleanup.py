import json
import pycurl
from requests.auth import HTTPDigestAuth
import os



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

apikey = os.environ["TSI_API_KEY"]


submitRequest("https://truesight.bmc.com/api/v1/entities/APPLICATION/online_auc")
submitRequest("https://truesight.bmc.com/api/v1/entities/DEVICE/oa-appserver-1")
submitRequest("https://truesight.bmc.com/api/v1/entities/TRANSACTION/oa-appserver-1.bid-tx")
submitRequest("https://truesight.bmc.com/api/v1/entities/TRANSACTION/oa-appserver-1.browse-catalog")

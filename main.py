import advertools as adv
import pandas as pd
import requests
import json
import time

sitemap_urls = adv.sitemap_to_df("https://weird-jokes.com/static/img/sitemap.xml")
url0 = sitemap_urls["loc"].to_list()
url=url0[2:100]

def get_(data):
    headers={'User-Agent':'curl/7.12.1 ',
             'Content-Type':'application/json'}
    try:
        r = requests.post(url='https://ssl.bing.com/webmaster/api.svc/json/SubmitUrl?apikey=536f58671234572dbe066b4aada63a62',json=data)
        print(r.status_code)
        print(r.content)
    except Exception.e:
        print(e)

for i in url:

          my_json_payload={
                            "siteUrl": "https://weird-jokes.com/",
                            "url": i
                          }
          print(my_json_payload)
          get_(my_json_payload)                
          time.sleep(3)

print(len(url)) 
print('Thats all, folks !!!') 

import json
from django.http import HttpResponse
import requests
from urllib.parse import unquote
import urllib.request

try:
    from urllib import request
except ImportError:
    import urllib
def lambda_handler(event, context):
#     query = event['queryStringParameters']
#     if len(query) == 0:
#         welcome = """
# <html>
# <form action="?" method="GET">
#   <input type="text" id="url" name="url" ><br><br>
#   <input type="submit" value="Submit">
# </form> 
# </body>
# </html>
#         """    
#         return {
#         'statusCode': 200, 
#         'headers': {"Content-Type":"text/html"},
#         'body': welcome
#         }
#     else:
        
    url = "http://www.draugiem.lv"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
    except (requests.ConnectionError, requests.Timeout) as exception:
    	print("No internet connection.")
        
        
        # Url = query['url']
        # print(Url)
        # print(unquote(Url))
        # url = unquote(Url)
                
        # req = urllib.request.Request(
        #     url, 
        #     data=None, 
        #     headers={
        #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        #       }
        # )
                
        # response = request.urlopen(req)
        # print(response.code, " JA ŠEIT RĀDĀS 200, TAD VISS SAIET!")
        # XML = response.read()
        # XML = XML.decode("UTF-8")
        # print(XML)   
        
    return {
        'statusCode': 200, 
        'headers': {"Content-Type":"text/html"},
        # 'body': query['url']+" downloaded"
    }
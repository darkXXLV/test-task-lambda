import json
from django.http import HttpResponse
import requests
from urllib.parse import unquote
import urllib.request
import boto3

try:
    from urllib import request
except ImportError:
    import urllib
    
s3 = boto3.client('s3')

def lambda_handler(event, context):
    query = event['queryStringParameters']
    if len(query) == 0:
        welcome = """
<html>
<form action="?" method="GET">
  <input type="text" id="url" name="url" ><br><br>
  <input type="submit" value="Submit">
</form> 
</body>
</html>
        """    
        return {
        'statusCode': 200, 
        'headers': {"Content-Type":"text/html"},
        'body': welcome
        }
    else:
        Url = query['url']
        print(Url)
        print(unquote(Url))
        url = unquote(Url)
                
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
               }
        )
                
        response = request.urlopen(req)
        print(response.code, " JA ŠEIT RĀDĀS 200, TAD VISS SAIET!")
        XML = response.read()
        XML = XML.decode("UTF-8")
        s3.put_object(Bucket='nedarita', Key='test.xml', Body=XML)
        
        return {
        'statusCode': 200, 
        'headers': {"Content-Type":"text/html"},
        'body': url+" downloaded"
        }
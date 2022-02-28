import json

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
        #do download/upload part
        return {
        'statusCode': 200, 
        'headers': {"Content-Type":"text/html"},
        'body': query['url']+" downloaded"
        }
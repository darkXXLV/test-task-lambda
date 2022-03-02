import json
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
<!doctype html>
<html lang="en" class="h-100">
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"> 
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </head>
    <body class="h-100">
        <div class="container h-100">
            <div class="row h-100 justify-content-center align-items-center">
                <div class="col-10 col-md-8 col-lg-6">
                    <!-- Form -->
                    <form class="form-example" action="?" method="GET">
                        <h2>Webpage source code downloader</h2>
                        <p class="description">Downloads webpage source code to Amazon S3 bucket.</p>
                        <!-- Input fields -->
                        <div class="form-group">
                            <label for="username">Insert URL:</label>
                            <input type="text" class="form-control username" id="url" placeholder="URL..." name="url">
                        </div>

                        <input type="submit" class="btn btn-primary btn-customized"></input>
                        <!-- End input fields -->
                        <p class="copyright">&copy; Kristaps Baumanis 2022</p>
                    </form>
                    <!-- Form end -->
                </div>
            </div>
        </div>
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
        event['queryStringParameters'] = ""
        
        return lambda_handler(event, context)
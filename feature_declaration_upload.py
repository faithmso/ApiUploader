import requests
import pandas as pd
import json

def uploads():
    #create a pandas data frame from a csv file
    df = pd.read_csv("C:/Users/FaithMu/Downloads/apiupload.csv.csv", dtype=str)

    #create a list called fileuploads that has a dictionary with a key called documentType with a value called "SupplierDeclaration"
    fileuploads = [{"documentType": "SupplierDeclaration"}]

    #create a loop that goes through each row in the csv file
    for index, row in df.iterrows():
        #obtain declarationlocation, declaration name and file type from the dataframe
        declaration_location = row['declarationlocation']
        declaration_name = row['declarationname']
        filetype = row['filetype']

        #create a naming for the file that will be uploaded to the API
        filename = declaration_location + declaration_name
        files = [({'declaration_name'},('file', open({'filename'},'rb'), 'application/octet-stream'))]

        #make an api call
        url = "https://api.stg.assentcompliance.com/v1/GlobalCatalogApi/files/supportingDocs"

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en',
            'Assent-Context-Key': '949726e4-31d1-4254-9f0f-702e2bed1e36',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5zdGcuYXNzZW50Y29tcGxpYW5jZS5jb20iLCJzdWIiOiJmYWl0aC5tdXRob25pQGFzc2VudGNvbXBsaWFuY2UuY29tIiwiaWF0IjoxNjc1ODUwMDA5LCJhdWQiOlsiKiJdLCJleHAiOjE2NzU5MDc2MDksImp0aSI6IjRhMzQ2NTU2LTRlYWEtNDEwOS04MDBkLWE1NmNkZThiNGVlOCIsImN0eCI6IjNjYTFmODRjLTgzN2EtNDE0Zi1hNTFkLWRjMWFhMjQxOWM1MiIsInR5cGUiOiJBY20iLCJpcCI6IjEwLjEwLjMwLjI1MSIsImVtYWlsIjoiZmFpdGgubXV0aG9uaUBhc3NlbnRjb21wbGlhbmNlLmNvbSIsInVnaWQiOiJhMzgzMzRjYi1lZWY2LTQ3OGItYmI2Mi04MTNkODc2MTZlZWUiLCJBQ1AuQWNjZXNzQ29ycmVjdGl2ZUFjdGlvbnMiOiJ0cnVlIiwiQUNQLkFjY2Vzc0RlY2xhcmF0aW9uU2VhcmNoIjoiZmFsc2UiLCJBQ1AuQWNjZXNzRXhjZXB0aW9uTWFuYWdlbWVudCI6ImZhbHNlIiwiQUNQLkFjY2Vzc0luZGlyZWN0TW9uaXRvcmluZyI6ImZhbHNlIiwiQUNQLkFjY2Vzc1NlZ21lbnRhdGlvblJlcG9ydCI6ImZhbHNlIiwiQUNQLkFjY2Vzc1RyYW5zYWN0aW9uTG9ncyI6ImZhbHNlIiwiQUNQLkFjY2Vzc1VzZXJNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuQWRkQ29ycmVjdGl2ZUFjdGlvblJlY29yZHMiOiJmYWxzZSIsIkFDUC5BZGRJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5BZGRJbmRpcmVjdE1vbml0b3JpbmdSZWNvcmRzIjoiZmFsc2UiLCJBQ1AuQ3JlYXRlQ29yZU9yZ2FuaXphdGlvbiI6ImZhbHNlIiwiQUNQLkRlbGV0ZUNvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRGVsZXRlSW5kaXJlY3RNb25pdG9yaW5nS2V5d29yZHNMaXN0IjoiZmFsc2UiLCJBQ1AuRGVsZXRlSW5kaXJlY3RNb25pdG9yaW5nUmVjb3JkcyI6ImZhbHNlIiwiQUNQLkVkaXRDb21wYW55UHJvZmlsZSI6ImZhbHNlIiwiQUNQLkVkaXRDb250YWN0TWFuYWdlbWVudCI6ImZhbHNlIiwiQUNQLkVkaXRDb3JyZWN0aXZlQWN0aW9uUmVjb3JkcyI6ImZhbHNlIiwiQUNQLkVkaXRJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5FZGl0SW5kaXJlY3RNb25pdG9yaW5nUmVjb3JkcyI6ImZhbHNlIiwiQUNQLkZ1bGxWaWV3Q29ycmVjdGl2ZUFjdGlvblJlY29yZHMiOiJ0cnVlIiwiQUNQLk1hbmFnZUNvcnJlY3RpdmVBY3Rpb25UZW1wbGF0ZXMiOiJmYWxzZSIsIkFDUC5SZXNwb25kVG9Db3JyZWN0aXZlQWN0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdBc3NpZ25lZENvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuVmlld0NvbXBhbnlQcm9maWxlIjoiZmFsc2UiLCJBQ1AuVmlld0NvbnRhY3RNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuVmlld0RyYWZ0T3JnYW5pemF0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5WaWV3SW5kaXJlY3RNb25pdG9yaW5nUmVjb3JkcyI6ImZhbHNlIiwiQUNQLlZpZXdOZXR3b3JrRGVjbGFyYXRpb25zIjoiZmFsc2UiLCJBQ1AuVmlld05vTWF0Y2hTdXBwbGllcnMiOiJmYWxzZSJ9.0UvpZFqqyEYEsgLqRXiLxhL6UpZ1mr5WYdK30gzMQiI',
            'Connection': 'keep-alive',
            'Origin': 'https://supplierportal.stg.assentcompliance.com',
            'Portal-Host': 'networkdeclarationlibrary.stg.assentcompliance.com',
            'Referer': 'https://supplierportal.stg.assentcompliance.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Cookie': 'AWSALB=TeRHI/huBCC4yjtpL1Pbs76iDbECH414Kw/hqdDOWgspx3jN87yLpbSlkFdTCKW5U222Gp5y5HsidJR5Jt27suAKsEfx1ceqHxWEty70MMhgKIUt++m5lu5vpz3s; AWSALBCORS=TeRHI/huBCC4yjtpL1Pbs76iDbECH414Kw/hqdDOWgspx3jN87yLpbSlkFdTCKW5U222Gp5y5HsidJR5Jt27suAKsEfx1ceqHxWEty70MMhgKIUt++m5lu5vpz3s'
        }

        response = requests.request("POST", url, headers=headers, files=files)
        print(response.status_code)
        data = json.loads(response.text.encode('utf8'))
        uniqueName = data["uniqueName"]
        url = {"files/" + uniqueName + "/supportingdocs"}
        file = {"name": "name", "size": 0, "uniqueName": uniqueName, "url": url}
        fileuploads.append(file)
        print(fileuploads)



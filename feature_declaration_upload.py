import requests
import pandas as pd
import json
import os

def declaration_upload():

    # Read the CSV into a pandas dataframe
    df = pd.read_csv("C:/Users/FaithMu/Downloads/apiupload.csv", dtype=str)

    # Initialize the fileuploads list
    fileuploads = []

    # Iterate through each row in the dataframe
    for index, row in df.iterrows():
        # Get the declarationlocation and declarationname for each row
        declarationlocation = row["DeclarationLocation"]
        declarationname = row["DeclarationName"]
        filename = declarationlocation + declarationname
        file = [(declarationname, ('file', open(filename, 'rb'), 'application/octet-stream'))]



        #debugging
        if os.path.exists(filename):
            file_for_api = []
            file_for_api.append(file)
        else:
            print("File does not exist: " + filename)


        # Loop through each file in the file_for_api list
        for file in file_for_api:
            # Call the API and obtain the uniquename and url
            url = "https://api.stg.assentcompliance.com/v1/GlobalCatalogApi/files/supportingDocs"

            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en',
                'Assent-Context-Key': 'a3c07c69-132c-47f6-ac2d-b45a4aeba23f',
                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5zdGcuYXNzZW50Y29tcGxpYW5jZS5jb20iLCJzdWIiOiJmYWl0aC5tdXRob25pQGFzc2VudGNvbXBsaWFuY2UuY29tIiwiaWF0IjoxNjc1OTM3ODI1LCJhdWQiOlsiKiJdLCJleHAiOjE2NzU5OTU0MjUsImp0aSI6IjZjMmUxZjdmLWU1ZDUtNGYwNS1iMmFlLTRjYTU1N2UwMDEwNCIsImN0eCI6ImZlNmZmMjQyLTIyYTgtNDk4Mi1hZTg2LWM2NWZmMTQyMGZmZSIsInR5cGUiOiJBY20iLCJpcCI6IjEwLjEwLjMwLjI1MSIsImVtYWlsIjoiZmFpdGgubXV0aG9uaUBhc3NlbnRjb21wbGlhbmNlLmNvbSIsInVnaWQiOiJhMzgzMzRjYi1lZWY2LTQ3OGItYmI2Mi04MTNkODc2MTZlZWUiLCJBQ1AuQWNjZXNzQ29ycmVjdGl2ZUFjdGlvbnMiOiJ0cnVlIiwiQUNQLkFjY2Vzc0RlY2xhcmF0aW9uU2VhcmNoIjoiZmFsc2UiLCJBQ1AuQWNjZXNzRXhjZXB0aW9uTWFuYWdlbWVudCI6ImZhbHNlIiwiQUNQLkFjY2Vzc0luZGlyZWN0TW9uaXRvcmluZyI6ImZhbHNlIiwiQUNQLkFjY2Vzc1NlZ21lbnRhdGlvblJlcG9ydCI6ImZhbHNlIiwiQUNQLkFjY2Vzc1RyYW5zYWN0aW9uTG9ncyI6ImZhbHNlIiwiQUNQLkFjY2Vzc1VzZXJNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuQWRkQ29ycmVjdGl2ZUFjdGlvblJlY29yZHMiOiJmYWxzZSIsIkFDUC5BZGRJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5BZGRJbmRpcmVjdE1vbml0b3JpbmdSZWNvcmRzIjoiZmFsc2UiLCJBQ1AuQ3JlYXRlQ29yZU9yZ2FuaXphdGlvbiI6ImZhbHNlIiwiQUNQLkRlbGV0ZUNvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRGVsZXRlSW5kaXJlY3RNb25pdG9yaW5nS2V5d29yZHNMaXN0IjoiZmFsc2UiLCJBQ1AuRGVsZXRlSW5kaXJlY3RNb25pdG9yaW5nUmVjb3JkcyI6ImZhbHNlIiwiQUNQLkVkaXRDb21wYW55UHJvZmlsZSI6ImZhbHNlIiwiQUNQLkVkaXRDb250YWN0TWFuYWdlbWVudCI6ImZhbHNlIiwiQUNQLkVkaXRDb3JyZWN0aXZlQWN0aW9uUmVjb3JkcyI6ImZhbHNlIiwiQUNQLkVkaXRJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5FZGl0SW5kaXJlY3RNb25pdG9yaW5nUmVjb3JkcyI6ImZhbHNlIiwiQUNQLkZ1bGxWaWV3Q29ycmVjdGl2ZUFjdGlvblJlY29yZHMiOiJ0cnVlIiwiQUNQLk1hbmFnZUNvcnJlY3RpdmVBY3Rpb25UZW1wbGF0ZXMiOiJmYWxzZSIsIkFDUC5SZXNwb25kVG9Db3JyZWN0aXZlQWN0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdBc3NpZ25lZENvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuVmlld0NvbXBhbnlQcm9maWxlIjoiZmFsc2UiLCJBQ1AuVmlld0NvbnRhY3RNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuVmlld0RyYWZ0T3JnYW5pemF0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5WaWV3SW5kaXJlY3RNb25pdG9yaW5nUmVjb3JkcyI6ImZhbHNlIiwiQUNQLlZpZXdOZXR3b3JrRGVjbGFyYXRpb25zIjoiZmFsc2UiLCJBQ1AuVmlld05vTWF0Y2hTdXBwbGllcnMiOiJmYWxzZSJ9.qyVsuINlsYr7r7VEgyTn-wVyWRmd9mW7trrSzBj8clo',
                'Connection': 'keep-alive',
                'Origin': 'https://supplierportal.stg.assentcompliance.com',
                'Portal-Host': 'networkdeclarationlibrary.stg.assentcompliance.com',
                'Referer': 'https://supplierportal.stg.assentcompliance.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Cookie': 'AWSALB=ofH5FoOk7xR+htESRIoGKjyfwk4Wav1iCWWz8bVmui4jEdn28TRYYkPcgJ3/b1bNgSkKP2PjyPTMGD1cHPIJmWsIVHIORMFNVV41LG7m+nsUYcMUjF358D/gJtTn; AWSALBCORS=ofH5FoOk7xR+htESRIoGKjyfwk4Wav1iCWWz8bVmui4jEdn28TRYYkPcgJ3/b1bNgSkKP2PjyPTMGD1cHPIJmWsIVHIORMFNVV41LG7m+nsUYcMUjF358D/gJtTn'
            }

            try:

                response = requests.request("POST", url, headers=headers, files=file)

                if response.status_code == 200:

                    # Get the uniquename and url from the API response
                    uniqueName = response.json()["uniqueName"]
                    url = "files/" + uniqueName + "/supportingdocs"
                    size = os.path.getsize(filename)

                    # Append the uniquename and url to the file key in the fileuploads list
                    fileuploads.append(
                        {
                            "DocumentTypes": "SupplierDeclaration",
                            "file": {
                                "uniquename": uniqueName,
                                "size": size,
                                "url": url
                            }
                        }
                    )
                    print("file upload successful")

                else:
                    print("file upload failed")

            except Exception as e:
                print("file upload failed")


    #print the fileuploads list
    print(fileuploads)

declaration_upload()






















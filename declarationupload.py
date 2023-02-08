import requests
import os


"""

fileUploads: [
    {
        "documentType": "SupplierDeclaration",
        # "isXml": False,
        "file": {
            "name": "REACH SVHC_Acceptance Criteria_German.pdf",
            "size": 331297,
            "uniqueName": "1d512972-8f71-4e2a-8fff-827112db5193",
            # "aiDocumentId": 0,
            "url": "files/1d512972-8f71-4e2a-8fff-827112db5193/supportingdocs",
            # "type": "pdf"
        }
    }
],
 """



"""
    Uploads declaration(s) and provides their declarationGUID.
    Arg 1: declaration name
    Arg 2: declaration path
    Arg 3: document type

    return: dict "fileUploads"

    Notes: This method needs to work with more than one document to be uploaded.
    Multiple documents come in one string separated by a '#'.
    """

"""    import requests

    url = "https://api.stg.assentcompliance.com/v1/GlobalCatalogApi/files/supportingDocs"

    payload = ""
    headers = {
        "cookie": "AWSALB=oHVXz6bWJ%2BNu6JRFhuvDBMwwMaM0wekK46wYM8kg6BgxYtJJXNEyg%2BnxjlPRJ5aVvToAjOWoA%2BdpvTwmK%2BVDW4qW%2BWeh%2FsD%2Bv3haG%2FGZy7lytfd1TgT1lmpTPkFa; AWSALBCORS=oHVXz6bWJ%2BNu6JRFhuvDBMwwMaM0wekK46wYM8kg6BgxYtJJXNEyg%2BnxjlPRJ5aVvToAjOWoA%2BdpvTwmK%2BVDW4qW%2BWeh%2FsD%2Bv3haG%2FGZy7lytfd1TgT1lmpTPkFa",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en",
        "Assent-Context-Key": "87ff8242-82eb-421a-aea2-f48a97e70fa3",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5zdGcuYXNzZW50Y29tcGxpYW5jZS5jb20iLCJzdWIiOiJuZGwzQGFzc2VudGNvbXBsaWFuY2UuY29tIiwiaWF0IjoxNjc0NjM0ODQ2LCJhdWQiOlsibmV0d29ya2RlY2xhcmF0aW9ubGlicmFyeS5zdGcuYXNzZW50Y29tcGxpYW5jZS5jb20iXSwiZXhwIjoxNjc0NjkyNDQ2LCJqdGkiOiI5MmUyZjg2Ny00ZjJiLTRkYTktOGJmNS05OTM4YjI3NDYyYWIiLCJjdHgiOiI1NDcyYzAyNi03MzU3LTRiZWYtOGM1Ny03ZmU1ZTM0NWRlNWEiLCJ0eXBlIjoiQWNtIiwiaXAiOiIxMC4xMC4zMC4yNTEiLCJlbWFpbCI6Im5kbDNAYXNzZW50Y29tcGxpYW5jZS5jb20iLCJ1Z2lkIjoiNDNkNTk2MmEtZTgzYy00NmMxLWJmOWMtMmUxYWEwNzk4NzE4IiwiQUNQLkFjY2Vzc0NvcnJlY3RpdmVBY3Rpb25zIjoiZmFsc2UiLCJBQ1AuQWNjZXNzRGVjbGFyYXRpb25TZWFyY2giOiJmYWxzZSIsIkFDUC5BY2Nlc3NFeGNlcHRpb25NYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuQWNjZXNzSW5kaXJlY3RNb25pdG9yaW5nIjoiZmFsc2UiLCJBQ1AuQWNjZXNzU2VnbWVudGF0aW9uUmVwb3J0IjoiZmFsc2UiLCJBQ1AuQWNjZXNzVHJhbnNhY3Rpb25Mb2dzIjoiZmFsc2UiLCJBQ1AuQWNjZXNzVXNlck1hbmFnZW1lbnQiOiJmYWxzZSIsIkFDUC5BZGRDb3JyZWN0aXZlQWN0aW9uUmVjb3JkcyI6ImZhbHNlIiwiQUNQLkFkZEluZGlyZWN0TW9uaXRvcmluZ0tleXdvcmRzTGlzdCI6ImZhbHNlIiwiQUNQLkFkZEluZGlyZWN0TW9uaXRvcmluZ1JlY29yZHMiOiJmYWxzZSIsIkFDUC5DcmVhdGVDb3JlT3JnYW5pemF0aW9uIjoiZmFsc2UiLCJBQ1AuRGVsZXRlQ29ycmVjdGl2ZUFjdGlvblJlY29yZHMiOiJmYWxzZSIsIkFDUC5EZWxldGVJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5EZWxldGVJbmRpcmVjdE1vbml0b3JpbmdSZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRWRpdENvbXBhbnlQcm9maWxlIjoiZmFsc2UiLCJBQ1AuRWRpdENvbnRhY3RNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuRWRpdENvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRWRpdEluZGlyZWN0TW9uaXRvcmluZ0tleXdvcmRzTGlzdCI6ImZhbHNlIiwiQUNQLkVkaXRJbmRpcmVjdE1vbml0b3JpbmdSZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRnVsbFZpZXdDb3JyZWN0aXZlQWN0aW9uUmVjb3JkcyI6ImZhbHNlIiwiQUNQLk1hbmFnZUNvcnJlY3RpdmVBY3Rpb25UZW1wbGF0ZXMiOiJmYWxzZSIsIkFDUC5SZXNwb25kVG9Db3JyZWN0aXZlQWN0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdBc3NpZ25lZENvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuVmlld0NvbXBhbnlQcm9maWxlIjoiZmFsc2UiLCJBQ1AuVmlld0NvbnRhY3RNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuVmlld0RyYWZ0T3JnYW5pemF0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5WaWV3SW5kaXJlY3RNb25pdG9yaW5nUmVjb3JkcyI6ImZhbHNlIiwiQUNQLlZpZXdOZXR3b3JrRGVjbGFyYXRpb25zIjoiZmFsc2UiLCJBQ1AuVmlld05vTWF0Y2hTdXBwbGllcnMiOiJmYWxzZSJ9.fQ5OYH_aYjKb5M8YUZxp0BCvdkLoRGu-KqAA2EOMFZQ",
        "Connection": "keep-alive",
        "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
        "Origin": "https://supplierportal.stg.assentcompliance.com",
        "Portal-Host": "networkdeclarationlibrary.stg.assentcompliance.com",
        "Referer": "https://supplierportal.stg.assentcompliance.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "sec-ch-ua": ""Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": ""Windows""
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)"""


def declaration_upload():



    folder_path = os.path.join('C:', 'Users', 'FaithMu', 'Documents')
    file_paths = []
    for file_name in os.listdir(folder_path):
        file_paths.append(os.path.join(folder_path, file_name))


    url = "https://api.stg.assentcompliance.com/v1/GlobalCatalogApi/files/supportingDocs"

    files = []
    for file_path in file_paths:
        files.append(('file', (file_path, open(file_path, 'rb'), 'application/pdf')))

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en',
        'Assent-Context-Key': '87ff8242-82eb-421a-aea2-f48a97e70fa3',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5zdGcuYXNzZW50Y29tcGxpYW5jZS5jb20iLCJzdWIiOiJuZGwzQGFzc2VudGNvbXBsaWFuY2UuY29tIiwiaWF0IjoxNjc0NjM0ODQ2LCJhdWQiOlsibmV0d29ya2RlY2xhcmF0aW9ubGlicmFyeS5zdGcuYXNzZW50Y29tcGxpYW5jZS5jb20iXSwiZXhwIjoxNjc0NjkyNDQ2LCJqdGkiOiI5MmUyZjg2Ny00ZjJiLTRkYTktOGJmNS05OTM4YjI3NDYyYWIiLCJjdHgiOiI1NDcyYzAyNi03MzU3LTRiZWYtOGM1Ny03ZmU1ZTM0NWRlNWEiLCJ0eXBlIjoiQWNtIiwiaXAiOiIxMC4xMC4zMC4yNTEiLCJlbWFpbCI6Im5kbDNAYXNzZW50Y29tcGxpYW5jZS5jb20iLCJ1Z2lkIjoiNDNkNTk2MmEtZTgzYy00NmMxLWJmOWMtMmUxYWEwNzk4NzE4IiwiQUNQLkFjY2Vzc0NvcnJlY3RpdmVBY3Rpb25zIjoiZmFsc2UiLCJBQ1AuQWNjZXNzRGVjbGFyYXRpb25TZWFyY2giOiJmYWxzZSIsIkFDUC5BY2Nlc3NFeGNlcHRpb25NYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuQWNjZXNzSW5kaXJlY3RNb25pdG9yaW5nIjoiZmFsc2UiLCJBQ1AuQWNjZXNzU2VnbWVudGF0aW9uUmVwb3J0IjoiZmFsc2UiLCJBQ1AuQWNjZXNzVHJhbnNhY3Rpb25Mb2dzIjoiZmFsc2UiLCJBQ1AuQWNjZXNzVXNlck1hbmFnZW1lbnQiOiJmYWxzZSIsIkFDUC5BZGRDb3JyZWN0aXZlQWN0aW9uUmVjb3JkcyI6ImZhbHNlIiwiQUNQLkFkZEluZGlyZWN0TW9uaXRvcmluZ0tleXdvcmRzTGlzdCI6ImZhbHNlIiwiQUNQLkFkZEluZGlyZWN0TW9uaXRvcmluZ1JlY29yZHMiOiJmYWxzZSIsIkFDUC5DcmVhdGVDb3JlT3JnYW5pemF0aW9uIjoiZmFsc2UiLCJBQ1AuRGVsZXRlQ29ycmVjdGl2ZUFjdGlvblJlY29yZHMiOiJmYWxzZSIsIkFDUC5EZWxldGVJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5EZWxldGVJbmRpcmVjdE1vbml0b3JpbmdSZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRWRpdENvbXBhbnlQcm9maWxlIjoiZmFsc2UiLCJBQ1AuRWRpdENvbnRhY3RNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuRWRpdENvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRWRpdEluZGlyZWN0TW9uaXRvcmluZ0tleXdvcmRzTGlzdCI6ImZhbHNlIiwiQUNQLkVkaXRJbmRpcmVjdE1vbml0b3JpbmdSZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRnVsbFZpZXdDb3JyZWN0aXZlQWN0aW9uUmVjb3JkcyI6ImZhbHNlIiwiQUNQLk1hbmFnZUNvcnJlY3RpdmVBY3Rpb25UZW1wbGF0ZXMiOiJmYWxzZSIsIkFDUC5SZXNwb25kVG9Db3JyZWN0aXZlQWN0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdBc3NpZ25lZENvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuVmlld0NvbXBhbnlQcm9maWxlIjoiZmFsc2UiLCJBQ1AuVmlld0NvbnRhY3RNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuVmlld0RyYWZ0T3JnYW5pemF0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5WaWV3SW5kaXJlY3RNb25pdG9yaW5nUmVjb3JkcyI6ImZhbHNlIiwiQUNQLlZpZXdOZXR3b3JrRGVjbGFyYXRpb25zIjoiZmFsc2UiLCJBQ1AuVmlld05vTWF0Y2hTdXBwbGllcnMiOiJmYWxzZSJ9.fQ5OYH_aYjKb5M8YUZxp0BCvdkLoRGu-KqAA2EOMFZQ',
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
        'Cookie': 'AWSALB=tAIL0HRBQ0RGvqHuR75srijbAFHXTufD0IFyU45vdBYcKJ481QUDEKZ7vs/ZXBhX9OO/p+voTxg98xFVFPHe+haDLL3g675n13zA1+l0N6WQu6lGOjGmAVSHQS41; AWSALBCORS=tAIL0HRBQ0RGvqHuR75srijbAFHXTufD0IFyU45vdBYcKJ481QUDEKZ7vs/ZXBhX9OO/p+voTxg98xFVFPHe+haDLL3g675n13zA1+l0N6WQu6lGOjGmAVSHQS41'
    }

    response = requests.post(url, headers=headers, files=files)

    print(response.text)
    return response.text


       

import requests
import json




def declaration_upload(template):

  #template is a file path where the files are stored

  template = "C:/Users/FaithMu/Documents/"

  #for each file in the template, upload the file to the server
  for file in template:
      #the naming convention for the files is filepath which is template + file name + "file_type"

      files = [({file}, {'file': (file, open(template + file, 'rb'), 'application/pdf')})]
      url = "https://api.stg.assentcompliance.com/v1/GlobalCatalogApi/files/supportingDocs"
      payload = {}
      headers = {
          'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'en',
          'Assent-Context-Key': 'd75ee78a-f248-43c7-9bb6-979234657d49',
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5zdGcuYXNzZW50Y29tcGxpYW5jZS5jb20iLCJzdWIiOiJuZGwzQGFzc2VudGNvbXBsaWFuY2UuY29tIiwiaWF0IjoxNjc1Nzc0NDYwLCJhdWQiOlsibmV0d29ya2RlY2xhcmF0aW9ubGlicmFyeS5zdGcuYXNzZW50Y29tcGxpYW5jZS5jb20iXSwiZXhwIjoxNjc1ODMyMDYwLCJqdGkiOiI3MDQzZTg2MC0zOGZjLTQ5NTctOGQzNS1iMGE0YTNjMmE4MzUiLCJjdHgiOiIyZDgzN2M0My02MDEyLTQwYTUtOTVhNC02NWE2Y2E0ODhiNDUiLCJ0eXBlIjoiQWNtIiwiaXAiOiIxMC4xMC4zMC4yNTEiLCJlbWFpbCI6Im5kbDNAYXNzZW50Y29tcGxpYW5jZS5jb20iLCJ1Z2lkIjoiNDNkNTk2MmEtZTgzYy00NmMxLWJmOWMtMmUxYWEwNzk4NzE4IiwiQUNQLkFjY2Vzc0NvcnJlY3RpdmVBY3Rpb25zIjoiZmFsc2UiLCJBQ1AuQWNjZXNzRGVjbGFyYXRpb25TZWFyY2giOiJmYWxzZSIsIkFDUC5BY2Nlc3NFeGNlcHRpb25NYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuQWNjZXNzSW5kaXJlY3RNb25pdG9yaW5nIjoiZmFsc2UiLCJBQ1AuQWNjZXNzU2VnbWVudGF0aW9uUmVwb3J0IjoiZmFsc2UiLCJBQ1AuQWNjZXNzVHJhbnNhY3Rpb25Mb2dzIjoiZmFsc2UiLCJBQ1AuQWNjZXNzVXNlck1hbmFnZW1lbnQiOiJmYWxzZSIsIkFDUC5BZGRDb3JyZWN0aXZlQWN0aW9uUmVjb3JkcyI6ImZhbHNlIiwiQUNQLkFkZEluZGlyZWN0TW9uaXRvcmluZ0tleXdvcmRzTGlzdCI6ImZhbHNlIiwiQUNQLkFkZEluZGlyZWN0TW9uaXRvcmluZ1JlY29yZHMiOiJmYWxzZSIsIkFDUC5DcmVhdGVDb3JlT3JnYW5pemF0aW9uIjoiZmFsc2UiLCJBQ1AuRGVsZXRlQ29ycmVjdGl2ZUFjdGlvblJlY29yZHMiOiJmYWxzZSIsIkFDUC5EZWxldGVJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5EZWxldGVJbmRpcmVjdE1vbml0b3JpbmdSZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRWRpdENvbXBhbnlQcm9maWxlIjoiZmFsc2UiLCJBQ1AuRWRpdENvbnRhY3RNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuRWRpdENvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRWRpdEluZGlyZWN0TW9uaXRvcmluZ0tleXdvcmRzTGlzdCI6ImZhbHNlIiwiQUNQLkVkaXRJbmRpcmVjdE1vbml0b3JpbmdSZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRnVsbFZpZXdDb3JyZWN0aXZlQWN0aW9uUmVjb3JkcyI6ImZhbHNlIiwiQUNQLk1hbmFnZUNvcnJlY3RpdmVBY3Rpb25UZW1wbGF0ZXMiOiJmYWxzZSIsIkFDUC5SZXNwb25kVG9Db3JyZWN0aXZlQWN0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdBc3NpZ25lZENvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuVmlld0NvbXBhbnlQcm9maWxlIjoiZmFsc2UiLCJBQ1AuVmlld0NvbnRhY3RNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuVmlld0RyYWZ0T3JnYW5pemF0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5WaWV3SW5kaXJlY3RNb25pdG9yaW5nUmVjb3JkcyI6ImZhbHNlIiwiQUNQLlZpZXdOZXR3b3JrRGVjbGFyYXRpb25zIjoiZmFsc2UiLCJBQ1AuVmlld05vTWF0Y2hTdXBwbGllcnMiOiJmYWxzZSJ9.m3fG-WNIEitnHKsD1I1GQa1p39nzMLlAVT3czJdLoIk',
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
          'Cookie': 'AWSALB=ravpgaw99NXSOn/8ZABcS+8Kp7oXQdGVfa4LH5JuLa6iC0kTI9kwJqlxfeEGUJQqK8gNahjYUpfpaNNJOTRM9BgQ7FHhCtZ97BZiQQ54UJvM6GUh13EgaKtrV4mv; AWSALBCORS=ravpgaw99NXSOn/8ZABcS+8Kp7oXQdGVfa4LH5JuLa6iC0kTI9kwJqlxfeEGUJQqK8gNahjYUpfpaNNJOTRM9BgQ7FHhCtZ97BZiQQ54UJvM6GUh13EgaKtrV4mv'
        }

      response = requests.request("POST", url, headers=headers, data = payload, files = files)
      data = json.loads(response.text)



  files = [
    ('TE_Product(2176401-9)REACH 224-ROHS3_November 2022.pdf', (
    'file', open('C:/Users/FaithMu/Documents/TE_Product(2176401-9)REACH 224-ROHS3_November 2022.pdf', 'rb'),
    'application/octet-stream'))
  ]

  fileUploads = []

  url = "https://api.stg.assentcompliance.com/v1/GlobalCatalogApi/files/supportingDocs"

  payload = {}

  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en',
    'Assent-Context-Key': 'd75ee78a-f248-43c7-9bb6-979234657d49',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5zdGcuYXNzZW50Y29tcGxpYW5jZS5jb20iLCJzdWIiOiJuZGwzQGFzc2VudGNvbXBsaWFuY2UuY29tIiwiaWF0IjoxNjc1Nzc0NDYwLCJhdWQiOlsibmV0d29ya2RlY2xhcmF0aW9ubGlicmFyeS5zdGcuYXNzZW50Y29tcGxpYW5jZS5jb20iXSwiZXhwIjoxNjc1ODMyMDYwLCJqdGkiOiI3MDQzZTg2MC0zOGZjLTQ5NTctOGQzNS1iMGE0YTNjMmE4MzUiLCJjdHgiOiIyZDgzN2M0My02MDEyLTQwYTUtOTVhNC02NWE2Y2E0ODhiNDUiLCJ0eXBlIjoiQWNtIiwiaXAiOiIxMC4xMC4zMC4yNTEiLCJlbWFpbCI6Im5kbDNAYXNzZW50Y29tcGxpYW5jZS5jb20iLCJ1Z2lkIjoiNDNkNTk2MmEtZTgzYy00NmMxLWJmOWMtMmUxYWEwNzk4NzE4IiwiQUNQLkFjY2Vzc0NvcnJlY3RpdmVBY3Rpb25zIjoiZmFsc2UiLCJBQ1AuQWNjZXNzRGVjbGFyYXRpb25TZWFyY2giOiJmYWxzZSIsIkFDUC5BY2Nlc3NFeGNlcHRpb25NYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuQWNjZXNzSW5kaXJlY3RNb25pdG9yaW5nIjoiZmFsc2UiLCJBQ1AuQWNjZXNzU2VnbWVudGF0aW9uUmVwb3J0IjoiZmFsc2UiLCJBQ1AuQWNjZXNzVHJhbnNhY3Rpb25Mb2dzIjoiZmFsc2UiLCJBQ1AuQWNjZXNzVXNlck1hbmFnZW1lbnQiOiJmYWxzZSIsIkFDUC5BZGRDb3JyZWN0aXZlQWN0aW9uUmVjb3JkcyI6ImZhbHNlIiwiQUNQLkFkZEluZGlyZWN0TW9uaXRvcmluZ0tleXdvcmRzTGlzdCI6ImZhbHNlIiwiQUNQLkFkZEluZGlyZWN0TW9uaXRvcmluZ1JlY29yZHMiOiJmYWxzZSIsIkFDUC5DcmVhdGVDb3JlT3JnYW5pemF0aW9uIjoiZmFsc2UiLCJBQ1AuRGVsZXRlQ29ycmVjdGl2ZUFjdGlvblJlY29yZHMiOiJmYWxzZSIsIkFDUC5EZWxldGVJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5EZWxldGVJbmRpcmVjdE1vbml0b3JpbmdSZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRWRpdENvbXBhbnlQcm9maWxlIjoiZmFsc2UiLCJBQ1AuRWRpdENvbnRhY3RNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuRWRpdENvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRWRpdEluZGlyZWN0TW9uaXRvcmluZ0tleXdvcmRzTGlzdCI6ImZhbHNlIiwiQUNQLkVkaXRJbmRpcmVjdE1vbml0b3JpbmdSZWNvcmRzIjoiZmFsc2UiLCJBQ1AuRnVsbFZpZXdDb3JyZWN0aXZlQWN0aW9uUmVjb3JkcyI6ImZhbHNlIiwiQUNQLk1hbmFnZUNvcnJlY3RpdmVBY3Rpb25UZW1wbGF0ZXMiOiJmYWxzZSIsIkFDUC5SZXNwb25kVG9Db3JyZWN0aXZlQWN0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdBc3NpZ25lZENvcnJlY3RpdmVBY3Rpb25SZWNvcmRzIjoiZmFsc2UiLCJBQ1AuVmlld0NvbXBhbnlQcm9maWxlIjoiZmFsc2UiLCJBQ1AuVmlld0NvbnRhY3RNYW5hZ2VtZW50IjoiZmFsc2UiLCJBQ1AuVmlld0RyYWZ0T3JnYW5pemF0aW9ucyI6ImZhbHNlIiwiQUNQLlZpZXdJbmRpcmVjdE1vbml0b3JpbmdLZXl3b3Jkc0xpc3QiOiJmYWxzZSIsIkFDUC5WaWV3SW5kaXJlY3RNb25pdG9yaW5nUmVjb3JkcyI6ImZhbHNlIiwiQUNQLlZpZXdOZXR3b3JrRGVjbGFyYXRpb25zIjoiZmFsc2UiLCJBQ1AuVmlld05vTWF0Y2hTdXBwbGllcnMiOiJmYWxzZSJ9.m3fG-WNIEitnHKsD1I1GQa1p39nzMLlAVT3czJdLoIk',
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
    'Cookie': 'AWSALB=ravpgaw99NXSOn/8ZABcS+8Kp7oXQdGVfa4LH5JuLa6iC0kTI9kwJqlxfeEGUJQqK8gNahjYUpfpaNNJOTRM9BgQ7FHhCtZ97BZiQQ54UJvM6GUh13EgaKtrV4mv; AWSALBCORS=ravpgaw99NXSOn/8ZABcS+8Kp7oXQdGVfa4LH5JuLa6iC0kTI9kwJqlxfeEGUJQqK8gNahjYUpfpaNNJOTRM9BgQ7FHhCtZ97BZiQQ54UJvM6GUh13EgaKtrV4mv'
  }
  """for file in files:
    response = requests.request("POST", url, headers=headers, data=payload, files=file)
    print('Hello')
    data = response.text
    print(data)
    print(response.status_code)"""
  # loop through files and make a rewuest for each file
  # for file in files:
  #   response = requests.request("POST", url, headers=headers, data=payload, files=file)
  #   print(response.text)
  #   print(response.status_code)
  #   data = response.text
  #   data = json.loads(data)
  #   uniqueName = data["uniqueName"]
  #   url = {"files/" + uniqueName + "/supportingdocs"}
  #   file = {"name": "name", "size": 0, "uniqueName": uniqueName, "url": url}
  #   fileUploads.append(file)
  #   print(fileUploads)

  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  print(response.text)
  print(response.status_code)
  data = response.text
  data = json.loads(data)
  uniqueName = data["uniqueName"]
  url = {"files/" + uniqueName + "/supportingdocs"}
  file = {"name": "name", "size": 0, "uniqueName": uniqueName, "url": url}
  fileUploads.append(file)
  print(fileUploads)



declaration_upload()













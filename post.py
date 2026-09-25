import requests
url="https://jsonplaceholder.typicode.com/posts"
payload=   {
    "userId": 1,
    "id": 1,
    "title": "Post using Python. Automation",
    "body": "This is a post"
  }
respone=requests.post(url,json=payload)
print(respone.status_code)
print(respone.json())
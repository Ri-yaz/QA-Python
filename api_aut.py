#API AUTOMATION USING REQUESTS MODULE
import requests

url="https://jsonplaceholder.typicode.com/posts"
respone=requests.get(url)
print(respone.status_code)
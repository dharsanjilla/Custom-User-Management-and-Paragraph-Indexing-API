from django.test import TestCase

# Create your tests here.
import requests

#test1
url = 'http://127.0.0.1:8000/api/register/'
data = {
    "email": "user@example.com",
    "username": "newuser",
    "password": "secretpassword"
}

response = requests.post(url, json=data)
print(response.status_code)  # Should be 201 for successful creation
print(response.json())       


#test2

url = 'http://127.0.0.1:8000/api/login'

data = {'username': 'example_user', 'password': 'example_password'}

response = requests.post(url, data=data)
print(response.status_code)  
print(response.json())   


#test3
url = 'http://127.0.0.1:8000/api/paragraphs'
data={
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
}
response = requests.post(url, data=data)
print(response.status_code)  
print(response.json())  

#test4
url = 'http://127.0.0.1:8000/api/search'
data = {'word': 'dolor'}
response = requests.post(url, data=data)
print(response.status_code)  
print(response.json()) 






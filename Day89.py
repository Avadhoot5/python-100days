# Requests Module 
import requests, bs4

# response = requests.get("https://www.google.com")
# print(response.text)

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'Test',
#     "body": 'Message',
#     "userId": 1
# }

# headers = {
#     'Content-type': 'application/json; charset=UTF-8',
# }

# response = requests.post(url, headers = headers, json = data)
# print(response.text)

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
receive = requests.get(url)
# print(receive.text)

soup = bs4.BeautifulSoup(receive.text, 'html.parser')
# print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)




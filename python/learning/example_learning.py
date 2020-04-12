import requests
from urllib.parse import quote
import json

# first try
def example_parse_some_data():
  url = "https://openlibrary.org/search.json?q=clean%20code"
  return requests.get(url)

def example_get_some_json():
  url = "https://openlibrary.org/search.json?q=clean%20code"
  response = requests.get(url)
  return response.json()

def example_get_author():
  url = "https://openlibrary.org/search.json?q=clean%20code"
  response = requests.get(url)
  json = response.json()
  print(json)
  return json["docs"][0]["author_name"][0]

def example_find_first_author(book_name):
  search = quote(book_name)
  url = "https://openlibrary.org/search.json?q=" + search
  response = requests.get(url)
  json = response.json()
  return json["docs"][0]["author_name"][0]

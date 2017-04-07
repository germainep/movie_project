import json
import requests

def movie_lookup(movie_title):
    url = "http://www.omdbapi.com/?t=" + movie_title
    response = requests.get(url)
    data = json.loads(response.text)
    return data

class Movie(): 
  def  __init__(self, title, trailer_youtube_url):
    self.title = title
    self.plot = movie_lookup(title)['Plot']
    self.poster_image_url = movie_lookup(title)['Poster']
    self.trailer_youtube_url = trailer_youtube_url

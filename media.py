import json
import requests

#looks up the movie from the imdb api
def movie_lookup(movie_title):
    url = "http://www.omdbapi.com/?t=" + movie_title
    response = requests.get(url)
    data = json.loads(response.text) #parses json data
    return data

class Movie(): 
  def  __init__(self, title, trailer_youtube_url):
    self.title = title
    #passes the title to movie_look up and returns the Plot and Poster Art 
    self.plot = movie_lookup(title)['Plot']
    self.poster_image_url = movie_lookup(title)['Poster']
    self.trailer_youtube_url = trailer_youtube_url

from flask import Flask, render_template
import requests


def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMzA1MjhlNDFkZWUxN2ZmODkyMTRlOThiOTg5YWY5YiIsInN1YiI6IjYwM2FiOGIyNDM0OTRmMDA2OGFlZDFhZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hOWmg9QcGYgdQF-Qt0YsyNZW_GCj-QxbH-7jZ0dsEys"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

get_popular_movies()

def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_path}"

def get_movie_info():
    dict = { "title" : "url"}
    return dict

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

#@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


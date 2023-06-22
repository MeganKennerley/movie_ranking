import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

article_content = soup.find_all(name="a", rel="noopener")
all_movies = [movie.getText() for movie in article_content if movie.getText().startswith("Read Empire's")]

movie_titles = []
for string in all_movies:
    movie_titles.append(string.split("of ", 1)[1])

with open("movies.txt", mode="w") as file:
    i = 0
    for movie in movie_titles:
        i += 1
        file.write(f"{i}) {movie}\n")

from bs4 import BeautifulSoup
import requests

URL = 'https://www.empireonline.com/movies/features/best-movies-2'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())

# all_movies = soup.find_all('h3', class_='title')
all_movies = soup.find_all('h3')
movie_titles = [movie.getText() for movie in all_movies]
# Reversing list with '[::1]'
movies = movie_titles[::1]

# Saving to .txt file
with open('movies.txt', mode='w') as file:
  for movie in movies:
    file.write(f'{movie}\n')

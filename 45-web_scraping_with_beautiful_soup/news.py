from bs4 import BeautifulSoup
import requests

page = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.title.text)

# For first result only
article_title = soup.find('span', class_='titleline').getText()
print(article_title)
article_link = soup.select('.titleline > a')[0].get('href')
print(article_link)
article_votes = soup.find('span', class_='score').getText()
print(article_votes)

# To find info for all articles
articles = soup.select('.titleline > a')
raw_scores = soup.find_all('span', class_='score')
# using list comprehension to convert vote text to intigers
votes = [int(score.getText().split(" ")[0]) for score in raw_scores]


# BUG: this actually does not account for articles with no votes so there are fewer votes than articles. The data are on different table rows. Could grab all, make every 1st the titles, every 2nd the votes but check for null/no values.
# print(f'# of articles: {len(articles)}')
# print(f'# of raw scores: {len(raw_scores)}')
# print(f'# of votes: {len(votes)}')
# print(votes)

# Print all articles, links and # votes
# for index, article in enumerate(articles):
#   print(index)
#   print(f'Title: {article.getText()}')
#   print(f'Link: {article.get("href")}')
  # print(f'Votes: {votes[index]}')


  # Find the highest ranked article (ingnoring bug for now)
def find_most_votes(votes):
  index_of_max = None

  for index, vote in enumerate(votes):
    if index_of_max is None or vote > votes[index_of_max]:
      index_of_max = index

  return index_of_max

highest_index = find_most_votes(votes)

print(f'The highest voted article today is {articles[highest_index]} with {votes[highest_index]} votes.')


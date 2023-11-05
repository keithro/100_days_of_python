# need to use the correct conda env and you can ignore warning
from bs4 import BeautifulSoup

# Importing our html page
with open('./website.html', 'r') as file:
  contents = file.read()
  # print(contents)

soup = BeautifulSoup(contents, 'html.parser') # I think you can remove '.parser' & just use 'html'
# pretty output
print(soup.prettify)
# get first element
print(soup.title)
# get element's name
print(soup.title.name)
# get string content of element
print(soup.title.string)

# get_all
all_anchor_tags = soup.find_all(name='a')

for tag in all_anchor_tags:
  # getText() accepts arguments, without any arguments is the same .text
  print(tag.getText())
  print(tag.get('href'))

# find using id
heading = soup.find(name='h1', id='name')
print(heading)
heading_list = soup.select('#name')
print(heading_list)

# find using class (can eliminate 'name=')
section_heading = soup.find('h3', class_='heading')
print(section_heading)
section_heading_list = soup.select('.heading')
print(section_heading_list)

# using multiple selectors
company_url = soup.select_one(selector='p a #name')
print(company_url)

from bs4 import BeautifulSoup
import requests


url = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&view=simple"
i = 1

for x in range(5):

    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')

    for movie in soup.find_all('div', class_='lister-item mode-simple'):

        title = movie.span.a.text

        rating = movie.find('div', class_='col-imdb-rating')
        rating = rating.strong.text

        year = movie.find(
            'span', class_='lister-item-year text-muted unbold').text
        year = year[1:5]

        rating = rating.strip('\n')
        rating = rating.strip(' ')
        rating = rating.strip('\n')

        print(f"Rating: {i}")
        print(f"Title: {title}")
        print(f"Rating: {rating}")
        print(f"Release year: {year}")
        print()
        i += 1

    url = soup.find('a', class_="lister-page-next next-page")
    url = url.get('href', None)
    url = f"https://www.imdb.com{url}"

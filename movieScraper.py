from urllib.request import urlopen
from bs4 import BeautifulSoup

url_scrape = "https://www.cinemark.com/theatres/ca-union-city/century-25-union-landing-and-xd?utm_medium=organic&utm_source=gmb&utm_campaign=int&utm_content=GMB_listing&y_source=1_MTc0OTMwNTAtNzE1LWxvY2F0aW9uLmdvb2dsZV93ZWJzaXRlX292ZXJyaWRl"

reqeust = urlopen(url_scrape)
page_html = request.read()
request.close()

html_parse = BeautifulSoup(page_html, 'html.parser')

movies_list = html_soup.findall('div', class_="col-xs-12 col-sm-8 showtimeColumn contentMain")

filename = 'moviesList.csv'
f = open(filename, 'w')
header = 'Title, Time \n'

f.write(header)

for movies in movies_list:
    movie_title = movies.find('div', class_="clearfix").text
    movie_time = movies.find('div', class_="showtime").text
    f.write(movie_title + ',' + movie_time)

f.close

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
# import lxml

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

chrome_driver_path = "YOUR_DRIVER_PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://www.imdb.com/chart/top/"

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, 'html.parser')

all_movies = []

table = soup.find('tbody', class_='lister-list')
rows = table.find_all('tr')

all_movie_name = []

for row in rows:
    movies = row.find('td', class_='titleColumn')
    movie_name = movies.find('a').text.strip()
    all_movie_name.append(movie_name)
print(all_movie_name)

all_rating = []
for row in rows:
    rating = row.find('td', class_='ratingColumn imdbRating').text.strip()
    all_rating.append(rating)
print(all_rating)
# print(len(rows))


gform = 'YOUR_GOOGLE_FORM_LINK'
chrome_driver_path = "YOUR_DRIVER_PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(rows)):
    driver.get(gform)
    time.sleep(2)

    movie_fill = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rating_fill = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')

    movie_fill.send_keys(all_movie_name[n])
    rating_fill.send_keys(all_rating[n])
    submit_button.click()

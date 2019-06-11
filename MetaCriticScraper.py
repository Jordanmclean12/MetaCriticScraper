
import re
import lxml
import facebook
import random
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/50.0.2661.102 Safari/537.36'}


def genre_get(output):
    url = "https://www.metacritic.com/game"
    result = 0

    for i in range(100):
        try:
            result = requests.get(url, headers=headers)
        except:
            continue
        break

    soup = BeautifulSoup(result.content.decode(), "lxml")
    main_soup = soup.find("ul", {"class": "genre_nav"})
    link_list = []

    for content in main_soup.find_all('a', href=True):
        if content.text:
            link_builder = "https://www.metacritic.com" + (content['href'])
            link_list.append(link_builder)

    if output:
        print(link_list)

    genre_picker(False, link_list)


def genre_picker(output, link_list):
    genre = random.choice(link_list)

    if output:
        print(genre)

    game_get(False, genre)


def game_get(output, genre):
    genre_page = 0

    for i in range(100):
        try:
            genre_page = requests.get(genre, headers=headers)
        except:
            continue
        break

    soup = BeautifulSoup(genre_page.content.decode(), "lxml")
    genre_soup = soup.find("ol", {"class": "list_products list_product_condensed"})
    game_list = []

    for game in genre_soup.find_all('a', href=True):
        if game.text:
            game_builder = "https://www.metacritic.com" + (game['href'])
            game_list.append(game_builder)

    if output:
        print(game_list)

    game_picker(output, game_list)


def game_picker(output, game_list):
    game = random.choice(game_list)

    if output:
        print(game)

    info_get(True, game)


def info_get(output, game):
    game_page = 0

    for i in range(100):
        try:
            game_page = requests.get(game, headers=headers)
        except:
            continue
        break

    soup = BeautifulSoup(game_page.content.decode(), "lxml")

    product_title_div = soup.find("div", {"class": "product_title"})
    product_title = product_title_div.find('h1').text

    product_platform_div = soup.find("span", {"class": "platform"})
    product_platform = product_platform_div.find('a').text.strip()

    critic_score = soup.find("span", {"itemprop": "ratingValue"}).text

    info_string = ("Game: " + product_title + "\n" +
              "Platform: " + product_platform + "\n" +
              "Critic Score: " + critic_score)

    if output:
        print(info_string)

    review = (game+"/user-reviews")
    review_get(True, review, info_string)


def review_get(output, review, info_string):
    review_page = 0

    for i in range(100):
        try:
            review_page = requests.get(review, headers=headers)
        except:
            continue
        break

    soup = BeautifulSoup(review_page.content.decode(), "lxml")
    review_soup = soup.find("ol", {"class": "reviews user_reviews"})
    review_list = []

    if soup.find("div", {"class": "msg msg_no_reviews"}):
        genre_get(False)
    else:
        for rev in review_soup.find_all("li", id=re.compile("^user_review_\d+")):
            if rev.text:
                review_list.append(rev)

    user_review = random.choice(review_list)

    username_div = user_review.find("div", {"class": "name"})
    username = username_div.text

    review_date = user_review.find("div", {"class": "date"}).text
    review_details = username.strip() + " | " + review_date.strip()

    review_score_div = user_review.find("div", {"class": "review_grade"})
    review_score = review_score_div.text.strip()

    review_contents = user_review.find("div", {"class": "review_body"})
    review_content = ""

    if review_contents.find("span", {"class": "blurb blurb_expanded"}):
        content_soup = review_contents.find("span", {"class": "blurb blurb_expanded"})
        for text in content_soup.findAll(text=True):
            review_content += text + "\n"

    else:
        content_soup = review_contents.find('span')
        for text in content_soup.findAll(text=True):
            review_content += text + "\n"

    review_string = ("\n" +
                     review_details + "\n" +
                     "User Rating: " + review_score + "/10" + "\n" + "\n" +
                     review_content)

    post_string = info_string + review_string

    if output:
        print(review_string)

    print(post_string)


# main
genre_get(False)
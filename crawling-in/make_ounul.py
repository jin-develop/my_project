import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\\Users\\nick0\\Desktop\\chromedriver')
import time
import random


from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbikea



ounul_sofa = 'https://ohou.se/store/category?category=0_1_0_3'
ounul_img = 'https://ohou.se'
def make_ounul_sofa():
    # URL을 읽어서 HTML를 받아오고, 데이터 가져오기 까지


    driver.get(ounul_sofa)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦


    for i in range(7):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        driver.implicitly_wait(10)
        time.sleep(5)

    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')

    # select를 이용해서, tr들을 불러오기
    sofas = soup.select('div.virtualized-list > div ')

    for sofa in sofas:
        a_href = sofa.select_one('article.production-item')
        if a_href is not None:
            href = ounul_img + a_href.select_one('a')['href']


            real_href = ounul_img + href
            name1 = a_href.select_one('div.production-item__content > h1 ')
            brand = name1.select_one('span.production-item__header__brand').text
            name = name1.select_one('span.production-item__header__name').text

            if a_href.select_one('div.production-item__image > img') is None:
                continue

            img_url = a_href.select_one('div.production-item__image > img')['src']


            price = a_href.select_one('div.production-item__content > span.production-item-price > span.production-item-price__price').text.strip()


            print(brand)
            print(name)
            print(price)
            print(href)
            print(img_url)

            # ##### DB에 추가하기,
            doc = {
                'brand': brand,
                'name': name,
                'price': price,
                'url': href,
                'img': img_url,
                'like': 0
            }

            db.sofas.insert_one(doc)
            # # 만약 중복된것이 있으면 삭제하기 기능,
            # # img 사진이 중복된것이 있다면 삭제하기

    print('*' * 80)

# 기존 sofas 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def insert_all():
      # sofas 콜렉션을 모두 지워줍니다.
    make_ounul_sofa()



insert_all()


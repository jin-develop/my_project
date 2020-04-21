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



ikea_url = 'https://www.ikea.com/kr/ko/'
# chair_url = 'https://www.ikea.com/kr/ko/cat/chairs-fu002/' # 의자를 선택하면 뒤에 cat/chairs-fu002/
# sofa_url = 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/' #sofa를 선택하면 cat/all-sofas-39130/

''''' 소파를 선택하면 아래 저장된 sofa_url_dict 에 있는 링크들이 실행이 되게 할수 있게.
        의자를 선택하면 역시 chair_url_dict가 실행되게.
    or 색상이라는 링크를 들어가서 자동으로 크롤링 하기.'''

def crawling():
    # URL을 읽어서 HTML를 받아오고, 데이터 가져오기 까지
    for i,j in sofa_url_dict.items():
        # 우선 1 페이지만 가져오기
        for k in range(1, 2):
            page = '&page={}'.format(k)

            real_page = j + page
            driver.get(real_page)

            req = driver.page_source
            time.sleep(1)
            color = i
            time.sleep(5)
            # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
            soup = BeautifulSoup(req, 'html.parser')

            # select를 이용해서, tr들을 불러오기
            sofas = soup.select('div.range-product-list__products > div ')

            for sofa in sofas:
                a_href = sofa.select_one('div.product-compact > div > a')
                if a_href is not None:
                    href = a_href['href']
                    # print(href)
                    # print(sofa)

                    name1 = a_href.select_one('span.product-compact__name').text
                    name2 = a_href.select_one('span.product-compact__type').text

                    name = name1 + ' ' + name2.strip()
                    price = a_href.select_one('span.product-compact__price').text.strip()
                    img_url = a_href.select_one('div.product-compact__image-container > div > div > img')['src']
                    print(color)
                    print(name)
                    print(price)
                    print(href)
                    print(img_url)

                    ##### DB에 추가하기,
                    doc = {
                        'color': color,
                        'name': name,
                        'price': price,
                        'url': href,
                        'img': img_url
                    }

                    db.sofas.insert_one(doc)
                    # 만약 중복된것이 있으면 삭제하기 기능,
                    # img 사진이 중복된것이 있다면 삭제하기

            print('*'*80)


# 기존 sofas 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def insert_all():
    db.sofas.drop()  # sofas 콜렉션을 모두 지워줍니다.
    crawling()



insert_all()




# # DB에 있는 정보들 에서 사진가져오기.
# # 아무 사진 가져오기.
# all_sofa = list(db.sofas.find())
# sofa_samples = random.sample(all_sofa, 5) #all_sofa에서 랜덤으로 sofa 5개 가져오기
# # 2가지 사진을 고르고 다음을 선택하면 2가지 사진과 관련된 색상의 소파가 나옴.
#
#
# #그냥 둘러보는 사람들을 위한 랜덤 이미지
# def rand_sofa():
#     all_sofa = list(db.sofas.find())
#     rand_sofa_one = random.sample(all_sofa, 50)



import requests
from bs4 import BeautifulSoup

dongsuh_sofa = {
    '4인' : 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001002',
    '2,3인': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001003',
    '1인': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001004',
    '소파베드': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001006'
}
dongsuh_chair = {

}
dong_suh_img = 'http://www.dongsuhfurniture.co.kr'
def make_dongsuh_sofa():
    for i,j in dongsuh_sofa.items():

        # URL을 읽어서 HTML를 받아오고,
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(j ,headers=headers)

        # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        soup = BeautifulSoup(data.text, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        sofas = soup.select('div.content > div.goods_list_item > div.goods_list > div.goods_list_cont > div.item_gallery_type > ul > li')


        for sofa in sofas:
            a_href = sofa.select_one('div.item_cont')
            if a_href is not None:
                href = a_href.select_one('div.item_photo_box > a')['href']
                # print(href)
                # print(sofa)
                real_href = dong_suh_img + href
                name1 = a_href.select_one('div.item_photo_box > a > img')['title']

                img_url = a_href.select_one('div.item_photo_box')['data-image-magnify']
                real_img_url = dong_suh_img + img_url

                price = a_href.select_one('div.item_info_cont > div.item_money_box > strong.item_price > span').text.strip()

                print(name1)
                print(price)
                print(real_href)
                print(real_img_url)

                doc = {
                    'brand': '동서가구',
                    'name': name1,
                    'price': price,
                    'url': href,
                    'img': img_url
                }

                db.sofas.insert_one(doc)


make_dongsuh_sofa()
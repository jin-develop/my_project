import requests
from bs4 import BeautifulSoup

sofa_url_dict = {
    'gray': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EA%B7%B8%EB%A0%88%EC%9D%B4%2410028',
    '베이지': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%B2%A0%EC%9D%B4%EC%A7%80%2410003',
    'black': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%B8%94%EB%9E%99%2410139',
    'brown': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%B8%8C%EB%9D%BC%EC%9A%B4%2410019',
    'white': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%ED%99%94%EC%9D%B4%ED%8A%B8%2410156',
    'Green': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EA%B7%B8%EB%A6%B0%2410033',
    'Blue': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%B8%94%EB%A3%A8%2410007',
    'Red': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%A0%88%EB%93%9C%2410124',
    'Multi-color': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%A9%80%ED%8B%B0%EC%BB%AC%EB%9F%AC%2410583',
    'Pink': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%ED%95%91%ED%81%AC%2410119',
    'Emerald': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%ED%84%B0%EC%BF%BC%EC%9D%B4%EC%A6%88%2410152'
}



# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.ikea.com/kr/ko/cat/all-sofas-39130/?page=2',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
sofas = soup.select('div.catalog-product-list__fragment')

# name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
# img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
# recent = soup.select_one(
#         '#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text

for sofa in sofas:
# div.catalog-product-list__fragment > div.product-compact > div.product-compact__spacer >
    name1 = sofa.select_one('span.product-compact__name').text
    name2 = sofa.select_one('span.product-compact__type').text

    name = name1 + name2
    img_url = sofa.select_one('div.product-compact__image-container > div.product-compact__image > div.range-image-claim-height >img')['src']
    price = sofa.select_one('span.product-compact__price__value').text
        # song_name = name[0].text.strip()
        # artist = name[1].text
        # print('*'*70)
        # print('{}   {}   {}'.format(rank, song_name, artist)) # <- TODO: 굿입니다!


    # doc = {
    #     'name': '엄청 편한 소파 ',
    #     'price': 50000,
    #     'color': 'black'
    # }
    print(name)
    print(img_url)
    print(price)
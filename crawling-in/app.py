import requests
from bs4 import BeautifulSoup
import time
import random
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbikea                     # 'dbikea'라는 이름의 db를 만듭니다.



color_dict = {#'예시 링크 화이트' : 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%ED%99%94%EC%9D%B4%ED%8A%B8%2410156',
    'gray': '%2410028',
    'beige': '%2410003',
    'black': '%2410139',
    'brown': '%2410019',
    'white': '%2410156',
    'Green': '%2410033',
    'Blue': '%2410007',
    'Red': '%2410124',
    'Multi-color': '%2410583',
    'Pink': '%2410119',
    'Emerald': '%2410152'
}

sofa_url_dict = {
    'gray': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EA%B7%B8%EB%A0%88%EC%9D%B4%2410028',
    'beige': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%B2%A0%EC%9D%B4%EC%A7%80%2410003',
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





## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/info', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기 
    # 랜덤으로 sofas 정렬
    sofas = list(db.sofas.find({}, {'_id': False}))
    random.shuffle(sofas)
    
    
    # 2. sofas라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'sofas': sofas})

## API 역할을 하는 부분
@app.route('/info', methods=['POST'])
def saving():
    # 1. 클라이언트로부터 데이터를 받기
    thing = request.form['thing_give']
    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})




# 기존 sofas 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.


#그냥 둘러보는 사람들을 위한 랜덤 이미지
def rand_sofa():
    all_sofa = list(db.sofas.find())
    rand_sofa_one = random.sample(all_sofa, 50)


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
import requests
from bs4 import BeautifulSoup
import time
import random
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbikea                     # 'dbikea'라는 이름의 db를 만듭니다.





## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/info/random', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기 
    # 랜덤으로 sofas 정렬
    sofas = list(db.sofas.find({}, {'_id': False}))
    chairs = list(db.chairs.find({}, {'_id': False}))
    random.shuffle(chairs)
    random.shuffle(sofas)
    rand = sofas + chairs
    random.shuffle(rand)
    
    return jsonify({'result':'success', 'rand': rand})


@app.route('/info/sofa', methods=['GET'])
def get_sofa():
    sofas = list(db.sofas.find({}, {'_id': False}))
    random.shuffle(sofas)
    return jsonify({'result':'success', 'sofas': sofas})


@app.route('/info/chair', methods=['GET'])
def get_chair():
    chairs = list(db.chairs.find({}, {'_id': False}))
    random.shuffle(chairs)
    return jsonify({'result':'success', 'chairs': chairs})


@app.route('/info/desk', methods=['GET'])
def get_desk():
    desks = list(db.desks.find({}, {'_id': False}))
    random.shuffle(desks)
    return jsonify({'result':'success', 'desks': desks})


## API 역할을 하는 부분
@app.route('/info', methods=['POST'])
def saving():
    # 1. 클라이언트로부터 데이터를 받기
    thing = request.form['thing_give']
    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})

## 데이터 지우기 


# 기존 sofas 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.


#그냥 둘러보는 사람들을 위한 랜덤 이미지
def rand_sofa():
    all_sofa = list(db.sofas.find())
    rand_sofa_one = random.sample(all_sofa, 50)


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
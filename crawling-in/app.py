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

@app.route('/go')
def go():
   return render_template('index2.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
       #Moving forward code
       forward_message = "Moving Forward..."
       return render_template('index.html')

@app.route('/info')
def info():
   return render_template('main.html')

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

@app.route('/info/price/sofa', methods=['POST'])
def get_price_sofa():
    min_price = request.form['min_price_give']
    max_price = request.form['max_price_give']
    sofa_list = []
    sofas = list(db.sofas.find({}, {'_id': False}))
    for sofa in sofas:
        price = int(sofa['price'].replace('￦','').replace('원','').strip().replace(',',''))
        if int(min_price) <= price and price <= int(max_price):
            sofa_list.append(sofa)
    random.shuffle(sofa_list)
    return jsonify({'result':'success', 'sofas': sofa_list})

@app.route('/info/price/chair', methods=['POST'])
def get_price_chair():
    min_price = request.form['min_price_give']
    max_price = request.form['max_price_give']
    sofa_list = []
    chairs = list(db.chairs.find({}, {'_id': False}))
    for sofa in chairs:
        price = int(sofa['price'].replace('￦','').replace('원','').strip().replace(',',''))
        if int(min_price) <= price and price <= int(max_price):
            sofa_list.append(sofa)
    random.shuffle(sofa_list)
    return jsonify({'result':'success', 'chairs': sofa_list})

@app.route('/info/price/desk', methods=['POST'])
def get_price_desk():
    min_price = request.form['min_price_give']
    max_price = request.form['max_price_give']
    sofa_list = []
    sofas = list(db.desks.find({}, {'_id': False}))
    for sofa in sofas:
        price = int(sofa['price'].replace('￦','').replace('원','').strip().replace(',',''))
        if int(min_price) <= price and price <= int(max_price):
            sofa_list.append(sofa)
    random.shuffle(sofa_list)
    return jsonify({'result':'success', 'desks': sofa_list})


## API 역할을 하는 부분





if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
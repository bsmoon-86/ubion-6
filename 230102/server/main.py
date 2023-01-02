## flask를 이용하여 웹 서버 구축
from flask import Flask, request, render_template
import random

## Flask class 생성
## __name__ : 현재 실행되는 파일의 이름
app = Flask(__name__)
app.config['DEBUG'] = True

## localhost:5000/ 에 요청시 아래에 있는 함수를 실행
@app.route("/")
## Hello World를 보내준다. 
def index():
    return render_template('index.html')

@app.route("/data")
def data():
    _pass = request.args['password']
    print(_pass)
    return ""

## 가위 바위 보 페이지 
@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/game2")
def game2():
    
    _user = request.args.get("user")
    list_ = ["가위", "바위", "보"]
    choicelist = random.choice(list_)
    if _user == choicelist:
        return "무승부"
    if _user == "가위":
        if choicelist =="바위":
            return "패"
        else:
            return "승"
    elif _user == "바위":
        if choicelist == "보":
            return "패"
        else:
            return "승"
    else :
        if choicelist == "가위":
            return "패"
        else:
            return "승"


app.run(port=8080)
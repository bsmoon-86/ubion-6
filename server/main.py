## flask라는 라이브러리를 로드 
from flask import Flask, render_template, request

## Flask라는 클래스를 생성
## __name__ : 자기 자신의 파일명
app = Flask(__name__)

## url 요청 주소 생성
## @ 해당하는 주소로 요청이 들어오면 아래에 있는 함수를 실행(네비게이션 함수)
@app.route("/")     ## '/'가 뜻하는바는? -> 127.0.0.1:5000/
def index():
    return "Hello World"

@app.route("/second")   ## 127.0.0.1 = localhost  (get 형식)
def second():
    req_id = request.args.get("id")
    req_pass = request.args.get("pass")
    print(req_id, req_pass)
    return render_template("second.html")

@app.route("/second", methods=["post"])
def post_page():
    req_id = request.form['id']
    req_pass = request.form['pass']
    ## id가 test 이고 password가 1234인 경우에는 second.html 보내주고
    ## 그 외의 경우라면 "login fail"
    # return req_id + req_pass
    if (req_id == "test") & (req_pass == "1234"):
        return render_template('second.html')
    else:
        return "login fail"

## html문서를 응답으로 보내는 방법
@app.route("/html")
def html():
    return render_template("index.html")

@app.route("/data", methods=["post"])
def data():
    req_menu = request.form['menu']
    print(req_menu)
    return render_template("data.html", menu = req_menu)


## 클래스 안에 있는 run() 함수를 실행
app.run(port="8080")
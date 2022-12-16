from flask import Flask

## Flask라는 클래스 생성 (파일의 이름)
## __name__ : 파일의 이름
app = Flask(__name__)

@app.route("/")     ## '/' request(요청)가 왔을때 아래에 있는 함수를 실행
def index():
    return "Hello"    ## user에게 response 

app.run()
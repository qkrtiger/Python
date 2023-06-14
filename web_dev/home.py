from flask import Flask, render_template # 클래스 가져오기

# flask 객체 생성
app = Flask(__name__)

# url 맵핑
@app.route("/")
def home():
    return '''
        <h1>hello flask</h1>
        <p>안녕하세요~</p>
        <p><a href="second/abcd">다음</a>
           <a href="third">세번째</a>
        </p>
        '''

@app.route("/second/<data>")
def second(data):
    return f'<h1>두번째 페이지</h1><p>{data}</p>'

@app.route("/third")
def third():
    m = 'hi~~'
    return render_template("third.html", msg=m)


if __name__ == '__main__':
    app.run(debug=True,port=8080)
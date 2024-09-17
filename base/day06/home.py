from flask import Flask, render_template, request

# flask 객체 생성
ap = Flask(__name__)

# url 메핑 함수 작성
@ap.route('/')
def home():
    return render_template('home.html')

@ap.route('/calcul')
def calcul():
    return render_template('calcul.html')

@ap.route('/calproc', methods=['GET'])
def calproc():
    n1 = request.args.get('num1', '')
    n2 = request.args.get('num2', '')
    print(n1, n2)
    n1 = int(n1)
    n2 = int(n2)
    return f'{n1} + {n2} = {n1 + n2}'

@ap.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form.get('id', '')
        pwd = request.form.get('pwd', '')
        print(id, pwd)
        return render_template('home.html')

if __name__ == '__main__':
    ap.run(debug=True, port=5000, host='192.168.0.66')